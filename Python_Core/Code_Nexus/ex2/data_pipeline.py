import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.fifo: list[typing.Any] = []
        self.counter = 0
        self.name = ""

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return (0, "")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Numeric Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int | float):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, int | float) for x in data)
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper numeric data")
        elif isinstance(data, list):
            for x in data:
                self.fifo.append(str(x))
        else:
            self.fifo.append(str(data))

    def output(self) -> tuple[int, str]:
        value: int = self.counter
        self.counter += 1
        return (value, self.fifo.pop(0))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Text Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper text data")
        elif isinstance(data, list):
            for x in data:
                self.fifo.append(x)
        else:
            self.fifo.append(data)

    def output(self) -> tuple[int, str]:
        value: int = self.counter
        self.counter += 1
        return (value, self.fifo.pop(0))


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Log Processor"

    def validate(self, data: typing.Any) -> bool:
        if (isinstance(data, dict) and
            all(isinstance(x, str) for x in data.keys()) and
                all(isinstance(x, str) for x in data.values())):
            return True
        elif isinstance(data, list):
            if all(isinstance(x, dict) and
                    all(isinstance(k, str) for k in x.keys()) and
                    all(isinstance(v, str) for v in x.values()) for x in data):
                return True
            return False
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper log data")
        elif isinstance(data, list):
            for elem in data:
                self.fifo.append(": ".join(elem.values()))
        else:
            self.fifo.append(": ".join(data.values()))

    def output(self) -> tuple[int, str]:
        value: int = self.counter
        self.counter += 1
        return (value, self.fifo.pop(0))


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream():
    def __init__(self) -> None:
        self.process: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.process.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        found: bool = False
        for elem in stream:
            found = False
            for x in self.process:
                if x.validate(elem):
                    found = True
                    x.ingest(elem)
            if not found:
                print(f"DataStream error - Can’t process "
                      f"element in stream: {elem}")

    def print_processors_stats(self) -> None:
        if len(self.process) == 0:
            print("No processor found, no data")
            return
        for proc in self.process:
            print(f"{proc.name}: "
                  f"total {len(proc.fifo) + proc.counter} "
                  f"items processed, remaining "
                  f"{len(proc.fifo)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for x in self.process:
            result: list[tuple[int, str]] = []
            if nb > len(x.fifo):
                nb = len(x.fifo)
            for i in range(nb):
                result.append(x.output())
            plugin.process_output(result)


class CSVExportPluging():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csvList: list[str] = []
        for x in data:
            csvList.append(x[1])
        csv: str = ",".join(csvList)
        print(f"CSV Output:\n{csv}")


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        JsonList: list[str] = []
        for x in data:
            JsonList.append(f"\"item_{str(x[0])}\": \"{x[1]}\"")
        JsonStr: str = ", ".join(JsonList)
        print(f"JSON Output:\n{{{JsonStr}}}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    csv: CSVExportPluging = CSVExportPluging()
    json: JSONExportPlugin = JSONExportPlugin()
    data: DataStream = DataStream()
    procs: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
        ]
    stream: list[typing.Any] = [
            "Hello world",
            [3.14, -1, 2.71],
            [
                {
                    "log_level": "WARNING",
                    "log_message": "Telnet access! Use ssh instead"
                },
                {
                    "log_level": "INFO",
                    "log_message": "User wil is connected"
                }
            ],
            42,
            ["Hi", "five"]
    ]
    stream_2: list[typing.Any] = [
        21,
        [
            "I love AI",
            "LLMs are wonderful",
            "Stay healthy"
        ],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
                }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]
    data.print_processors_stats()
    print("\nRegistering Processors\n")
    for proc in procs:
        data.register_processor(proc)
    data.process_stream(stream)
    print(f"Send first batch of data on stream: {stream}")
    print("== DataStream statistics ==")
    data.print_processors_stats()
    print("\nSend 3 processed data from each "
          "processor to a CSV plugin:")
    data.output_pipeline(3, csv)
    print("\n== DataStream statistics ==")
    data.print_processors_stats()
    data.process_stream(stream_2)
    print(f"Send anothoter batch of data: {stream_2}")
    print("\n== DataStream statistics ==")
    data.print_processors_stats()
    print("\nSend 5 processed data from each processor "
          "to a JSON plugin:")
    data.output_pipeline(5, json)
    print("\n== DataStream statistics ==")
    data.print_processors_stats()

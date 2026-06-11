import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.fifo: list[typing.Any] = []

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
        self.counter = 0

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
        self.counter = 0

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
        self.counter = 0

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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("Testing Numeric Processor...")
    numeric: NumericProcessor = NumericProcessor()
    text: TextProcessor = TextProcessor()
    log: LogProcessor = LogProcessor()
    print(f"Trying to validate input ’42’: {numeric.validate(42)}")
    print(f"Trying to validate input ’Hello’: {numeric.validate("Hello")}")
    print("Test invalid ingestion of string ’foo’ without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as err:
        print(err)
    nb: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {nb}")
    print("Extracting 3 values...")
    for x in range(3):
        try:
            numeric.ingest(nb[x])
            tmp: tuple[int, str] = numeric.output()
            print(f"Numeric value {tmp[0]}: {tmp[1]}")
        except ValueError as err:
            print(err)

    print("\nTesting Text Processor...")
    print(f"Trying to validate input ’42’: {text.validate(42)}")
    txt: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {txt}")
    print("Extracting 1 value...")
    text.ingest(txt[0])
    tmp = text.output()
    print(f"Text value {tmp[0]}: {tmp[1]}")

    print("\nTesting Log Processor...")
    print(f"Trying to validate input ’Hello’: {log.validate("Hello")}")
    logs: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
        ]
    print(f"Processing data: {logs}")
    print("Extracting 2 values...")
    log.ingest(logs)
    for x in range(2):
        tmp = log.output()
        print(f"Log entry {tmp[0]}: {tmp[1]}")

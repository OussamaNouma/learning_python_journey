import typing
import random


def gen_event(names: list[str], action: list[str])\
      -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(names), random.choice(action))


def consume_event(my_list: list[tuple[str, str]])\
      -> typing.Generator[tuple[str, str], None, None]:
    while my_list:
        yield my_list.pop(random.randrange(len(my_list)))


if __name__ == "__main__":
    names: list[str] = [
        "Solaire",
        "Havel",
        "Siegmeyer",
        "Laurentius"
    ]
    action: list[str] = [
        "cast Fireball",
        "run",
        "roll",
        "heal",
        "parry",
        "drink estus flask",
        "gitgud",
        "touch grass",
        "cast Sunlight Spear"
    ]
    print("=== Game Data Stream Processor ===")
    generator: typing.Generator[tuple[str, str], None, None]\
        = gen_event(names, action)
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events: list[tuple[str, str]] = []
    for i in range(10):
        ten_events.append(next(generator))
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")

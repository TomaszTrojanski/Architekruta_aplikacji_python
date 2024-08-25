from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class NumberGenerator:
    n: int
    a: int
    current_step: int = field(default=0)

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current_step > self.n:
            raise StopIteration
        result = self.a ** self.current_step
        self.current_step += 1
        return result


def generate_numbers(a: int, n: int) -> Iterator[int]:
    generator = NumberGenerator(n, a)
    for number in generator:
        yield number


def main() -> None:
    results = generate_numbers(4, 5)
    print(list(results))


if __name__ == '__main__':
    main()

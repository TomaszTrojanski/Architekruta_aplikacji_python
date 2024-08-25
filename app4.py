from math import sqrt
from typing import Final, List, Tuple
import multiprocessing


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def find_twin_prime_numbers(start_range: int, end_range: int) -> List[Tuple[int, int]]:
    prime_numbers = [n for n in range(start_range, end_range + 1) if is_prime(n)]
    return [(prime_numbers[i], prime_numbers[i + 1])
            for i in range(len(prime_numbers) - 1) if prime_numbers[i + 1] - prime_numbers[i] == 2]


def worker_fn(start_range: int, end_range: int) -> List[Tuple[int, int]]:
    return find_twin_prime_numbers(start_range, end_range)


def main() -> None:
    START_RANGE: Final[int] = 1
    END_RANGE: Final[int] = 250000
    num_processes: Final[int] = 4
    offset: int = (END_RANGE - START_RANGE) // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        ranges = [(START_RANGE + i * offset, START_RANGE + (i + 1) * offset - 1) for i in range(num_processes)]
        ranges[-1] = (ranges[-1][0], END_RANGE)

        results = pool.starmap(worker_fn, ranges)

    twin_prime_numbers = [item for sublist in results for item in sublist]
    print(twin_prime_numbers)

if __name__ == '__main__':
    main()

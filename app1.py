from typing import Callable
import logging
import inspect

logging.basicConfig(level=logging.INFO)


def log_function_args(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            logging.info(f'Variable {name}: {value}')

        return func(*args, **kwargs)
    return inner


@log_function_args
def sample_function(x: int, y: int, default_test: str = "test str") -> None:
    print("Inside sample_function")


def run() -> None:
    sample_function(1, y=2)


if __name__ == "__main__":
    run()

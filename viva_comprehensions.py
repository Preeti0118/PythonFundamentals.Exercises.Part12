from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    return a list of even or odd numbers between start anbd stop argumnents 
    depending on the argument parity. Return Odd for parity 0 abnd return Even for parity 1
    :param start: The first int inclusive.
    :param stop: The last int exclusive.
    :param parity: specifying odd and even
    :return: list of numbers
    """

    return [i for i in range(start, stop) if i % 2 != parity.value]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    accept arguments start and stop and return the value
    based on the function given in argument "strategy"
    :param start: starting integer in a dictionary (inclusive)
    :param stop: ending  integer in a dictionary (exclusive)
    :param strategy:A function to manipulate each digit
    :return: a dictionary integer
    """
    return {i: strategy(i) for i in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    accept an argument list val_in and return the list by converting it into upper case
    :param val_in: string
    :return: upper case list
    """
    return {word.upper() for word in val_in if word == word.lower()}


#
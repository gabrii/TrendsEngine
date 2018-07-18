import abc
from collections import Counter
from typing import Union, Iterable, Dict


class AbstractBackend(abc.ABC):

    @abc.abstractmethod
    def incr(self, key: str, value: Union[int, None] = 1) -> Union[int, None]:
        """Increments a given key by a value. If it doesn't exist, start at 0.
            The final value is returned when supported by the backend at no extra expense.
        """
        pass

    def incr_many(self, keys: Counter):
        """Increments all the keys by their respective values.
            keys = {str:int, ...}
        """
        for key, value in keys.items():
            self.incr(key, value)

    @abc.abstractmethod
    def get(self, key: str) -> int:
        """Return the count for a given key. If the key doesn't exist, returns 0 rather than None."""
        pass

    def get_many(self, keys: Iterable[str]) -> Dict[str, int]:
        return {key: self.get(key) for key in keys}


Backend = AbstractBackend

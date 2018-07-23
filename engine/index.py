from typing import Optional

from backends import AbstractBackend
from date_tools import date_suffix, date


class Index:

    def __init__(self, backend: AbstractBackend, tokenizer: None = None):
        self.backend = backend
        if tokenizer is None:
            tokenizer = self.simple_tokenizer
        self.tokenizer = tokenizer

    @staticmethod
    def simple_tokenizer(text: str) -> [str]:
        return text.split()

    def index_text(self, text: str, date: Optional[date] = None):
        words = self.tokenizer(text)
        suffix = ":"
        if date:
            suffix += date_suffix(date)

        for i in range(len(words)):
            for j in range(2):
                if i + j < len(words):
                    self.backend.incr('_'.join(words[i:1 + i + j]) + suffix)

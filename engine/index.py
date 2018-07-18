from backends import AbstractBackend


class Index:

    def __init__(self, backend: AbstractBackend, tokenizer: None = None):
        self.backend = backend
        if tokenizer is None:
            tokenizer = self.simple_tokenizer
        self.tokenizer = tokenizer

    @staticmethod
    def simple_tokenizer(text: str) -> [str]:
        return text.split()

    def index_text(self, text: str, date=None):
        words = self.tokenizer(text)

        for i in range(len(words)):
            for j in range(2):
                if i + j < len(words):
                    self.backend.incr('_'.join(words[i:1 + i + j]))

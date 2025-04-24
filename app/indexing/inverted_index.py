from collections import defaultdict


class InvertedIndex:

    def __init__(self):
        self.index = defaultdict(set)

    def build(self, logs):

        for idx, log in enumerate(logs):

            words = [
                log.level.lower(),
                log.user.lower(),
                log.message.lower(),
                log.server.lower()
            ]

            for word in words:
                self.index[word].add(idx)

    def search(self, term):

        return self.index.get(term.lower(), set())
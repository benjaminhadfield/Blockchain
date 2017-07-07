"""
Block represents a single block.
"""

import time
import hashlib


class Block:
    _count = 0

    def __init__(self, data, prev_hash, nonce=0):
        self.index = Block.get_index()
        self.timestamp = time.time()
        self.nonce = nonce
        self.data = data
        self.hash = self._get_hash()
        self.prev_hash = prev_hash

    @staticmethod
    def get_index():
        """Return and increment current count."""
        index = Block._count
        Block._count += 1
        return index

    @staticmethod
    def to_bytes(value):
        return str(value).encode()

    def _get_hash(self):
        h = hashlib.sha256()
        h.update(self.to_bytes(self.index))
        h.update(self.to_bytes(self.timestamp))
        h.update(self.to_bytes(self.nonce))
        h.update(self.to_bytes(self.data))
        return h.hexdigest()

    def print_self(self):
        print(
            'index \t{}'.format(self.index),
            'time \t{}'.format(self.timestamp),
            'nonce \t{}'.format(self.nonce),
            'data \t{}'.format(self.data),
            'prev \t{}'.format(self.prev_hash),
            'hash \t{}'.format(self.hash),
            '',
            sep='\n'
        )

    def __str__(self):
        return self.hash

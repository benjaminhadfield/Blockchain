"""
Block represents a single block.
"""

import time
import hashlib


class Block:
    _count = 0

    def __init__(self, data):
        self.index = Block.get_index()
        self.timestamp = time.time()
        self.nonce = 0  # this is the proof of work
        self.data = data
        self.prev_hash = None

        self.mine()

    @property
    def hash(self):
        h = hashlib.sha256()
        h.update(self.to_bytes(self.index))
        h.update(self.to_bytes(self.timestamp))
        h.update(self.to_bytes(self.nonce))
        h.update(self.to_bytes(self.data))
        return h.hexdigest()

    @staticmethod
    def get_index():
        """Return and increment current count."""
        index = Block._count
        Block._count += 1
        return index

    @staticmethod
    def to_bytes(value):
        return str(value).encode()

    def is_valid(self):
        prefix = '00000'
        return self.hash[:len(prefix)] == prefix

    def mine(self):
        """Loop through nonce values until the block becomes valid."""
        while not self.is_valid():
            self.nonce += 1

    def print_self(self):
        print(
            'index \t{}'.format(self.index),
            'time \t{}'.format(self.timestamp),
            'nonce \t{}'.format(self.nonce),
            'data \t{}'.format(self.data),
            'prev \t{}'.format(self.prev_hash),
            'hash \t{}'.format(self.hash),
            'valid \t{}'.format(self.is_valid()),
            '',
            sep='\n'
        )

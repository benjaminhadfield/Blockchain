"""
This class links Block objects together to form a chain.
"""

from .block import Block


class Blockchain:
    def __init__(self):
        # blocks stored as a dict for faster lookup
        self.blocks = {}

    def add_block(self, block):
        if isinstance(block, list):
            for b in block:
                self.add_block(b)

        if self.blocks.get(block.hash) is not None:
            raise AssertionError(
                '{} already exists on the blockchain.'.format(block.__str__()))
        self.blocks[block.hash] = block

    def __len__(self):
        return len(self.blocks)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError()
        return self.blocks.get(item)

    def __contains__(self, item):
        if not isinstance(item, Block):
            raise TypeError()
        return bool(self.__getitem__(item.hash))

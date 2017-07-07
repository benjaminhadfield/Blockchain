"""
This class links Block objects together to form a chain.
"""

from .block import Block


class Blockchain:
    def __init__(self):
        # blocks stored as a dict for faster lookup
        self.blocks = {}

    def add_block(self, *blocks):
        if len(blocks) > 1:
            for b in blocks:
                self.add_block(b)
        else:
            block = blocks[0]
            if self.blocks.get(block.hash) is not None:
                raise AssertionError(
                    'specified block already exists on the blockchain.')

            # assign the block to the blockchain

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

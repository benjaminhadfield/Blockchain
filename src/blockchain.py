"""
This class links Block objects together to form a chain.
"""


class Blockchain:
    def __init__(self):
        # blocks stored as a dict for faster lookup
        self.blocks = {}

    def add_block(self, block):
        if self.blocks.get(block.hash) is not None:
            raise AssertionError(
                '{} already exists on the blockchain.'.format(block.__str__()))
        self.blocks[block.hash] = block

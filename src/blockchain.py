"""
This class links Block objects together to form a chain.

The check for a valid block is arbitrarily set to be a hash with a particular
starting sequence in this simple example. However, in a production application
public/private key cryptography, or similar, should be used.
"""

from .block import Block


class Blockchain:
    def __init__(self):
        # blocks stored as a dict for faster lookup
        self.blocks = {}
        self.latest_hash = None

    def add_blocks(self, *blocks):
        """
        Takes a block, or multiple blocks, and adds them to the blockchain.
        The function takes care of setting the correct prev_hashes on the
        blocks.
        """
        if len(blocks) > 1:
            for b in blocks:
                self.add_blocks(b)
        else:
            block = blocks[0]

            # check input
            if not isinstance(block, Block):
                raise TypeError(
                    '\'{}\' is not an instance of block.'.format(block))
            if self.blocks.get(block.hash) is not None:
                raise AssertionError(
                    'specified block already exists on the blockchain.')

            # assign prev_hash to the last block added to the chain
            if self.latest_hash:
                block.prev_hash = self.latest_hash

            # assign the block to the blockchain and update latest_hash
            self.blocks[block.hash] = block
            self.latest_hash = block.hash

            # in a production blockchain, we would also broadcast the new block
            # to other nodes in the distributed system at this point

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

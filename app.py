from src.block import Block
from src.blockchain import Blockchain


if __name__ == '__main__':
    bc = Blockchain()

    block1 = Block('Data :)', None)
    block2 = Block('More data :)', block1.hash)

    bc.add_block(block1, block2, 1)

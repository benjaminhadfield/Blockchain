from src.block import Block
from src.blockchain import Blockchain


if __name__ == '__main__':
    bc = Blockchain()

    block1 = Block('Data :)')
    block2 = Block('More data :)')

    bc.add_blocks(block1, block2)

    block1.print_self()
    block2.print_self()

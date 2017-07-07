from src.block import Block
from src.blockchain import Blockchain


if __name__ == '__main__':
    block1 = Block('Data :)', None)
    block2 = Block('More data :)', block1.hash)

    bc = Blockchain()

    bc.add_block(block2)

    print(bc.__contains__(block1))

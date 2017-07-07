from src.block import Block


if __name__ == '__main__':
    block1 = Block('Data :)', None)
    block2 = Block('More data :)', block1.hash)

    block1.print_self()
    block2.print_self()

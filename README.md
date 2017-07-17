# Blockchain

**A simple implementation of a blockchain ⛓**

The blocks are signed by checking that the hash of the block starts with a specific sequence.
For example, we might state that blocks starting with `0000` are considered to be signed blocks.

> In production blocks should be signed using public/private key cryptography or similar.

In having a method to easily verify a block's validity, we can be confident that a given block has not be tampered with.

## Usage

Let's assume we defined a valid block to have a hash starting with the sequence `0000`.

```python
from src/block import Block
from src/blockchain import Blockchain

# Create a blockchain
blockchain = Blockchain()

# Create a couple of blocks containing data
b1 = Block({'from': 'Jas', 'to': 'Alex', 'amount': '100'})
b2 = Block('data data data')

# Add the blocks to the blockchain
blockchain.add_blocks(b1, b2)

print(b1.hash)      # 00007a8e7cf6e5b867967aa22f729823271d161f499b8d974f067844e1ad5754
print(b1.prev_hash) # None
print(b1.data)      # {'from': 'Amy', 'to': 'Parker', 'value': '100'}
print(b1.nonce)     # 16650
print(b1.is_valid)  # True

print(b2.hash)      # 000081217d9b741edcdffa31d9c7c62d3b1e175901905cedba4a68e5321a9037
print(b2.prev_hash) # 00007a8e7cf6e5b867967aa22f729823271d161f499b8d974f067844e1ad5754
print(b2.data)      # data data data
print(b2.nonce)     # 2044
print(b2.is_valid)  # True


# Change some data, invalidating the block
b1.data = 'New data 👾'
print(b1.is_valid)  # False


# We can mine a block to make it valid again
b1.mine()
print(b1.nonce)     # 8139
print(b1.is_valid)  # True

```

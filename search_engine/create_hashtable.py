# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.


def make_hashtable(nbuckets):
    hash_table = []
    for bucket in range(nbuckets):
        hash_table.append([])
    return hash_table

print make_hashtable(5)
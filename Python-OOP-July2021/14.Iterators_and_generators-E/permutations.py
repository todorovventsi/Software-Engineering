from itertools import permutations


def possible_permutations(collection):
    perms = permutations(collection)
    for permutation in perms:
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]

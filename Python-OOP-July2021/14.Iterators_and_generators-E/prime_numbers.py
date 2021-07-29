def is_prime(num):
    return num > 1 and not any([num % n == 0 for n in range(2, num)])


def get_primes(collection):
    primes = [num for num in collection if is_prime(num)]
    for prime in primes:
        yield prime


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

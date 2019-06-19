def naive_climb_stairs(n):
    if n < 0:
        return 0

    elif n == 0:
        return 1

    else:
        return naive_climb_stairs(n-1) + naive_climb_stairs(n-2) + naive_climb_stairs(n-3)


def memoized_climb_stairs(n, cache):
    if n < 0: return 0
    elif n == 0: return 1
    elif cache[n] > 1: return cache[n]
    else:
        cache[n] = memoized_climb_stairs(n - 1, cache) + \
                   memoized_climb_stairs(n - 2, cache) + \
                   memoized_climb_stairs(n - 3, cache)
        return cache[n]

print(naive_climb_stairs(10))
print(naive_climb_stairs(30))

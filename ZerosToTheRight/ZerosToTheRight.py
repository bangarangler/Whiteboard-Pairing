def zeros_to_right(arr):
    output = []
    n_zeros = 0

    for x in arr:
        if x == 0:
            n_zeros += 1
        else:
            output.append(x)

    for _ in range(n_zeros):
        output.append(0)

    return len(output) - n_zeros


print(zeros_to_right([0,2,0,4,0,6,7,8]))


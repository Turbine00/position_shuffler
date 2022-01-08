start_sequence = "635f"
shuffled = []


def shuffler(a, b):

    x = str(a)

    if len(str(a)) == 1:
        if (b+a) not in shuffled:
            shuffled.append(b + a)

    else:
        for i in range(len(x)):
            shuffler(x[:i] + x[i + 1:], b + x[i])


shuffler(start_sequence, "")
print(sorted(shuffled))

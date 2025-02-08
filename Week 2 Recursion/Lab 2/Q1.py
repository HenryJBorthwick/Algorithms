def sequence_length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + sequence_length(n/2)
    else:
        return 1 + sequence_length(3*n + 1)

print(sequence_length(22))
#print(sequence_length(1))
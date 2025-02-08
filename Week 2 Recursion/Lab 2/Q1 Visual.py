# import matplotlib.pyplot as plt

# def collatz_sequence(n):
#     sequence = [n]
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         sequence.append(n)
#     return sequence

# def visualize_collatz_sequence(n):
#     sequence = collatz_sequence(n)
#     plt.plot(range(len(sequence)), sequence)
#     plt.xlabel('Index')
#     plt.ylabel('Value')
#     plt.title(f'Collatz sequence of {n}')
#     plt.show()

# visualize_collatz_sequence(22)

def sequence_length(n):
    print(n, end=" ")
    if n == 1:
        print()
        return 1
    elif n % 2 == 0:
        return 1 + sequence_length(n // 2)
    else:
        return 1 + sequence_length(3 * n + 1)

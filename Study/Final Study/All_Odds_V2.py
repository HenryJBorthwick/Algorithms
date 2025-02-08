def all_odds(numbers):
    # Base case: if the list is empty, return True
    if not numbers:
        return True
    # Recursive case: check if the first number is odd and check next number in list
    else:
        return numbers[0] % 2 != 0 and all_odds(numbers[1:])

print(all_odds([3, 5, -7, 79]))
# True
print(all_odds([]))
# True
def all_odds(numbers):

    #Empty list
    if len(numbers) == 0:
        return True

    #If last number and is odd return true
    if len(numbers) == 1 and numbers[0] % 2 != 0:
        return True
    
    # Even end return false
    if numbers[0] % 2 == 0:
        return False
    
    # Odd check next number
    if numbers[0] % 2 != 0:
        return all_odds(numbers[1:])
    
    

print(all_odds([3, 5, -7, 79]))
# True
print(all_odds([]))
# True
def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate, input_data):
    """Returns True if the candidate is a complete solution."""
    # A candidate is a complete solution if its length is equal to the length of the input_data
    return len(candidate) == len(input_data)

def children(candidate, input_data):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    
    # Initialize an empty list to store child candidates
    child_candidates = []
    
    # Calculate the remaining elements in the input_data that are not part of the current candidate
    remaining_elements = input_data - set(candidate)
    
    # Loop through the remaining_elements
    for element in remaining_elements:
        # Create a new candidate by appending the current element to the existing candidate
        child_candidate = candidate + (element,)
        
        # Add the new candidate to the list of child candidates
        child_candidates.append(child_candidate)
    
    # Return the list of child candidates
    return child_candidates



#TEST
# print(sorted(permutations({1,2,3})))

#OUTPUT
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

#TEST:
# print(sorted(permutations({'a'})))

#OUTPUT:
# [('a',)]

#TEST:
# perms = permutations(set())
# print(len(perms) == 0 or list(perms) == [()])

#OUTPUT:
# True
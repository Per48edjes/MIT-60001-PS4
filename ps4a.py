# Problem Set 4A
# Name: Ravi Dayabhai 
# Collaborators: N/A
# Time Spent: ???

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Base case
    if len(sequence) == 1:
        return [sequence]

    # Recursive cases
    else:
        # Set up list to be returned
        perms = []
        last_letter = sequence[-1]
        sequence = sequence[:-1]
        prev_perm_list = get_permutations(sequence)
        
        # Insert 'last_letter' at each position for each permutation
        for p in prev_perm_list:
            for pos in range(0,len(p)+1):
                new_p = p[:pos] + last_letter + p[pos:]
                perms.append(new_p)

        return list(set(perms))

if __name__ == '__main__':
    
    # Example test case 1
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    # Example test case 2
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Output:', get_permutations(example_input))

    # Example test case 3
    example_input = 'abb'
    print('Input:', example_input)
    print('Expected Output:', ['abb', 'bab', 'bba'])
    print('Output:', get_permutations(example_input))

    # Example test case 4
    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['aaa'])
    print('Output:', get_permutations(example_input))
    
    # Example test case 5
    example_input = 'ravi'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))
    print(len(get_permutations(example_input)))

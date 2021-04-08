# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    if len(sequence) <= 1:
        # print([sequence])
        return [sequence]
    else:
        permutations = []
        first_char = sequence[0]
        next_chars = sequence[1:]
        permutations_of_subsequence = get_permutations(next_chars)
        for seq in permutations_of_subsequence:
            for index in range(len(seq) + 1):
                new_seq = seq[0:index] + first_char + seq[index:len(seq) + 1]
                permutations.append(new_seq)

        # print(permutations)
        return permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    print(get_permutations('ab'))
    print(get_permutations('abc'))
    print(get_permutations('bust'))
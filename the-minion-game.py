def count(letter_list, input_string):        
    index_list = []
    index = 0
    for s in input_string:
        if s in letter_list:
            index_list.append(index)
        index += 1
    input_string_len = len(input_string)
    points = sum([input_string_len-i for i in index_list])
    return points

def count_consonants(string):
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 
                  'K', 'L', 'M', 'N', 'P', 'Q', 'R',
                  'S', 'T', 'V', 'X', 'Z', 'W', 'Y']
    stuart_points = count(consonants, string)
    return ('Stuart', stuart_points)

def count_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin_points = count(vowels, string)
    return ('Kevin', kevin_points)


def minion_game(string):
    kevin = count_vowels(string)
    stuart = count_consonants(string)
    if kevin[1] > stuart[1]:
        print(kevin[0], kevin[1])
    elif kevin[1] < stuart[1]:
        print(stuart[0], stuart[1])
    else: 
        print('Draw')

if __name__ == '__main__':
    S = 'BANANA'
    minion_game(S)
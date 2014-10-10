def count_consonants(str):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                  'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
                  'v', 'w', 'x', 'z']
    count = 0
    for k in str:
        if k in consonants:
            count += 1
    return count

import string
def print_rangoli(n):
    # your code goes here
    alphabet = string.ascii_lowercase[:n]
    
    height = n * 2 - 1
    width = n * 4 - 3
    lines = [None] * height
    for i in range(n):
        sub_alphabet = alphabet[(-i - 1):]
        letters = ''.join(reversed(sub_alphabet)) + sub_alphabet[1:]
        lines[i] = lines[-i - 1] = '-'.join(letters).center(width, '-')
    
    print(*lines, sep='\n')
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
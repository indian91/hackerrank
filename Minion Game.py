def minion_game(S):
    # your code goes here
    n = len(S)

    # consonents
    stuart = 0

    # vowels
    kevin = 0

    for i in range(n):
        if S[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
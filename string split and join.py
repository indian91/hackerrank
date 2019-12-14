def split_and_join(line):
    a=line.split(" ")
    join="-".join(a)
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
def pascal_line(n):
    first_line = [1]
    return pascal_rec(first_line, n)


def pascal_rec(lst, n):
    if n == 0:
        return lst
    new_line = [1]
    for i in range(0, len(lst)-1):
        new_line.append(lst[i] + lst[i+1])
    new_line.append(1)
    return pascal_rec(new_line, n-1)


user_input = int(input('Enter n: '))
print(pascal_line(user_input))

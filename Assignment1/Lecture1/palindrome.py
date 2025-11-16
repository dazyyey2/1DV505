def check_palindrome(s):
    if s.strip() == '' or len(s) == 1:
        return True
    first = s[0]
    last = s[len(s)-1]
    s = s[1:-1]
    return is_palindrome(s, first, last)


def is_palindrome(s, first, last):
    if first == last:
        while len(s) > 0:
            first = s[0]
            last = s[len(s)-1]
            if first == last:
                s = s[1:-1]
            else:
                return False
    else:
        return False
    return True


user_input = str(input('Please enter a string: '))
if check_palindrome(user_input):
    print(f'{user_input} is a palindrome.')
else:
    print(f'{user_input} is not a palindrome.')

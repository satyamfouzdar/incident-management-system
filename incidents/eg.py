num = 55


def checkPalindrome(num):
    num_string = str(num)

    for digit in num_string:
        if not digit == num_string[-digit.index]:
            return False

    return True


checkPalindrome(num)

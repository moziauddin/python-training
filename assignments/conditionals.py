def str_len(str1):
    if isinstance(str1, int):  # You can also use type(str1) == int
        print('Integer is not supported')
    elif type(str1) == float:
        print('Floating point values are also not support at this stage')
    else:
        return len(str1)

str_len(233.5)

# ---------------------------------------------


def cel_to_far(cel):
    if cel < -273:
        print('Invalid value: please enter a value over -273')
    else:
        far = cel * 9 / 5 + 32
        return far

print(cel_to_far(-272))


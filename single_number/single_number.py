'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    doubles = {}
    for item in arr:
        if item in doubles:
            doubles[item] += 1
        else:
            doubles[item] = 1
    print(doubles)
    for key, value in doubles.items():
        if value == 1:
            return key
        else:
            "doesn't exist"


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

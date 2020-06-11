'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    count = 0

    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] == 0:
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if swap == False:
            count += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# def single_number(arr):
#     doubles = {}
#     for item in arr:
#         if item in doubles:
#             doubles[item] += 1
#         else:
#             doubles[item] = 1
#     # print(doubles)
#     for key, value in doubles.items():
#         if value == 1:
#             return key
#         else:
#             "doesn't exist"

def single_number(arr):
    # Your code here

    single = arr[0]
    # Do XOR of all elements and return
    print("single: ", single)
    for i in range(1, len(arr)):
        single ^= arr[i]  # exclusive OR， XOR
        # single = single ^ arr[i], if single is same as arr[i], return 0
        # 0 ^ b = b
        print("single: ", single, " arr", arr[i])
    return single


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

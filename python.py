# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


def mostFrequent(arr, int):
    my_dict = {}
    output = []

    for i in arr:
        my_dict[i] = my_dict.get(i, 0) + 1

    for key, val in my_dict.items():
        output.append((key, val))
    output.sort(key = lambda x : x[1], reverse=True)

    final_return = list(map(list, zip(*output)))
    return final_return[0][:int]

print(mostFrequent([1,1,1,1,1,2,2,2,2,2,2,3,3,3], 2))
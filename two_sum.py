from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        # {2: 0, 7: 1, 11: 2, 15: 3}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test case 1
    input_data = [2, 7, 11, 15]
    target = 9
    output = [0, 1]
    solution = Solution()
    assert output == solution.twoSum(input_data, target), "validation failed"

    # test case 2
    input_data = [3, 2, 4]
    target = 6
    output = [1, 2]
    assert output == solution.twoSum(input_data, target), "validation failed"

    # test case 3
    input_data = [3, 3]
    target = 6
    output = [0, 1]
    assert output == solution.twoSum(input_data, target), "validation failed"

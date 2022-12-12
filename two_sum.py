from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test case 1
    input_data = [2, 7, 11, 15]
    target = 9
    output = [0, 1]
    assert output == Solution.twoSum(input_data, target), "validation failed"

    # test case 2
    input_data = [3, 2, 4]
    target = 6
    output = [1, 2]
    assert output == Solution.twoSum(input_data, target), "validation failed"

    # test case 3
    input_data = [3, 3]
    target = 6
    output = [0, 1]
    assert output == Solution.twoSum(input_data, target), "validation failed"

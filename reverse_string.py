from typing import List

"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i: int = 0
        j: int = len(s) - 1
        while i < j:
            tmp: str = s[i]
            s[i] = s[j]
            s[j] = tmp
            i = i + 1
            j = j - 1

        return s


if __name__ == '__main__':
    # test case 1
    input_data = ["h","e","l","l","o"]
    output_data = ["o","l","l","e","h"]
    solution = Solution()
    assert output_data == solution.reverseString(input_data), "validation failed"

    # test case 2
    input_data = ["H","a","n","n","a","h"]
    output_data = ["h","a","n","n","a","H"]
    solution = Solution()
    assert output_data == solution.reverseString(input_data), "validation failed"

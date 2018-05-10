'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        遍历字符串, 用字典记录每个字符串出现的位置，若当前的字符在之前出现过，则更新左边start位置，
        并重新计算maxlen的值
        :type s: str
        :rtype: int
        """
        maxlen, start, res = 0, 0, {}
        for idx, val in enumerate(s, 1):
            if res.get(val, -1) >= start:
                start = res[val]
            res[val] = idx
            maxlen = max(maxlen, idx - start)
        return maxlen

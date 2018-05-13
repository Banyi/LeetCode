'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    def longestPalindrome1(self, s):
        """
        Manacher算法
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        s = '#' + '#'.join(s) + '#'
        idx , mx = 0, 0
        p = [0] * len(s)
        for i in range(len(s)):
            # 核心，如果右边界mx > i了，则 p[i] = min(p[2 * idx - i], mx - i),否则p[i] = 1
            p[i] = min(p[2 * idx - i], mx -i) if mx > i else 1
            # 尝试着扩展
            while i + p[i] < len(s) and i - p[i] > 0 and s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
                
            # 右边界
            mx = i + p[i]
            # 对称中心
            idx = i
        maxlen = max(p)
            
        return ''.join(s[p.index(maxlen) - maxlen + 1 : p.index(maxlen) + maxlen].split('#'))
    
    def longestPalindrome(self, s):
        """
        逆转字符串并找到与原串的最大子串，这个实现也是线性的O(N)
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        left, maxlen = 0, 1
        for i in range(len(s)):
            # 
            if i - maxlen >= 0 and s[i - maxlen: i+1] == s[i - maxlen: i+1][::-1]:
                left = i - maxlen
                maxlen += 1
                continue
            if i - maxlen >= 1 and s[i - maxlen - 1: i+1] == s[i - maxlen - 1: i+1][::-1]:
                left = i - maxlen - 1
                maxlen += 2
                
        return s[left: left + maxlen]

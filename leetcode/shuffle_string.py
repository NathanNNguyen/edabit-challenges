# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# Example 1:

# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.

class Solution:
    def restoreString(self, s, indices):
        # make a dict to store k, v as values from indices and s
        cache = {}
        for i in range(len(indices)):
            cache[indices[i]] = s[i]
        r = ''
        # use the sorted method on the dict keys to figure out the value for it
        for k in sorted(cache.keys()):
            r += cache[k]
        return r


s = 'codeleet'
indices = [4, 5, 6, 7, 0, 2, 1, 3]

print(Solution().restoreString(s, indices))

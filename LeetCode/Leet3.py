class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length

# JAVASCRIPT

# var lengthOfLongestSubstring = function(s) {
#     let left = 0;
#     let maxLength = 0;
#     let charSet = new Set();

#     for (let right = 0; right < s.length; right++) {
#         while (charSet.has(s[right])) {
#             charSet.delete(s[left]);
#             left++;
#         }

#         charSet.add(s[right]);
#         maxLength = Math.max(maxLength, right - left + 1);
#     }

#     return maxLength;    
# };

# JAVA

# class Solution {
#     public int lengthOfLongestSubstring(String s) {
#         int left = 0;
#         int maxLength = 0;
#         HashSet<Character> charSet = new HashSet<>();

#         for (int right = 0; right < s.length(); right++) {
#             while (charSet.contains(s.charAt(right))) {
#                 charSet.remove(s.charAt(left));
#                 left++;
#             }

#             charSet.add(s.charAt(right));
#             maxLength = Math.max(maxLength, right - left + 1);
#         }

#         return maxLength;       
#     }
# }
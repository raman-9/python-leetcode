# Find the Longest substring (print length)
class solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        start = 0
        end = 0
        max_len = 0 #store maximum length
        char_set = set()
        
        for start in range(len(s)):
            while s[start] in char_set():
                char_set.remove(s[end])
                end +=1
            max_len = max(max_len,start - end +1)
        return max_len
                
                
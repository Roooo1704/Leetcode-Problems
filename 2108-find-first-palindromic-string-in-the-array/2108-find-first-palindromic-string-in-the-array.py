class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        w=""
        for i in range(len(words)):
            a=words[i]
            if a==a[::-1]:
                w+=str(a)
                break
        return w
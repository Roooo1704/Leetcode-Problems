class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = "qwertyuiop"
        b = "asdfghjkl"
        c = "zxcvbnm"
        list1=[]
        for i in words:
            x=0
            y=0
            z=0
            for j in i:
                j = j.lower()
                if j in a:
                    x+=1
                elif j in b:
                    y+=1
                else:
                    z+=1
            if x == len(i) or y == len(i) or z == len(i):
                list1.append(i)    
        return list1
        
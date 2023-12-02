class Solution:
    def romanToInt(self, s: str) -> int:
        s+="*";c=0;i=0
        while i<len(s)-1:
            if s[i]=="I" and s[i+1]=="V":
                c+=4
                i+=2
            elif s[i]=="I" and s[i+1]=="X":
                c+=9
                i+=2
            elif s[i]=="X" and s[i+1]=="L":
                c+=40
                i+=2
            elif s[i]=="X" and s[i+1]=="C":
                c+=90
                i+=2
            elif s[i]=="C" and s[i+1]=="D":
                c+=400
                i+=2
            elif s[i]=="C" and s[i+1]=="M":
                c+=900
                i+=2
            elif s[i]=="I":
                c+=1
                i+=1
            elif s[i]=="V":
                c+=5
                i+=1
            elif s[i]=="X":
                c+=10 
                i+=1
            elif s[i]=="L":
                c+=50
                i+=1
            elif s[i]=="C":
                c+=100
                i+=1
            elif s[i]=="D":
                c+=500
                i+=1
            elif s[i]=="M":
                c+=1000
                i+=1
        return c

        
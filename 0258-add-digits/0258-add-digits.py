class Solution:
    def addDigits(self, num: int) -> int:
        # def add(num):
        #     s = 0
        #     for i in str(num):
        #         s += int(i)
        #     num = s
        #     return num
        # while num%10 != num:
        #     add(num)
        # return num
        if num%9 != 0 and num != 0:
            return num%9
        elif num == 0:
            return 0
        else:
            return 9
        
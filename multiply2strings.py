class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_arr = len(num1) if len(num1)>len(num2) else len(num2)
        num1_arr = [0]*len_arr
        num2_arr = [0]*len_arr
        if len(num1)>len(num2):
            num2 = str(num2).zfill(len_arr)
        else:
            num1 = str(num1).zfill(len_arr)
        
        i = 1
        while i<=len_arr:
            if not(num1[len_arr-i] is None):
                num1_arr[len_arr-i] = num1[len_arr-i]
            if not(num2[len_arr-i] is None):
                num2_arr[len_arr-i] = num2[len_arr-i]    
            i+=1
        
        res1 = int(''.join(str(i) for i in num1_arr))
        res2 = int(''.join(str(i) for i in num2_arr))
        return str(res1*res2)
            
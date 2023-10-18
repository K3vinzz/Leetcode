class Solution:
    def isHappy(self, n: int) -> bool:
        new_num = n
        occur_num_list = []
        while True:
            str_n = str(new_num)
            n_list = [int(num) for num in str_n]
            new_sum = 0
            for num in n_list:
                new_sum += num * num
            new_num = new_sum
            if new_num == 1:
                return True
            elif new_num in occur_num_list:
                return False
            occur_num_list.append(new_num)




sol = Solution()
print(sol.isHappy(n=45))


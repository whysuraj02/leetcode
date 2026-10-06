class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n
        freq = {}
        for i in range(1,n+1):
            digsum = 0
            temp = i
            while temp > 0:
                digsum += temp % 10
                temp  = temp // 10
            
            if digsum in freq:
                freq[digsum] += 1
            else:
                freq[digsum] = 1

            #using loop
            # st_i = str(i)
            # digsum = 0
            # for num in st_i:
            #     digsum += int(num)
            # if digsum in freq:
            #     freq[digsum] += 1
            # else:
            #     freq[digsum] = 1
        
        mf = 0
        count = 0
        for key in freq:
            if freq[key] > mf:
                mf = freq[key]
                count = 1
            elif freq[key] == mf:
                count += 1

        return count 




            




class Solution:
    def countSeniors(self, details: list[str]) -> int:
        if not details:
            return None
        count=0
        for i in details:
            if int(i[11:13])>60:
                # count+=1
                count+=1
        return count
sol=Solution()
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
a=sol.countSeniors(details)
print(a)
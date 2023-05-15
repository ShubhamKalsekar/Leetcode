class Solution:
    def average(self, salary: List[int]) -> float:
        a= max(salary)
        b=min(salary)
        x = []
        
        for i in range(len(salary)):
            if(a!=salary[i] and b!=salary[i]):
                x.append(salary[i]) 
        y = len(x) 
        
        return(sum(x)/y)

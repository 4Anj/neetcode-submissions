class Solution:
    def twoSum(self, n: List[int], tar: int) -> List[int]:
        seen={}
        for i in range(len(n)):
            diff=tar-n[i]
            if diff in seen:
                return [seen[diff],i+1]
            seen[n[i]]=i+1

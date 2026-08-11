class Solution:
    def isValid(self, s: str) -> bool:
        b={")":"(","}":"{","]":"["}
        st=[]
        for i in s:
            if i in b:
                t=st.pop() if st else None
                if b[i]!=t:
                    return False
            else:
                st.append(i)
        return len(st)==0
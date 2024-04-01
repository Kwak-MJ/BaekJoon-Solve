class Solution:
    def longestPalindrome(self, s: str) -> str:
        #문자열의 길이가 1이거나, 전체가 펠린드롬 문자열인 경우
        if len(s) < 1 or s == s[::-1]:
            return s

        # 이동하는 투포인터 만들기, n은 left와 right 사이의 간격
        # 단 n은 1보다 크거나 같고, len(s) - 1 보다 작거나 같다 
        def twopointer(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            

        result = ''
        for i in range(len(s)-1):
            result = max(result, twopointer(i,i+1),twopointer(i,i+2), key=len)
        return result
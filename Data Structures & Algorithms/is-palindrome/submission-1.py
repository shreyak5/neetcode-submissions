class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        is_alphanumeric = lambda c: (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')

        while i < j:
            if not is_alphanumeric(s[i]):
                i += 1
                continue
            if not is_alphanumeric(s[j]):
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

                    
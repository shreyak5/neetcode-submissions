class Solution:

    def encode(self, strs: List[str]) -> str:
        out = str(len(strs)) + ","
        str_concat = ""
        for s in strs:
            str_concat += s
            out += str(len(s)) + ","
        return out + str_concat

    def decode(self, s: str) -> List[str]:
        idx = 0
        # get the number of strings
        n = 0
        for i in range(idx, len(s)):
            char = s[i]
            if char == ",":
                idx = i + 1
                break
            n = 10*n + int(char)

        # get the length of each string
        str_lens = []
        curr_len = 0
        for i in range(idx, len(s)):
            char = s[i]
            if char == ",":
                str_lens.append(curr_len)
                curr_len = 0
                idx = i + 1
                n -= 1
                if n == 0:
                    break
            else:
                curr_len = 10*curr_len + int(char)

        # get each string
        out = []
        for l in str_lens:
            out.append(s[idx:idx+l])
            idx = idx + l
        
        return out





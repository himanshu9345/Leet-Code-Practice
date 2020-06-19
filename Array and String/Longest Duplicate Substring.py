class Solution(object):
    def findDuplicateOfLength(self, s, lenght1):
        hashPool = set()
        Prime = 101
        strLength = len(s)
        hashValue = self.calculateHash(s[:lenght1-1])
        j = 0
        for i in range(lenght1-1, strLength):
            hashValue += (ord(s[i]) - 96)*(Prime**(lenght1-1))
            hashValue = hashValue % self.q
            if hashValue in hashPool:
                return i - lenght1+1
            else:
                hashPool.add(hashValue)
            # print( j,i,"gg",lenght1)
            hashValue -=  ord(s[j]) - 96
            hashValue //= Prime
            j+=1
        return -1
    def findDuplicateOfLength2(self, s, lenght1):
        hashPool = set([])
        j = 0
        for i in range(len(s)-lenght1+1):
            str1 = s[i:i+lenght1]
            # print(str1,hashPool)
            if str1 in hashPool:
                return  i
            hashPool.add(str1)
        return -1
    def calculateHash(self, str1):
        Prime = 101
        hashval = 0
        for i, v in enumerate(str1):
            hashval += (ord(v) - 96)*(Prime**i)
        return  hashval

    def longestDupSubstring(self, S):
        n = len(S)
        l = 0
        r = len(S)
        # self.q = 2**63 - 1
        maxlen = 0
        maxindex = -1
        while l < r:
            mid = l + (r - l)//2
            if mid!=0:
                index = self.findDuplicateOfLength2(S, mid)
                # print (index,mid,l,r)
                
                if index == -1:
                    r = mid 
                else:
                    if mid > maxlen:
                        maxlen = mid
                        maxindex = index
                    l = mid + 1
            else:
                break
        # print (maxindex,maxlen)     
        return s[maxindex:maxindex+maxlen]
        """
        :type S: str
        :rtype: str
        """
sol = Solution()
s = "moplvidmaagmsiyyrkchbyhivlqwqsjcgtumqscmxrxrvwsnjjvygrelcbjgbpounhuyealllginkitfaiviraqcycjmskrozcdqylbuejrgfnquercvghppljmojfvylcxakyjxnampmakyjbqgwbyokaybcuklkaqzawageypfqhhasetugatdaxpvtevrigynxbqodiyioapgxqkndujeranxgebnpgsukybyowbxhgpkwjfdywfkpufcxzzqiuglkakibbkobonunnzwbjktykebfcbobxdflnyzngheatpcvnhdwkkhnlwnjdnrmjaevqopvinnzgacjkbhvsdsvuuwwhwesgtdzuctshytyfugdqswvxisyxcxoihfgzxnidnfadphwumtgdfmhjkaryjxvfquucltmuoosamjwqqzeleaiplwcbbxjxxvgsnonoivbnmiwbnijkzgoenohqncjqnckxbhpvreasdyvffrolobxzrmrbvwkpdbfvbwwyibydhndmpvqyfmqjwosclwxhgxmwjiksjvsnwupraojuatksjfqkvvfroqxsraskbdbgtppjrnzpfzabmcczlwynwomebvrihxugvjmtrkzdwuafozjcfqacenabmmxzcueyqwvbtslhjeiopgbrbvfbnpmvlnyexopoahgmwplwxnxqzhucdieyvbgtkfmdeocamzenecqlbhqmdfrvpsqyxvkkyfrbyolzvcpcbkdprttijkzcrgciidavsmrczbollxbkytqjwbiupvsorvkorfriajdtsowenhpmdtvamkoqacwwlkqfdzorjtepwlemunyrghwlvjgaxbzawmikfhtaniwviqiaeinbsqidetfsdbgsydkxgwoqyztaqmyeefaihmgrbxzyheoegawthcsyyrpyvnhysynoaikwtvmwathsomddhltxpeuxettpbeftmmyrqclnzwljlpxazrzzdosemwmthcvgwtxtinffopqxbufjwsvhqamxpydcnpekqhsovvqugqhbgweaiheeicmkdtxltkalexbeftuxvwnxmqqjeyourvbdfikqnzdipmmmiltjapovlhkpunxljeutwhenrxyfeufmzipqvergdkwptkilwzdxlydxbjoxjzxwcfmznfqgoaemrrxuwpfkftwejubxkgjlizljoynvidqwxnvhngqakmmehtvykbjwrrrjvwnrteeoxmtygiiygynedvfzwkvmffghuduspyyrnftyvsvjstfohwwyxhmlfmwguxxzgwdzwlnnltpjvnzswhmbzgdwzhvbgkiddhirgljbflgvyksxgnsvztcywpvutqryzdeerlildbzmtsgnebvsjetdnfgikrbsktbrdamfccvcptfaaklmcaqmglneebpdxkvcwwpndrjqnpqgbgihsfeotgggkdbvcdwfjanvafvxsvvhzyncwlmqqsmledzfnxxfyvcmhtjreykqlrfiqlsqzraqgtmocijejneeezqxbtomkwugapwesrinfiaxwxradnuvbyssqkznwwpsbgatlsxfhpcidfgzrc"
# s = "banana"
print(sol.longestDupSubstring(s))


class Solution(object):
    def findDuplicateOfLength2(self, s, lenght1):
        hashPool = set([])
        j = 0
        for i in range(len(s)-lenght1+1):
            str1 = s[i:i+lenght1]
            # print(str1,hashPool)
            if str1 in hashPool:
                return  i
            hashPool.add(str1)
        return -1
    def test(self, S, L):
        mod = 2**63 - 1
        p = pow(26, L, mod)
        cur = reduce(lambda x, y: (x * 26 + y) % mod, self.A[:L], 0)
        seen = {cur}
        for i in xrange(L, len(S)):
            cur = (cur * 26 + self.A[i] - self.A[i - L] * p) % mod
            if cur in seen: return i - L + 1
            seen.add(cur)
        return -1
    # def findDuplicateOfLength(self, s, lenght1):
    #     hashPool = set()
    #     Prime = 17
    #     strLength = len(s)
    #     hashValue = self.calculateHash(s[:lenght1-1])
    #     j = 0
    #     for i in range(lenght1-1, strLength):
    #         hashValue += (ord(s[i]) - 96)*(Prime**(lenght1-1))
    #         hashValue = hashValue % self.q
    #         if hashValue in hashPool:
    #             return i - lenght1+1
    #         else:
    #             hashPool.add(hashValue)
    #         # print( j,i,"gg",lenght1)
    #         hashValue -=  ord(s[j]) - 96
    #         hashValue //= Prime
    #         j+=1
    #     return -1
    # def calculateHash(self, str1):
    #     Prime = 17
    #     hashval = 0
    #     for i, v in enumerate(str1):
    #         hashval += (ord(v) - 96)*(Prime**i)
    #     return  hashval

    def longestDupSubstring(self, S):
        self.A = [ord(c) - ord('a') for c in S]

        n = len(S)
        l = 0
        r = len(S)
        maxlen = 0
        maxindex = -1
        self.q = 2**63 - 1

        while l < r:
            mid = l + (r - l)//2
            if mid!=0:
                index = self.test(S, mid)
                # print (index,mid,l,r)
                
                if index == -1:
                    r = mid 
                else:
                    if mid > maxlen:
                        maxlen = mid
                        maxindex = index
                    l = mid + 1
            else:
                break
        # print (maxindex,maxlen)     
        return S[maxindex:maxindex+maxlen]
        """
        :type S: str
        :rtype: str
        """
# sol = Solution()
# s = "abcd"
# print(sol.longestDupSubstring(s))
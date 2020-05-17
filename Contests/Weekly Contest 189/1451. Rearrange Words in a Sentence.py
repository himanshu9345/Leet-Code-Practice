class Solution:
    def arrangeWords(self, text: str) -> str:
        ans = sorted(text.lower().split(" "), key = lambda s : len(s))
        ans[0] = ans[0].capitalize()
        return " ".join(ans)
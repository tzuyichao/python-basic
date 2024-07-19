class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - bulls
        return f"{bulls}A{cows}B"

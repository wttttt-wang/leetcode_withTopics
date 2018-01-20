"""
Bulls and Cows
@ Hash
"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, occurs, cow = 0, {}, 0
        for i in range(len(secret)):
            if i < len(guess) and secret[i] == guess[i]:
                bull += 1
            else:
                occurs[secret[i]] = occurs.get(secret[i], 0) + 1
        for i in range(len(guess)):
            if i < len(secret) and guess[i] == secret[i]:
                continue
            if guess[i] in occurs:
                cow += 1
                occurs[guess[i]] -= 1
                if not occurs[guess[i]]:
                    occurs.pop(guess[i])
        return "{}A{}B".format(bull, cow)

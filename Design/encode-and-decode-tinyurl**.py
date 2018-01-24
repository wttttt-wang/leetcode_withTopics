"""
Encode and Decode TinyURL
@ Design + Hash: Please refer to 'Design/design-tinyurl.md' for detailed explanation.
"""


class Codec:
    def __init__(self):
        self.id = 0
        self.alphas = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.l2s, self.s2l = {}, {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.l2s:
            ind = self.id
            self.id += 1
            short = self.map62(ind)
            self.l2s[longUrl] = "http://tinyurl.com/" + short
            self.s2l[short] = longUrl
        return self.l2s[longUrl]

    def map62(self, num):
        res = []
        while num > 0:
            res.append(self.alphas[num % 62])
            num /= 62
        # Attention: need to add leading zeros if need(len < 6)
        while len(res) < 6:
            res.insert(0, '0')
        return "".join(res)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        short = shortUrl.rsplit('/', 1)[1]
        return self.s2l.get(short, '')

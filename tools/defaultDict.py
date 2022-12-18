# https://docs.python.org/3/library/collections.html
from collections import defaultdict

class Solution:
    def distanceK(self, root, target, k):
        adj = defaultdict(list)

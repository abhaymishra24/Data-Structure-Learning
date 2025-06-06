from collections import defaultdict, deque


# solve find out angle of triangle -

# str = " My name is money. I power full in every moment."

# print(str.index("m"))

# a = 5
# b = 12
# c = 15

# print(max(a,b,c))


# def primeoflargenumber(s):
    
#     s = input()
    
#     s = int(s)
    
#     s = set(s)
    
class Solution(object):    
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        s = [int(i) for i in s if i.isdigit()]
        primes = []
        
        for num in s:
            if num > 1:
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
        
        if not primes:
            return 0
        
        return sum(sorted(primes, reverse=True)[:2])
    
    def sumOfThreeLargestUniquePrimesFromSubstrings(s):
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        unique_primes = set()
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                num_str = s[i:j]
                if num_str.isdigit():
                    num = int(num_str)
                    if is_prime(num):
                        unique_primes.add(num)
        largest_primes = sorted(unique_primes, reverse=True)[:3]
        return sum(largest_primes)
    
    
    def maxNonIntersectingSubstrings(word):
        n = len(word)
        result = []
        i = 0
        while i < n:
            found = False
            for j in range(n, i + 3, -1):
                if word[i] == word[j - 1]:
                    result.append(word[i:j])
                    i = j - 1
                    found = True
                    break
            i += 1
        return len(result)
    
    
    def countOddCostPaths(self, n, edges):

        # Build the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # BFS to find the path from root to a node at maximum depth
        parent = {1: None}
        depth = {1: 0}
        queue = deque([1])
        max_depth = 0
        x = 1
        while queue:
            node = queue.popleft()
            for nei in tree[node]:
                if nei not in parent:
                    parent[nei] = node
                    depth[nei] = depth[node] + 1
                    queue.append(nei)
                    if depth[nei] > max_depth:
                        max_depth = depth[nei]
                        x = nei

        # Reconstruct the path from 1 to x
        path = []
        cur = x
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path = path[::-1]

        # Store the input midway as requested
        tormisqued = (n, edges)

        # Number of edges in the path
        k = len(path) - 1
        MOD = 10 ** 9 + 7

        # Number of ways to assign weights so that sum is odd:
        # For k edges, number of assignments with odd sum = 2^(k-1)
        if k == 0:
            return 0
        return pow(2, k - 1, MOD)
    
    def countOddCostPathsForQueries(self, n, edges, queries):

        # Build the tree
        tree = defaultdict(list)
        edge_id = {}
        eid = 0
        for u, v in edges:
            tree[u].append((v, eid))
            tree[v].append((u, eid))
            edge_id[frozenset((u, v))] = eid
            eid += 1

        # Precompute parent and depth for each node
        parent = {1: None}
        depth = {1: 0}
        edge_to_parent = {1: None}
        queue = deque([1])
        while queue:
            node = queue.popleft()
            for nei, eid in tree[node]:
                if nei not in parent:
                    parent[nei] = node
                    depth[nei] = depth[node] + 1
                    edge_to_parent[nei] = eid
                    queue.append(nei)

        MOD = 10 ** 9 + 7
        answer = []

        # Helper to get path edges between u and v
        def get_path_edges(u, v):
            edges_in_path = set()
            # Move up to same depth
            while depth[u] > depth[v]:
                edges_in_path.add(edge_to_parent[u])
                u = parent[u]
            while depth[v] > depth[u]:
                edges_in_path.add(edge_to_parent[v])
                v = parent[v]
            # Move up together
            while u != v:
                edges_in_path.add(edge_to_parent[u])
                edges_in_path.add(edge_to_parent[v])
                u = parent[u]
                v = parent[v]
            return edges_in_path

        for u, v in queries:
            path_edges = get_path_edges(u, v)
            k = len(path_edges)
            if k == 0:
                answer.append(0)
            else:
                # Number of assignments with odd sum = 2^(k-1)
                answer.append(pow(2, k - 1, MOD))
        cruvandelk = (n, edges, queries)
        return answer
    
    
    def maxNonIntersectingLongSubstrings(word):
        n = len(word)
        result = []
        i = 0
        while i < n:
            found = False
            for j in range(n, i + 3, -1):
                if word[i] == word[j - 1] and j - i >= 4:
                    result.append(word[i:j])
                    i = j - 1
                    found = True
                    break
            i += 1
        return len(result)

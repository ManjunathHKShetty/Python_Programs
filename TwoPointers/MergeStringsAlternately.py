class solution:
    def mergeAlternately(self, word1, word2):
        i, j = 0, 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)

X = solution()
result_1 = X.mergeAlternately("abc","pqr")
print(result_1)

result_2 = X.mergeAlternately("ab","pqrs")
print(result_2)

result_2 = X.mergeAlternately("abcd","pq")
print(result_2)
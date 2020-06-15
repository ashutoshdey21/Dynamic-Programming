class LongestCommonSubsequence:
    def __init__(self, text1, text2):
        self.lcs = [[None for x in range(len(text2) + 1)] for y in range(len(text1) + 1)]
        for x in range(len(text1) + 1):
            self.lcs[x][0] = 0
        for y in range(len(text2) + 1):
            self.lcs[0][y] = 0
        # print(self.lcs)
        self.text1 = text1
        self.text2 = text2

    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        # print(lcs[len(text1)-1][len(text2)])
        i = len(text1)
        j = len(text2)
        # print('i=', i, 'j=', j)
        # print(self.lcs[i][j])
        result = self.get_sequence_length(i, j)
        # for i, j in enumerate(self.lcs):
        #     print(i, j)

        return result

    def get_sequence_length(self, i, j):
        # print(self.text2, self.text1)
        # print(i, j)

        # if i == -1 or j == -1:
        #     return 0
        if self.lcs[i][j] is not None:
            return self.lcs[i][j]
        elif self.text1[i - 1] == self.text2[j - 1]:
            self.lcs[i][j] = 1 + self.get_sequence_length(i - 1, j - 1)
        else:
            self.lcs[i][j] = max(self.get_sequence_length(i, j - 1), self.get_sequence_length(i - 1, j))

        return self.lcs[i][j]


def main():
    a = 'abc'
    b = 'abbbcccabc'

    obj = LongestCommonSubsequence(a, b)
    count = obj.longest_common_subsequence(a, b)
    print('length of the LCS=', count)

    # print(obj.lcs)


if __name__ == '__main__':
    main()

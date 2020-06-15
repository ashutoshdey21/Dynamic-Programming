# Created By: @ashutosh.dey21
def print_matrix(length_matrix):
    for index, row in enumerate(length_matrix):
        print(row)


class Solution(object):

    def longest_palindromic_subsequence(self, s: str) -> str:
        length_matrix = [[0 for x in range(len(s))] for y in range(len(s))]

        for x in range(len(s)):
            length_matrix[x][x] = 1
        i, j = 0, 0
        for each_length in range(2, len(s) + 1):
            # print("length=", each_length)
            for i in range(0, (len(s) - each_length) + 1):
                j = i + each_length - 1
                # print(i, j)
                if s[i] == s[j] and each_length == 2:
                    length_matrix[i][j] = 2
                elif s[i] == s[j]:
                    length_matrix[i][j] = 2 + length_matrix[i + 1][j - 1]
                else:
                    length_matrix[i][j] = max(length_matrix[i + 1][j], length_matrix[i][j - 1])
                # print_matrix(length_matrix)

        # print(length_matrix[i][j])

        print_matrix(length_matrix)
        print("length=", length_matrix[i][j])
        # subsequence_length = length_matrix[i][j]
        result = [None for x in range(len(s) + 1)]
        end_i, end_j = i, j
        # print("start:", end_j, end_i)
        string_i, string_j = s, s
        while end_i < len(s) and end_j > 1:
            # print(end_j, end_i)
            # print(result)
            if string_i[end_i] == string_j[end_j]:
                result[end_i] = string_i[end_i]
                result[end_j] = string_j[end_j]
                end_i += 1
                end_j -= 1
                # subsequence_length -= 2
            elif length_matrix[end_i + 1][end_j] > length_matrix[end_i][end_j - 1]:
                end_i += 1
            else:
                end_j -= 1

        palindrome = ""
        for each in result:
            if each is not None:
                palindrome += each
        return palindrome


def main():
    string = "aa"
    obj = Solution()
    result = obj.longest_palindromic_subsequence(string)
    print("longest_palindromic_subsequence=", result)


if __name__ == '__main__':
    main()

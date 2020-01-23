# Created By: @ashutosh.dey21
import sys


def print_matrix(length_matrix):
    for index, row in enumerate(length_matrix):
        print(row)


class LongestPalindromicSubstring(object):
    def longest_palindromic_substring(self, s: str) -> str:
        length_matrix = [[False for x in range(len(s))] for y in range(len(s))]
        max_substring = sys.maxsize * -1
        end_i, end_j = 0, 0

        for i in range(len(s)):
            length_matrix[i][i] = True
            for j in range(i):
                # print(i, j)
                if s[i] == s[j]:
                    if i - j + 1 <= 2 or length_matrix[j + 1][i - 1] is True:
                        length_matrix[j][i] = True
                        if i - j + 1 > max_substring:
                            max_substring = i - j + 1
                            end_i = i
                            end_j = j
        print_matrix(length_matrix)
        # print(end_i, end_j)
        return s[end_j:end_i + 1]


def main():
    input_string = "abcda"
    obj = LongestPalindromicSubstring()
    result = obj.longest_palindromic_substring(input_string)
    print(result)


if __name__ == '__main__':
    main()

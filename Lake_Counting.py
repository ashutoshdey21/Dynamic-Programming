def traverse_map(self, visited, column, row):
    # print(row, column)
    visited[column][row] = True
    for x_modifier in range(-1, 2):
        for y_modifier in range(-1, 2):
            current_column = column + x_modifier
            current_row = row + y_modifier
            if 0 <= current_column < self.column_count:
                if 0 <= current_row < self.row_count:
                    if not visited[current_column][current_row]:
                        if self.campus_map[current_column][current_row] == '#':
                            # return 1 + traverse_map(self, visited, current_column, current_row)
                            traverse_map(self, visited, current_column, current_row)
                            # return 1


class LakeCounting:
    def __init__(self, campus_map):
        # map_2d = []
        # visited = [[False for x in range(n)] for y in range(n)]

        self.campus_map = campus_map
        # print(campus_map[1][1])

        # self.map_2d = map_2d
        for index, row in enumerate(self.campus_map):
            # row=[row]
            # print(index)
            # map_2d.append([row])
            # print(len(row))
            self.row_count = len(row)
            break

        self.column_count = len(self.campus_map)

    def count_the_lakes(self):

        # print(column_count)
        # print(row_count)

        result = 0
        visited = [[False for x in range(self.row_count)] for y in range(self.column_count)]
        for row in range(self.row_count):
            for column in range(self.column_count):
                # print(row, column)
                # print(visited)
                # print(self.campus_map[column][row])
                if visited[column][row] is False and self.campus_map[column][row] == '#':
                    # result += traverse_map(self, visited, column, row)
                    traverse_map(self, visited, column, row)
                    result += 1

        # print(result)
        return result


def main():
    obj = LakeCounting(["#---------#",
                        "-#-------#-",
                        "--#-----#--",
                        "---#---#---",
                        "----#-#----",
                        "-----------",
                        "----#-#----",
                        "---#---#---",
                        "--#-----#--",
                        "-#-------#-",
                        "#---------#"])
    result = obj.count_the_lakes()
    print('The number of ponds:', result)


if __name__ == '__main__':
    main()

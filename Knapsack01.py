class Knapsack01:
    def __init__(self, weight_sack, items):
        self.items = items
        self.weight_sack = weight_sack
        benefit_matrix = [[None for i in range(len(items) + 1)] for j in range(weight_sack + 1)]
        for w in range(weight_sack + 1):
            benefit_matrix[w][0] = 0
        for i in range(len(items) + 1):
            benefit_matrix[0][i] = 0
        self.benefit_matrix = benefit_matrix
        print(benefit_matrix)
        print('benefit matrix initialized')

    def get_max_benefit(self):
        print('Items for the sack')
        print(self.items)
        for item_index in range(1, len(self.items) + 1):
            for weight in range(1, self.weight_sack + 1):
                # print('item_index=', item_index, 'w=', w)
                # items[item_index-1][x] x=0 for weight and x=1 for benefit
                # print(self.items[item_index - 1][1])
                current_item_weight = self.items[item_index - 1][0]
                current_item_benefit = self.items[item_index - 1][1]
                previous_item_index = item_index - 1
                if current_item_weight <= weight:
                    # print(current_item_benefit)
                    if current_item_benefit + self.benefit_matrix[weight - current_item_weight][previous_item_index] > \
                            self.benefit_matrix[weight][previous_item_index]:
                        self.benefit_matrix[weight][item_index] = current_item_benefit + \
                                                                  self.benefit_matrix[weight - current_item_weight][
                                                                      previous_item_index]
                    else:
                        self.benefit_matrix[weight][item_index] = self.benefit_matrix[weight][previous_item_index]
                else:
                    self.benefit_matrix[weight][item_index] = self.benefit_matrix[weight][previous_item_index]

        print('Benefit matrix for the resulting items in the sack.')
        for weight in range(self.weight_sack + 1):
            print(self.benefit_matrix[weight])
        return self.benefit_matrix[weight][item_index]


def main():
    sack = Knapsack01(6, [(1, 3),
                          (2, 4),
                          (3, 5),
                          (4, 8)])
    print('The max benefit will be:')
    print(sack.get_max_benefit())


if __name__ == '__main__':
    main()

import sys


def backpack(w_backpack, items_list):
    total = 0
    cost_list = list()
    for item in items_list:
        cost_list.append(item[0] / item[1])
    while w_backpack > 0 and len(cost_list) > 0:
        max_value = max(cost_list)
        max_index = cost_list.index(max_value)
        if w_backpack < items_list[max_index][1]:
            total += w_backpack * cost_list[max_index]
            w_backpack = 0
            cost_list.pop(max_index)
            items_list.pop(max_index)
        else:
            w_backpack -= items_list[max_index][1]
            total += items_list[max_index][0]
            cost_list.pop(max_index)
            items_list.pop(max_index)
    return '{:.3f}'.format(total)


def main():
    user_input = sys.stdin.readlines()
    weight = int(user_input[0].split()[1])
    user_input.pop(0)
    items = list()
    for string in user_input:
        items.append(list(map(int, string.split())))
    print(backpack(weight, items))


main()

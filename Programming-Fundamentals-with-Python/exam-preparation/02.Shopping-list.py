shopping_list = input().split("!")

command = input()

while "Go Shopping!" not in command:
    if "Correct" not in command:
        action, item = command.split()
        item_in_list = True
        if item not in shopping_list:
            item_in_list = False
        if action == "Urgent" and not item_in_list:
            shopping_list.insert(0, item)
        elif action == "Unnecessary" and item_in_list:
            shopping_list.remove(item)
        elif action == "Rearrange" and item_in_list:
            shopping_list.remove(item)
            shopping_list.append(item)
    else:
        action, old_item, new_item = command.split()
        if old_item in shopping_list:
            shopping_list[shopping_list.index(old_item)] = new_item

    command = input()


print(*shopping_list, sep=", ")

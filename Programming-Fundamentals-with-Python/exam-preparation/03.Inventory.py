item_list = input().split(", ")

command = input()

while "Craft!" not in command:
    action, item = command.split(" - ")
    item_in_list = True
    if item not in item_list:
        item_in_list = False

    if action == "Collect" and not item_in_list:
        item_list.append(item)
    elif action == "Drop" and item_in_list:
        item_list.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item not in item_list:
            continue
        item_list.insert(item_list.index(old_item) + 1, new_item)
    elif action == "Renew" and item_in_list:
        item_list.remove(item)
        item_list.append(item)

    command = input()

print(*item_list, sep=", ")

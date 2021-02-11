note = input()
to_do_list = [0] * 10

while not note == "End":
    note_importance, note_text = note.split("-")
    note_importance = int(note_importance) - 1
    to_do_list[note_importance] = note_text
    note = input()

to_do_sorted = [task for task in to_do_list if not task == 0]
print(to_do_sorted)

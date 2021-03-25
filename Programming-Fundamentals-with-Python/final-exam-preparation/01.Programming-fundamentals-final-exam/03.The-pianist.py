def add_piece(new, new_composer, new_key, origin):
    if new in origin:
        print(f"{new} is already in the collection!")
        return origin
    origin[new] = {"composer": new_composer, "key": new_key}
    print(f"{new} by {new_composer} in {new_key} added to the collection!")
    return origin


def remove_piece(to_remove, origin):
    if to_remove not in origin:
        print(f"Invalid operation! {to_remove} does not exist in the collection.")
        return origin
    origin.pop(to_remove)
    print(f"Successfully removed {to_remove}!")
    return origin


def change_key(c_piece, new_key, origin):
    if c_piece not in origin:
        print(f"Invalid operation! {c_piece} does not exist in the collection.")
        return origin
    origin[c_piece]["key"] = new_key
    print(f"Changed the key of {c_piece} to {new_key}!")
    return origin


number_of_pieces = int(input())
pieces_register = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    if piece not in pieces_register:
        pieces_register[piece] = {"composer": '', "key": ''}
    pieces_register[piece] = {"composer": composer, "key": key}

command = input()
while not command == "Stop":
    data = command.split("|")
    if "Add" in data:
        piece_to_add, piece_composer, piece_key = data[1:]
        # piece_to_add = data[1]
        # piece_composer = data[2]
        # piece_key = data[3]
        pieces_register = add_piece(piece_to_add, piece_composer, piece_key, pieces_register)
    elif "Remove" in data:
        piece_to_remove = data[1]
        pieces_register = remove_piece(piece_to_remove, pieces_register)
    elif "ChangeKey" in data:
        piece_to_change = data[1]
        key_to_change = data[2]
        pieces_register = change_key(piece_to_change, key_to_change, pieces_register)

    command = input()

sorted_register = sorted(pieces_register.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"]))

for piece in sorted_register:
    piece_name = piece[0]
    composer = piece[1]["composer"]
    key = piece[1]["key"]
    print(f"{piece_name} -> Composer: {composer}, Key: {key}")

cards = input()
shuffle_times = int(input())

cards_listed = cards.split(" ")

for _ in range(shuffle_times):
    current_deck_state = []
    even_count = 0
    for index in range(len(cards_listed)):
        if index % 2 == 0:
            current_deck_state.append(cards_listed[int(index / 2)])
        else:
            current_deck_state.append(cards_listed[int(len(cards_listed) / 2 + even_count)])
            even_count += 1
    cards_listed = current_deck_state
print(cards_listed)

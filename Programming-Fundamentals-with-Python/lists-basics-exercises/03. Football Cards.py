given_cards = input()

given_cards_listed = given_cards.split(" ")
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
isTerminated = False

if given_cards:
    for card in given_cards_listed:
        card_listed = card.split("-")
        if not int(card_listed[1]) in team_a or not int(card_listed[1]) in team_b:
            continue
        if card_listed[0] == "A":
            team_a.remove(int(card_listed[1]))
        elif card_listed[0] == "B":
            team_b.remove(int(card_listed[1]))
        if len(team_a) < 7 or len(team_b) < 7:
            isTerminated = True
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if isTerminated:
    print("Game was terminated")

n = int(input())
heroes = {}
max_hp = 100
max_mp = 200

for _ in range(n):
    hero_name, hit_points, mana_points = input().split()
    hit_points = int(hit_points)
    mana_points = int(mana_points)
    heroes[hero_name] = {'hit_points': hit_points, 'mana_points': mana_points}

data = input()

while data != "End":
    command = data.split(" - ")
    if command[0] == "CastSpell":
        hero_name = command[1]
        mana_points = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]['mana_points'] >= mana_points:  # Should be mana_points, not max_mp
            heroes[hero_name]['mana_points'] -= mana_points
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana_points']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name]['hit_points'] -= damage
        if heroes[hero_name]['hit_points'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit_points']} HP left!")
        # Missing print:
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        initial_mp = heroes[hero_name]['mana_points']
        if heroes[hero_name]['mana_points'] + amount <= max_mp:  # Should be <=
            heroes[hero_name]['mana_points'] += amount
        # Missing case
        else:
            heroes[hero_name]['mana_points'] = max_mp
        diff = abs(initial_mp - heroes[hero_name]['mana_points'])
        print(f"{hero_name} recharged for {diff} MP!")
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        initial_hp = heroes[hero_name]['hit_points']
        if heroes[hero_name]['hit_points'] + amount <= max_hp:  # Should be <=
            heroes[hero_name]['hit_points'] += amount
        else:
            heroes[hero_name]['hit_points'] = max_hp
        diff = abs(initial_hp - heroes[hero_name]['hit_points'])
        print(f"{hero_name} healed for {diff} HP!")
    data = input()

sorted_heroes = sorted(heroes.items(), key=lambda tkvp: (-tkvp[1]["hit_points"], tkvp[0]))

for key, value in sorted_heroes:
    print(key)
    print(f"  HP: {value['hit_points']}\n  MP: {value['mana_points']}")

def cast_spell(hero, mana, spell, heroes_dict):
    if heroes_dict[hero]["mp"] >= mana:
        heroes_dict[hero]["mp"] -= mana
        print(f"{hero} has successfully cast {spell} and now has {heroes_dict[hero]['mp']} MP!")
        return
    print(f"{hero} does not have enough MP to cast {spell}!")
    return


def take_damage(hero, dmg, attacking_hero, heroes_dict):
    heroes_dict[hero]["hp"] -= dmg
    if heroes_dict[hero]["hp"] <= 0:
        heroes_dict.pop(hero)
        print(f"{hero} has been killed by {attacking_hero}!")
        return
    print(f"{hero} was hit for {damage} HP by {attacking_hero} and now has {heroes_dict[hero]['hp']} HP left!")
    return


def recharge(hero, value, heroes_dict):
    starting_mp = heroes_dict[hero]["mp"]
    if heroes_dict[hero]["mp"] + value <= 200:
        heroes_dict[hero]["mp"] += value
    else:
        heroes_dict[hero]["mp"] = 200
    diff = heroes_dict[hero]["mp"] - starting_mp
    print(f"{hero} recharged for {diff} MP!")
    return


def heal(hero, value, heroes_dict):
    starting_hp = heroes_dict[hero]["hp"]
    if heroes_dict[hero]["hp"] + value <= 100:
        heroes_dict[hero]["hp"] += value
    else:
        heroes_dict[hero]["hp"] = 100
    diff = heroes_dict[hero]["hp"] - starting_hp
    print(f"{hero} healed for {diff} HP!")
    return


number_of_heroes = int(input())

heroes = {}

for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    hero_hp = int(hp)
    hero_mp = int(mp)
    heroes[hero_name] = {"hp": 0, "mp": 0}
    if hero_hp > 100:
        heroes[hero_name]["hp"] = 100
    else:
        heroes[hero_name]["hp"] = hero_hp
    if hero_mp > 200:
        heroes[hero_name]["mp"] = 200
    else:
        heroes[hero_name]["mp"] = hero_mp

command = input()
while not command == "End":
    data = command.split(" - ")
    hero_name = data[1]
    if "CastSpell" in data:
        needed_mp = int(data[2])
        spell_name = data[3]
        cast_spell(hero_name, needed_mp, spell_name, heroes)
    elif "TakeDamage" in data:
        damage = int(data[2])
        attacker = data[3]
        take_damage(hero_name, damage, attacker, heroes)
    elif "Recharge" in data:
        re_charge_amount = int(data[2])
        recharge(hero_name, re_charge_amount, heroes)
    elif "Heal" in data:
        heal_amount = int(data[2])
        heal(hero_name, heal_amount, heroes)

    command = input()

heroes = sorted(heroes.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0]))
for name, stat in heroes:
    print(name)
    print(f"  HP: {stat['hp']}")
    print(f"  MP: {stat['mp']}")

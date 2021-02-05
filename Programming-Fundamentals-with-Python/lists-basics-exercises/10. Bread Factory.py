# Inputs:
events = input().split("|")

# Initial stats:
energy = 100
coins = 100
day_completed = True

# Event looping:
for event in events:
    current_event = event.split("-")
    event_value = int(current_event[-1])

    #Event computing:
    if "rest" in current_event:
        if not event_value + energy <= 100:
            print(f"You gained 0 energy.")
        else:
            energy += event_value
            print(f"You gained {event_value} energy.")
        print(f"Current energy: {energy}.")

    elif "order" in current_event:
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        energy -= 30
        coins += event_value
        print(f"You earned {event_value} coins.")

    else:
        if coins <= event_value:
            print(f"Closed! Cannot afford {current_event[0]}.")
            day_completed = False
            break
        coins -= event_value
        print(f"You bought {current_event[0]}.")

if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

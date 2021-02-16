n_rooms = int(input())

there_are_free_chairs = True
free_chairs = 0

for room in range(1, n_rooms + 1):
    chairs, people = input().split(" ")
    difference = abs(len(chairs) - int(people))
    if int(people) > len(chairs):
        print(f"{difference} more chairs needed in room {room}")
        there_are_free_chairs = False
    else:
        free_chairs += difference

if there_are_free_chairs:
    print(f"Game On, {free_chairs} free chairs left")

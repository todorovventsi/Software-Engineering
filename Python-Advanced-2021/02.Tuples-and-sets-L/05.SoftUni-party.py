number_of_invitations = int(input())

vip_numbers = set()
regular_numbers = set()

for _ in range(number_of_invitations):
    registration = input()
    if registration[0].isdigit():
        vip_numbers.add(registration)
        continue
    regular_numbers.add(registration)

next_guest = input()
while not next_guest == "END":
    if next_guest[0].isdigit():
        vip_numbers.discard(next_guest)
        next_guest = input()
        continue
    regular_numbers.discard(next_guest)
    next_guest = input()

guests_missing = vip_numbers.union(regular_numbers)
print(f"{len(guests_missing)}")
[print(guest) for guest in sorted(vip_numbers)]
[print(guest) for guest in sorted(regular_numbers)]

days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

gained = 0

for day in range(1, days_of_plunder + 1):
    gained += daily_plunder
    if day % 3 == 0:
        gained += daily_plunder * 0.5
    if day % 5 == 0:
        gained -= gained * 0.3
if gained >= expected_plunder:
    print(f"Ahoy! {gained:.2f} plunder gained.")
else:
    print(f"Collected only {gained / expected_plunder * 100:.2f}% of the plunder.")

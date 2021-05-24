from collections import deque

costumer = input()
market_queue = deque()

while not costumer == "End":
    if costumer == "Paid":
        for client in range(len(market_queue)):
            print(market_queue.popleft())
    else:
        market_queue.append(costumer)
    costumer = input()
print(f"{len(market_queue)} people remaining.")

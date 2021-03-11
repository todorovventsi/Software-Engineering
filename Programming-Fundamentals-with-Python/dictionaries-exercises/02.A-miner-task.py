command = input()
counter = 1
resources = {}
last_res = command

while not command == "stop":
    if not counter % 2 == 0:  # when counter is odd
        if command not in resources:
            resources[command] = 0
        last_res = command
    else:
        resources[last_res] += int(command)

    counter += 1
    command = input()

for resource, value in resources.items():
    print(f"{resource} -> {value}")

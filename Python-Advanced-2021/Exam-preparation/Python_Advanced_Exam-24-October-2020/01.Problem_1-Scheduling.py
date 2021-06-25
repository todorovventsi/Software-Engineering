tasks = [int(i) for i in input().split(', ')]
task_index = int(input())

fastest_task = min(tasks)
target_task = tasks[task_index]
completed_cycles = target_task

if tasks.count(target_task) > 1:
    for index in range(0, len(tasks)):
        if tasks[index] == target_task and index < task_index:
            completed_cycles += tasks[index]

for task in tasks:
    if task < target_task:
        completed_cycles += task

print(completed_cycles)

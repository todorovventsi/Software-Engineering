# numbers = [int(i) for i in input().split()] # [1, 2, 3, 4, 5, 6, 7]
# k = int(input())
# length = len(numbers)
# result = []
# last_removed = -1
# while numbers:
#     to_remove = last_removed + k
ls = [int(i) for i in input().split()]
skip = int(input()) - 1
dead_list = []
idx = skip
while len(ls) > 1:
    dead_list.append(ls[idx])
    ls.pop(idx)  # kill prisoner at idx
    idx = (idx + skip) % len(ls)

dead_list.append(ls[0])
dead_list_str = list(map(str, dead_list))
string = ",".join(dead_list_str)

print(f"[{string}]")

ranges_number = int(input())

longest_intersection = set()

for _ in range(ranges_number):
    # read the ranges and stores them into sets:
    first_range, second_range = input().split("-")
    first_range = first_range.split(",")
    second_range = second_range.split(",")
    first_set = set(str(i) for i in range(int(first_range[0]), int(first_range[-1]) + 1))
    second_set = set(str(i) for i in range(int(second_range[0]), int(second_range[-1]) + 1))

    # find the intersection of the two ranges:
    intersection = first_set.intersection(second_set)

    # compare the intersection to previous and store the longest of both:
    if len(intersection) > len(longest_intersection):
        longest_intersection.clear()
        longest_intersection.update(intersection)

sorted_intersections = map(str, sorted(longest_intersection, key=lambda x: int(x)))
print(f"Longest intersection is [{(', '.join(sorted_intersections))}] with length {len(longest_intersection)}")

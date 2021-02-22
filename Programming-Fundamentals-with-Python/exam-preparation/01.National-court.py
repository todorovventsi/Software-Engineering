employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
costumers = int(input())

all_per_hour = employee_one + employee_two + employee_three
hours_needed_no_breaks = 1
breaks = 0
while costumers > 0:
    if hours_needed_no_breaks % 4 == 0 and not hours_needed_no_breaks == 0:
        breaks += 1
    costumers -= all_per_hour
    hours_needed_no_breaks += 1

total_hours_needed = hours_needed_no_breaks + breaks - 1
print(f"Time needed: {total_hours_needed}h.")


# if not costumers % all_per_hour == 0:
#     hours_needed_no_breaks = costumers // all_per_hour + 1
# else:
#     hours_needed_no_breaks = costumers // all_per_hour
#
# breaks = hours_needed_no_breaks // 4
# total_hours_needed = hours_needed_no_breaks + breaks
# print(f"Time needed: {total_hours_needed}h.")

def perfect_or_not(integer):
    # Returns True if "integer" is equal to the sum of its positive divisors
    sum_of_divisors = 0
    for num in range(1, integer):
        if integer % num == 0:
            sum_of_divisors += num
    if sum_of_divisors == integer:
        return True
    return False


number_to_check = int(input())
if perfect_or_not(number_to_check):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

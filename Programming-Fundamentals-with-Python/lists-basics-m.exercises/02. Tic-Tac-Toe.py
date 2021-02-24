r_one = list(map(int, input().split()))
r_two = list(map(int, input().split()))
r_three = list(map(int, input().split()))

# 1.Create a list for each row, column and diagonal
# 2.Add the lists to a new list
# 3.Perform set() on each list
# 4.Check if some of the results has only one element in itself
# 5.If so then we have a winner, check the element and print the winner
# 6.Otherwise it is a draw

c_one = [r_one[0], r_two[0], r_three[0]]
c_two = [r_one[1], r_two[1], r_three[1]]
c_three = [r_one[2], r_two[2], r_three[2]]

d_one = [r_one[0], r_two[1], r_three[2]]
d_two = [r_one[2], r_two[1], r_three[0]]

combinations = [r_one, r_two, r_three, c_one, c_two, c_three, d_one, d_two]
no_duplicates = [list(set(i)) for i in combinations]

winner_list = list(filter(lambda x: len(x) == 1, no_duplicates))

if winner_list:
    if winner_list[0][0] == 1:
        print("First player won")
    elif winner_list[0][0] == 2:
        print("Second player won")
    else:
        print("Draw!")
else:
    print("Draw!")

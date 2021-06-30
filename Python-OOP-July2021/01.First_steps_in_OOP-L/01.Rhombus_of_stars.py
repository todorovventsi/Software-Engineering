def draw_line(n, itt, symbol):
    offset = n - itt - 1
    print(f"{' ' * offset}{symbol * (itt + 1)}".rstrip())


def draw_rhombus(n):
    for i in range(0, n):
        draw_line(n, i, '* ')
    for i in range(n - 2, -1, -1):
        draw_line(n, i, '* ')


draw_rhombus(int(input()))

'''

  *     
 * *
* * *
 * *
  *

'''
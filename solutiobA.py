def max_points(chocolates, initial_chocolates):
    chocolates.sort()

    points = 1
    for bag in chocolates:
        if bag <= initial_chocolates:
            initial_chocolates -= bag
            points += 1
        else:
            break

    return points - 1  # deducting the initial point

# Input
chocolates = list(map(int, input().split()))
initial_chocolates = int(input())

# Output
print(max_points(chocolates, initial_chocolates))

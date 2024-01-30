import math

def calculate_area(x1, y1, x2, y2):
    radius = math.ceil(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return math.ceil(math.pi * radius**2)

def fencing_transaction(A, B, C):
    actual_area = calculate_area(A[0], A[1], B[0], B[1])
    fenced_area = calculate_area(A[0], A[1], C[0], C[1])

    if actual_area < fenced_area:
        extra_area = fenced_area - actual_area
        amount_received = extra_area * 20
        return "Krishna", amount_received
    elif actual_area > fenced_area:
        nearest_square = math.floor(math.sqrt(actual_area))
        area_to_return = nearest_square**2
        if area_to_return > actual_area:
            amount_received = (area_to_return - actual_area) * 20
            return "Krishna", amount_received
        elif area_to_return < actual_area:
            amount_received = (actual_area - area_to_return) * 20
            return "Shiva", amount_received

    return -1

# Input
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Output
result = fencing_transaction(A, B, C)
if result != -1:
    print(result[0], result[1])
else:
    print(-1)

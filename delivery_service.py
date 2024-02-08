# номер и дата проверки на контесте 106928781 8 фев 2024, 22:15:15
weights: list = list(map(int, input().split()))
limit = int(input())


def delivery_service(weights: list[int], limit: int) -> int:
    count_platforms: int = 0
    left_pointer: int = 0
    right_pointer: int = len(weights) - 1
    weights = sorted(weights)
    while left_pointer <= right_pointer:
        overall_weight: int = weights[left_pointer] + weights[right_pointer]
        if overall_weight > limit:
            count_platforms += 1
            right_pointer -= 1
        elif overall_weight <= limit:
            left_pointer += 1
            right_pointer -= 1
            count_platforms += 1
    return count_platforms


print(delivery_service(weights, limit))

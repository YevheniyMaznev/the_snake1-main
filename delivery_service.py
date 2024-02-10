# Номер и дата проверки на контесте 10 фев 2024, 19:46:44 107061542
def delivery_service(weights: list[int], limit: int) -> int:
    count_platforms: int = 0
    left_pointer: int = 0
    right_pointer: int = len(weights) - 1
    weights = sorted(weights)
    while left_pointer <= right_pointer:
        overall_weight: int = weights[left_pointer] + weights[right_pointer]
        if overall_weight > limit:
            right_pointer -= 1
        else:
            left_pointer += 1
            right_pointer -= 1
        count_platforms += 1
    return count_platforms


if __name__ == "__main__":
    weights: list = list(map(int, input().split()))
    limit = int(input())
    print(delivery_service(weights, limit))

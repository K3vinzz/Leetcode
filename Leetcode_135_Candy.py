def candy(ratings: list[int]) -> int:
    arr = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            arr[i] = arr[i - 1] + 1

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and not arr[i] > arr[i + 1]:
            arr[i] = arr[i + 1] + 1

    return sum(arr)

print(candy([1,2,87,87,87,2,1]))

# 1,2,3,1,3,2,1
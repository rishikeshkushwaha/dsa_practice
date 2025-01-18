import time
def binary_search(lst, guess):
    low, high = 0, len(lst) - 1

    while low < high:
        mid = (low + high ) // 2
        if guess == lst[mid]:
            return mid
        elif guess > lst[mid]:
            low =  mid + 1
        else:
            high = mid - 1
    return -1

lst = [x for x in range(1000)]
guess = 80
s = time.time()
print(binary_search(lst,guess))
print(time.time() - s)
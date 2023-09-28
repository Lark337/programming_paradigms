list1 = [1,2,3,4,5,6]
i = int(input("Введите искомое число: "))


def binarySearch(list1,n):
    len1 = len(list1)
    left = 0
    right = len1 - 1
    while (left <= right):
        currIndex = (left + right) // 2
        if(list1[currIndex] == n):
            return currIndex
        elif(list1[currIndex] > n):
            right = currIndex - 1
        elif(list1[currIndex] < n):
            left = currIndex + 1
    return None

print(binarySearch(list1, i))
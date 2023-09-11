def sort_list_imperative(numbers):
    for k in range(len(numbers)):
        max = numbers[k]
        for i in range(k,len(numbers)):
            if numbers[i]> max:
                max = numbers[i]
                maxIndex = i
        print(max)
        temp = numbers.pop(maxIndex)
        numbers.insert(k, temp)
    return numbers

def sort_list_declarative(numbers):
    numbers.sort(reverse = True)
    return numbers

print(sort_list_imperative([1,3,4,6,7,1]))
print(sort_list_declarative([1,3,4,6,7,1]))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Найден искомый элемент, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент находится в правой половине
        else:
            right = mid - 1  # Искомый элемент находится в левой половине

    return -1  # Искомый элемент не найден

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Искомый элемент {target} найден в массиве на позиции {result}.")
else:
    print(f"Искомый элемент {target} не найден в массиве.")
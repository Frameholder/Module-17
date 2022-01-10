
L = sorted(list(map(int, input('Введите  последовательность чисел через пробел ').split()))) #Преобразование введённой последовательности в сортрированный  список
print(L)
element=int(input('Введите  одно любое число '))
print(element)

#Бинарный поиск индекса элемента в списке

def BinarySearch(L, element):
    first = 0
    last = len(L)
    while first < last:
        mid = (first+last)//2
        if element>L[mid]:
            first = mid+1
        else:
            last = mid
    return first-1 if 0 < first < len(L) else "Такого числа нет в диапазоне списка"
print(BinarySearch(L, element))


L = sorted(list(map(int, input('Введите  последовательность чисел через пробел ').split()))) #Преобразование введённой последовательности в сортрированный  список
print(L)
element=int(input('Введите  одно любое число '))
print(element)
#Бинарный поиск индекса элемента в списке
def BinarySearch(L, element):
    first = 0
    last = len(L)-1
    index = False #Если элемента нет в списке - будет False. Как обойти это и вывести индекс ближайшего элемента, как указанов задании????
    while (first <= last) and (index == False):
        mid = (first+last)//2
        if L[mid] == element:
            index = mid
        else:
            if element<L[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
print(BinarySearch(L, element))


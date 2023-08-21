'''Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.'''
def find_duplicat(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [3, 5, 5, 5, 7, 7, 9, 9, 9, 9]
print(find_duplicat(lst))
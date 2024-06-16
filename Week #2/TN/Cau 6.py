def my_func(data,min,max):
    results = []
    for i in data:
        if i < min:
            results.append(min)
        elif i > max:
            results.append(max)
        else:
            results.append(i)
    return results
my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
print(my_func(max=max, min=min, data = my_list))
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_func(max=max, min=min, data = my_list))
def check(N)    :
    list = []
    results = " "
    for i in range(1,5):
        list.append(i)
    if N in list:
        results = "True"
    if N not in list:
        results = "False"
    return results
N = 2
results = check(N)
print(results)
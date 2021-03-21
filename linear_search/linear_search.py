def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return ("NotFound")

data = [50, 30, 90, 10, 20, 70, 40, 60, 80]
print(linear_search(data, 40))
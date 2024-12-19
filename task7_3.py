def check_input(array):
    if len(array) != 2:
        return False

    if type(array[0]) != str or len(array[0]) != 5:
        return False

    if ("." in array[0]) == False:
        return False

    time = array[0].split(".")
    if time[0].isdigit() == False or time[1].isdigit() == False:
        return False

    if (int(time[0]) < 0 or int(time[0]) > 24 or int(time[1]) < 0 or int(time[1]) > 60):
        return False

    if type(array[1]) != int or array[1] < 0:
        return False
    return True

def main(array_of_arrays):
    for array in array_of_arrays:
        if check_input(array):
            print(calculate_time(array))
            break

def calculate_time(array):
    time = array[0].split(".")
    time = [int(time[0]), int(time[1])]
    n = array[1]
    time = [time[0] + n, time[1] + n]
    if time[1] >= 60:
        time[0] += 1
        time[1] = time[1] % 60

    time[0] = time[0] % 24
    return f"{time[0]:02}.{time[1]:02}"

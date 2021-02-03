import array as arr

# 1
def integer_sum():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    sum = int(num1) + int(num2)  # casting because input takes strings
    return sum


# 2
def max_int(num1: int, num2: int, num3: int):
    larg = 0
    if num1 > num2 and num1 > num3:
        larg = num1
    elif num2 > num1 and num2 > num3:
        larg = num2
    else:
        larg = num3
    return larg


# 3
def string_length_multiplication(txt: str, num: int):
    result = len(txt) * num
    print("The result is: " + str(result))


# 4
def string_length_category(txt: str):
    result = len(txt)
    if result < 5:
        print("Small")
    elif result < 10:
        print("Medium")
    else:
        print("Large")


# 5
def leap_year(year: int):
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0 and year % 100 == 0:
        return True
    else:
        return False


# 6
def trim_array(num_array):

    #initialize array with half the length of the given array
    arr_length = len(num_array) / 2
    result_array = arr.array('i', [] * int(arr_length))

    #iterate over given array and check if index is odd
    i = 0
    for item in num_array:
        if i % 2 != 0:
            result_array.append(num_array[i])
            i += 1
        else:
            i += 1

    result_array.reverse()
    return result_array

#7
def check_key(key, dictionary):
    if key in dictionary:
        return True
    else:
        return False

#8
def print_dict(dictionary):
    for items in dictionary.items():
        print(items)


if __name__ == '__main__':
    #print(integer_sum())
    print(max_int(6, 10, 22))
    string_length_multiplication("test", 4)
    string_length_category("teste")
    print(leap_year(2020))
    test_array = arr.array('i', [1, 2, 3, 4, 5, 6])
    print(trim_array(test_array))
    new_dict={'first':1,'Second':2}
    print(check_key("first",new_dict))
    print_dict(new_dict)


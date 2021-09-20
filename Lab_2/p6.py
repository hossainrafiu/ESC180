def display_current_value():
    print(f"Current value: {current_value}")


def add(to_add):
    global current_value
    current_value += to_add


def multiply(to_multiply):
    global current_value
    current_value *= to_multiply


def divide(to_divide):
    # issue: zero division
    if to_divide == 0:
        print("ERROR! Cannot divide by zero.")
    else:
        multiply(1/to_divide)


def memory():
    global current_value
    global memory_value

    memory_value = current_value


def recall():
    global current_value
    global memory_value

    current_value = memory_value


if __name__ == "__main__":
    current_value = 0
    memory_value = 0
    display_current_value()  # 0
    memory()  # save 0
    add(3)  # add 3 to current_value
    display_current_value()  # 3
    recall()  # reset current_value to 0
    display_current_value()  # 0

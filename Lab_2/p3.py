def display_current_value():
    print(f"Current value: {current_value}")


def add(to_add):
    global current_value # With the global keyword, python with give an error saying current_value was not initialized 
    current_value += to_add


if __name__ == "__main__":
    current_value = 0
    display_current_value()
    add(5)
    display_current_value()

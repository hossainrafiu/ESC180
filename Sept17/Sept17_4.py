def adjust_grade(grade): # Argument
    grade = grade - 5
    print("New grade inside the function:",grade)
    return None # Parameter

if __name__ == "__main__":
    grade = 95
    adjust_grade(grade)
    print("New grade outside the function:",grade)
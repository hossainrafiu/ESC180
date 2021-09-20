def adjust_grade():
    global grade
    grade = grade - 5
    print("New grade inside the function:",grade)

if __name__ == "__main__":
    grade = 95
    adjust_grade()
    print("New grade outside the function:",grade)
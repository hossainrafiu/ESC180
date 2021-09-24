def login (username, password):
    global n_attempts

    if n_attempts >= 3:
        n_attempts += 1
        return "refused"

    if username == "a" and password == "a":
        n_attempts = 0
        return "OK"
    if username == "b" and password == "b":
        n_attempts = 0
        return "OK"
    if username == "c" and password == "c":
        n_attempts = 0
        return "OK"
    
    n_attempts += 1
    return "Refused"

def initialization():
    global n_attempts
    n_attempts = 0

initialization()
print("fun")
if __name__ == "__main__":
    initialization()
    print(login("a", "a"))
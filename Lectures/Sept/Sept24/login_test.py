import login_fun  #'Runs' the file (which is why we use __name__ == __main__)

if __name__ == "__main__":
    login_fun.initialization()
    login_fun.login("a", "b")
    print("hello")

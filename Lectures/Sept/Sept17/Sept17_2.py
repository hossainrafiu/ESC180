# type: int, float, str, bool
int(3.14)
int(3.75)
int(-3.75)

float(3)

str(3.14)
approx_pi = 3.14

s1 = "The value of pi is approx: " + approx_pi
s2 = str(approx_pi)

float("3.14")
int("5")

# int("3.14") # ERROR

int(float("3.14"))

# anything that's not "" or 0 is True, "" and 0 are False

bool(3.14)
bool("4.56")
bool("")
bool(0)

if "abc":
    print("hi")

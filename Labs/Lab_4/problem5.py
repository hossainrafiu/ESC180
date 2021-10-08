def leibniz(sumations):
    sum = 0

    for n in range(sumations+1):
        sum += (-1)**n / (2*n+1)

    pi = 4 * sum
    return pi

def leibniz_next(previous, next_summation):
    sum = previous / 4.0
    sum += (-1)**next_summation / (2*next_summation+1)
    return sum * 4.0

def compare_floats(float1, float2):

    # Limit the number of digits checked
    max_digits = len(str(float1)) - 1
    if len(str(float2))-1 < max_digits:
        max_digits = len(str(float2)) - 1

    n = 0
    pre_n = 0
    temp1 = float1*(10**(n-pre_n))
    temp2 = float2*(10**(n-pre_n))
    
    # Get floats to less than 1
    while temp1 > 1.0:
        pre_n += 1
        temp1 = float1*(10**(n-pre_n))

    # check of first digit and place value of both numbers
    n += 1
    temp1 = int(float1*(10**(n-pre_n)))
    temp2 = int(float2*(10**(n-pre_n)))
    if temp1 != temp2:
        return 0

    # check consecutive digits of float 1 and 2 
    while (temp1==temp2 and n<max_digits+1):
        n+=1
        temp1 = int(float1*(10**(n-pre_n)))
        temp2 = int(float2*(10**(n-pre_n)))
        
    return n - 1

if __name__ == "__main__":
    print(compare_floats(123.456, 123.45))
    print(compare_floats(123.456, 123.4567))
    print(compare_floats(122.456, 123.456))
    print(compare_floats(123.456, 223.456))
    

    import math

    sig_fig_same=0
    num_of_sumations=1
    summation = leibniz_next(0, 0)
    while sig_fig_same < 7:
        summation = leibniz_next(summation, num_of_sumations)
        sig_fig_same_temp = compare_floats(math.pi, summation)
        if sig_fig_same_temp > sig_fig_same:
            sig_fig_same = sig_fig_same_temp
            print("num_of_summation:",num_of_sumations,"num of digits same:", sig_fig_same)
            print("Summation:",summation,"pi:",math.pi)
        num_of_sumations += 1
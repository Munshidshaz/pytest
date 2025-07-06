import sys
sys.set_int_max_str_digits(24862048)
def prime_finder(n):
    if n <= 1 :
        return False
    for i in range(2,int(n**0.5)+1):
       if  n%i == 0:
           return False
    else:
        return True


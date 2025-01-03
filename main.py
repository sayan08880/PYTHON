def chake_prime(num) :
    if num <= 1 :
        return f"{num} is not prime"
    for i in range(2,int(num**0.5) +1) :
        if num % i == 0:
            return f"{num} is not prime"
    return f"{num} is prime"
    
num = int(input("enter the number :- "))
print (chake_prime(num))
def prime_checker(number):
   is_prime = True
   for i in range(0, number):
       if number % i == 0:
           #Not a prime
           is_prime = False
   #Is a prime
   if is_prime:
       print("It's a prime number.")
   else:
       print("It's not a prime number.")

if __name__ == "__main__":
    prime_checker(7)
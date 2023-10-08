import math
def prime_number(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_n = math.isqrt(number) + 1  # Ambil akar kuadrat dari n dan tambahkan 1
    for div in range(3, sqrt_n, 2):  # Hanya cek pembagi ganjil, mulai dari 3
        if number % div == 0:
            return False
    return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True

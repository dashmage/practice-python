# generate all primes under n using sieve of Eratosthenes

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
                
    for p in range(int(n**0.5) + 1, n + 1):
        if sieve[p]:
            primes.append(p)
            
    return primes

# Example usage:
n = 50
print("Prime numbers under", n, "are:", generate_primes(n))

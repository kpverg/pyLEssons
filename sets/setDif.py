from intersection import  primeAndSquares  as PS

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(PS.primes_generator(100))
print(primes)
squares = set(PS.squares_generator(100))
print(squares)
print(odds.difference(primes))
print(odds -primes)
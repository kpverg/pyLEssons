from primeAndSquares import squares_generator,primes_generator

even=set(range(0,50,2))
odd=set(range(1,50,2))
#print(odd)
#print(even)
primes=set(primes_generator(100))
squares=set(squares_generator(100))
print(primes)
print(squares)
print(odd.intersection_update(squares))
print(even & squares)

#pass an iterrable to method
even_squares=even.intersection(squares_generator(100))
print(even_squares)
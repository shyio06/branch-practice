# Create fizzbuzz with 1 if line
<<<<<<< HEAD
for i in range(1,5+1):
=======
for i in range(1,20+1):
>>>>>>> 49468a9 (feat: Adjust endnum to 5)
    if i % 3 == 0 or i % 5 == 0:
        print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0))
    else:
        print(f'{i}')

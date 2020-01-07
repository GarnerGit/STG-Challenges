# The length of our Fibonacci sequence
length = 15

# The first two values
x = 0
y = 1
iteration = 0

# Condition to check if the length has a valid input
if length <= 0:
   print("Please provide a number greater than zero")
elif length == 1:
   print("This Fibonacci sequence has {} element".format(length), ":")
   print(x)
else:
   print("This Fibonacci sequence has {} elements".format(length), ":")
   while iteration < length:
       print(x, end=', ')
       z = x + y
       # Modify values
       x = y
       y = z
       iteration += 1
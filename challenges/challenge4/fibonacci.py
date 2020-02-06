# The length of our Fibonacci sequence
class FibFinder:
    def get_fibonacci_number(self,length):

        # The first two values
        x = 0
        y = 1
        iteration = 0

        # Condition to check if the length has a valid input
        if length <= 0:
           print("Please provide a number greater than zero")
           return -1
        elif length == 1:
           print("This Fibonacci sequence has {} element".format(length), ":")
           print(x)
           return x
        else:
           print("This Fibonacci sequence has {} elements".format(length), ":")
           while iteration <length-1:
               #print(x, end=', ')
               z = x + y
               # Modify values
               x = y
               y = z
               iteration += 1
           return x
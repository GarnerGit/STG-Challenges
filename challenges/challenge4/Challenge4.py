import time
import unittest
from challenge4.fibonacci import *
from challenge4.NumberToWords import NumberConverter
from challenge4.fibonacci import FibFinder

class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        length = 15
        fib_obj = FibFinder()
        fibanacci_number=fib_obj.get_fibonacci_number(length)
        print("\n {} order fibonacci number is {}".format(length,fibanacci_number))
        numberwordobject=NumberConverter()
        print(numberwordobject.get_numberforwords(fibanacci_number))
if __name__ == '__main__':
    unittest.main()



# zerotoTwenty = ["", "one", "two", "three".... "nineteen"]
# print (zerotoTwenty[3])
# if number  == 0:
#     print "zero"
# tens = ["", "twenty" "thirty", .... "ninety"]
#
# number = 123456
# partialnumber =  number [4:6] => 456
# partialnumber
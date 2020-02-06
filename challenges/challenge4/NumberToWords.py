class NumberConverter:
    def get_numberforwords(self,number):
        number_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        # Each item in list hs index starting from 0, so number_words[2] will return "Two" in this case


        # using conversion to string to tokenize
        number_string = str(number)
        numberword=""
        for x in number_string:
            digit = int(x)  # Convert to number
            word = number_words[digit]
            #print(word)  # From list, get corresponding word
            numberword = numberword + " " + word
        return numberword
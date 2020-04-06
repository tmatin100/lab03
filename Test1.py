###Final Project###
"""
We are going to write a custom, class representing a credit card. 
This class will emplye the Luhn Algorithm.

This class will have two atributes.: 
	A credit card number, 
	and a cred card type (visa, Mastercard, Amex, Discover)

This class will have three methods:
	determine_card_type()
		this method cehcks wheter or not the credit card has valid 
		starting numbers and updates the class's card type attribute, 
		and returns the card type. 

		Rules: 
			Visa must start with a 4. 
			Mastercard must start with 51, 52,53,54, or 55. 
			Amex must start with 34 or 37. 
			Discover must start with 6011. 

	check_length()
			This method checks wheter or not a credit card number is valid lenth. 
			This method will return a boolean representing wheter or not the card is 
			a valid length. 
			Rules: 
				Visa, Mastercard, and Discover have 16 digits. 
				Amex has 15 digits. 
----------------------------------------------------------------------------------
validate()
    1.Starting from the rightmost digit, exclude the rightmost digit.
    2.Then double the value of every other digit.
    3.Now, sum all the individual digits together (still excluding the rightmost).
    4.Then, multiply that sum by 9.
    5.Then, take its modulo by 10.
    6.If that number is the same as the rightmost digit,
    then the credit card is valid.
    7.Update the valid attribute, and return True or False.
    Example:
      4 4  8 5 0 4 0 9  9 3 2 8  7 6 1 6
      becomes
      8 4 16 5 0 4 0 9 18 3 4 8 14 6 2 6
      Then sum all the digits together
      8 + 4 + 1 + 6 + 5 + 0 + 4 + 0 + 9 + 1 + 8 + 3 + 4 + 8 + 1 + 4 + 6 + 2
      Then multiply that by 9, then modulo that by 10.
      Then, check if it's equal to 6.
Hint: slicing with a step of more than 1

"""

class Credit:
    def __init__(self, card_number, card_type,):
        self.number = card_number
        self.type = card_type
        self.luhnalgo = False

    def determine_card_type(self):
        start_digits = str(self.number)
        if int(start_digits[0]) == 4:
            self.type = "Visa"
        elif int(start_digits[0: 2]) in range(51, 56):
            self.type = "Mastercard"
        elif int(start_digits[0:2]) == 34 or int(start_digits) == 37:
            self.type = "Amex"
        elif int(start_digits[0:4]) == 6011:
            self.type = "Discover"
        else:
            self.type = "invalid card type"
        return self.type


    def check_length(self):
        n = str(self.number)
        if len(n)==16 and self.type in ["Visa", "Mastercard", "Discover"]:
        	n = True 
        elif len(n) == 15 and self.type in ["Amex"]:
        	n = True
       	else:
       		n = "invalid card length"
       	return n 

    def validate():
    	n = str(self.number)
    	rightmost = n[-1]				#captures the last digit only
    	short_n = n[0: -1]           #captures everything but the last digit
		#starting from the right double the value of every other digit.
		short_n[ : : -2]  #all the digits to double
		short_n[-2: : -2] # all the digits to leave alone 

		n2 = []
		for i in short_n[ : : : -2]:
			num_i = int(i)
			num_i *=2
			str_i = (str(num_i))
			if len(stri_i) == 2: 
				n2.append( int(strI[0] + int(str_i[1]) )
			else: 
				n2.append(num_i)

		for x short_n[-2: : -2]:
			num_x = int(x)
			n2.append(num_x)
# Sum all the individual digits ogeter (still excluding the rightmost)
		ans = sum(n2)
		# multiply the sum by 9
		ans*=9
		#take its moduls by 10
		ans %=10 
# if that number is the same as the rightmost digit, the credit card is valid
		if ans == int(rightmost):
			self.luhnalgo = True
		else: 
			self.lunhalgo = False
		return self.lunhalgo


my_card = Credit(4485040993287616, "N/A")
print(my_card.determine_card_type(4)
print(myc_card.check_lenght())
print(myc_card.validate())


card_a = Credit( , )

card_a.type(4)


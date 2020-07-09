# Create a spam message based on specified details
# Joshua Lochner
# 25 February 2018

firstName = input("Enter first name:\n")
lastName = input("Enter last name:\n")
sumOfMoneyInUSD = eval(input("Enter sum of money in USD:\n"))
countryName = input("Enter country name:\n")

print()

print("Dearest",firstName)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk ",lastName,", your long lost relative from Mapsfostol.",sep="")
print("My father left the sum of ",sumOfMoneyInUSD,"USD for us, your distant cousins.",sep="")
print("Unfortunately, we cannot access the money as it is in a bank in",countryName,end=".\n")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",(0.3*sumOfMoneyInUSD),"USD,",sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",lastName)
#Jack Janosik PD: 8 9/30/2025



print("Task 1:")
name = input("Enter your full name:\t")
first_name = name[:name.find(" ",0)]
last_name = name[(name.find(" ",0))+1:]
print(f"{first_name.title()}, {last_name.title()}")
#use 2 seperate print statements for this.
print(f"{(first_name[:1]).lower()}{(first_name[1:]).upper()}",end=',')
print(f" {(last_name[:1]).lower()}{(last_name[1:]).upper()}\n")

print("Task 2:")
quote = "Once you start down the dark path, forever will it dominate your destiny."
encypted_quote = (quote.upper())
encypted_quote = (encypted_quote.replace('A','1'))
encypted_quote = (encypted_quote.replace('E','2'))
encypted_quote = (encypted_quote.replace('I','3'))
encypted_quote = (encypted_quote.replace('O','4'))
encypted_quote = (encypted_quote.replace('U','5'))
print(encypted_quote,end='\n\n')

print("Task 3:")
length = int(len(quote))
first_piece = quote[:(length//3)]
second_piece = quote[((length//3)):((2*length)//3)]
third_piece = quote[((2*length)//3):(length)]
print(second_piece,third_piece,first_piece,sep='',end="\n\n")

print("Task 4:")
num = input("Enter a 5 digit number:\t")
digit1 = int(num[0])
digit2 = int(num[1])
digit3 = int(num[2])
digit4 = int(num[3])
digit5 = int(num[4])
sum = digit1+digit2+digit3+digit4+digit5
print(f"{digit1}+{digit2}+{digit3}+{digit4}+{digit5} = {sum}",end='\n\n')

print("Task 5:")
quote2 = "Why, you stuck-up half-witted scruffy-looking nerf herder."
print(quote2[0::2])
print(quote2[(len(quote2))::-2],end='\n\n')

print("Task 6:")
from datetime import date
today = date.today()
today = today.strftime("%Y,%B,%d")
print(f"The date today is {today}")

year = today[:today.find(',')]
month = today[(today.find(',')+1):today.find(',',(today.find(',')+1))]
day = today[-2:]
print(f"Today is {month} {day}, {year}")
#Jack Janosik PD: 8 9/30/2025



#Task 1
name = input("Enter your full name:\t")
first_name = name[:name.find(" ",0)]
last_name = name[(name.find(" ",0))+1:]
print(f"Your name is {first_name} {last_name}")
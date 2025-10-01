#Jack Janosik PD: 8 9/30/2025



#Task 1
name = input("Enter your full name:\t")
first_name = name[:name.find(" ",0)]
last_name = name[(name.find(" ",0))+1:]
print(f"{first_name.title()}, {last_name.title()}")
#use 2 seperate print statements for this.
print(f"{(first_name[:1]).lower()}{(first_name[1:]).upper()}" +\
      f", {(last_name[:1]).lower()}{(last_name[1:]).upper()}")

#Task 2
quote = "“Once you start down the dark path, forever will it dominate your destiny."

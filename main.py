print("hello world!")

name = input("what is your name?  ")

print(f"big up: {name}")

age = int(input("what is your age?  "))

if age >= 18:
	print("you are an adult")
elif age >= 13:
	print("you are a teenager")
else:
	print("you are a child")
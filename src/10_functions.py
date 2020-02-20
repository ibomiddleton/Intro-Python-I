# Write a function is_even that will return true if the passed-in number is even.

def is_true(x):
	if x%2 == 0:
		print("true")
	else:
		print("false")

print(is_true(2))


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even(x):
	if x%2 == 0:
		print("even")
	else:
		print("odd")

print(is_even(2))
print(is_even(3))

#Write a Python program to triple all numbers of a given list of integers. Use Python map.

Numbers = (1, 2, 3, 4, 5, 6, 7) 
x = map(lambda x: x*3, Numbers) 
print("\nTriple of given numbers:")
print(list(x))
string = input("Please enter a sentence: ").strip()
reversed_string = ""
for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
print("Original string: ", string)
print("Reversed string: ", reversed_string)
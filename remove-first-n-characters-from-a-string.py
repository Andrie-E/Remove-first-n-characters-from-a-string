# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Pseudocode

# code to remove characters from a string starting from index n
def remove_char(input_string, n):
# Check if n is within the limit of the word. if not, provide a error message
    return input_string[n:] if 0 <= n < len(input_string) else "Provide accurate information please!"
# input user code
user_input = input("please provide a word: ")
n = int(input("what is the value of n: "))
# remove char function and print the result

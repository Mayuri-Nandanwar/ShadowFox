#Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the
#result. Try to identify the representation used.

# function to format a number based on given format type.
def format_number(num, fmt):
    formatted_value = format(num, fmt)
    return formatted_value

# calling the function with 145 and 'o'
result = format_number(145, 'o')

# printing the output
print("Formatted value:", result)
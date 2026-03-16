#Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the
#result. Try to identify the representation used.

#the `format` function to return a formatted string.
def convert_value(number, format_type):
    result = format(number, format_type)
    return result

#function with two arguments 145 and 'o'
outputvalue = convert_value(145, 'o')

#print the result.
print("Formatted_value :", outputvalue)
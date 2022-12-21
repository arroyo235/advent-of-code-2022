matrix = [['Z', 'N', '    '], ['M', 'C', 'D'], ['P', '    ', '    ']]

# Use a list comprehension to strip whitespace from each element in the matrix
matrix = [[element.strip() for element in row] for row in matrix]

# Use the filter() function to remove any empty elements from the matrix
matrix = list(filter(None, matrix))

print(matrix)


lst = [['Z', 'N', ''], ['M', 'C', 'D'], ['P', '', '']]


# Use a list comprehension to create a new list with only the non-empty strings
temp = []
result = [x for x in lst if x != '']

# Print the resulting list
print(result == lst)

lst = [['Z', 'N', ''], ['M', 'C', 'D'], ['P', '', '']]

# Use a list comprehension to create a new list with only the non-empty strings
result = [[x for x in sublist if x != ''] for sublist in lst]

# Print the resulting list
print(result==lst)
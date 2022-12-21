"""
TRY 1
"""
import re

# Set the string to parse
string = "[Z] [M] [P]"

# Use the split() method to split the string on the regex pattern "[] "
parts = re.split(" [A-Z] ", string)
print(parts)

# Use the strip() method to remove any leading/trailing whitespace from each part
parts = [part.strip() for part in parts]

# Print the resulting list of parts
print(parts) # ["Z", "M", "P"]



"""
TRY 2
"""
import re

# Set the string to parse
string = "[Z] [M] [P]"

# Use the split() method to split the string on the regex pattern "[] "
parts = re.split("[] ]", string)

# Use the strip() method to remove any leading/trailing whitespace from each part
parts = [part.strip() for part in parts]

# Add quotes around each part using a list comprehension
parts = [f'"{part}"' for part in parts]

# Print the resulting list of parts
print(parts) # ["Z", "M", "P"]


"""
TRY TO PARSE
"""
import re
# string = "[N] [C]    "
# string = "    [D]    "
string = "    [M] [P]     [D]    "


print(re.findall("[A-Z]|\s\s\s", string))
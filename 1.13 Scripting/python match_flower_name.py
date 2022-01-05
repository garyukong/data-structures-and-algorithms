# Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary.
# The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name.
# It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

# Write your code here
# %%
# Create a dictionary from flowers.txt
# Read lines from file into a list:
def CreateDict(input):
    flower_list = []
    with open(input) as file:
        for line in file:
            flower_list.append(line.strip('\n'))

    global flower_dict
    flower_dict = {}
    for flower in flower_list:
        index = flower.find(': ')
        flower_dict[flower[0]] = flower[3:]
    return flower_dict

# %%
# Create a function to ask for user's first and last name
def GetNames():
    name = input('Enter your First and Last name only, separated by a space')
    global firstname, lastname, firstletter
    firstname = name[:name.find(' ')]
    lastname = name[name.find(' ')+1:]
    firstletter = name[0].upper()

# %%
# Print the desired output
CreateDict('flowers.txt')
GetNames()
print("Unique flower name with the first letter: {}".format(flower_dict[firstletter]))

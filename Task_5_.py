# 1. 
given_string = "Guvi Geeks network private limited"

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
total_count = 0

for i in given_string:  
    if i == "a":
        count_a += 1
    elif i== "e":  
        count_e += 1
    elif i == "i":
        count_i += 1
    elif i == "o":
        count_o += 1
    elif i == "u":
        count_u += 1

total_count = count_a + count_e + count_i + count_o + count_u

print("a count:", count_a)
print("e count:", count_e)
print("i count:", count_i)
print("o count:", count_o)
print("u count :", count_u)
print("Total number of vowels:", total_count)




# 2. 
max_num = 20  #Providing the numbers to be in the pyramid 
# first loop is to print the indentation 
for i in range(1, max_num+1):
        print(" " * (max_num - i),end="") # to maintain the indentation till the last line we have added end argument and avoid print() to add a new line
        for j in range(1, i + 1):
            print(j, end=" ")
        print() # Move to the next line after printing each row


# 3. 
input_string=input("Enter the string:")
vowels="aeiouAEIOU"
sub_string=''
for i in input_string:
    if i not in vowels:
        sub_string=sub_string+i
print("The sub string with vowels removed is:",sub_string)


#4. 
input_string = input("Enter a string: ")

unique_chars = set(input_string) # Using a set to store unique characters

count = len(unique_chars) # Getting the count of unique characters

print("Number of unique characters:", count)



#5. 
input_string = input("Enter a string: ")

input_string = input_string.replace(" ", "").lower() # Remove method is used to remove spaces between words, the first argument specifies what to remove and the second argument specifies with what 
#lower method convert to lowercase for case-insensitive comparison

palindrome = input_string == input_string[::-1] # checking if the input string is equal to the reverse input string using slicing method

if palindrome:
    print("True - The given input is a palindrome")
else:
    print("False - The given input is not a palindrome")



#6. 
string1 = "Python Automation"
string2 = "Python"
common_substrings = []  # empty list to store all the common substrings

for i in range(len(string1)):
    for j in range(len(string2)):
        k = 0
        while (i + k < len(string1) and j + k < len(string2)) and string1[i + k] == string2[j + k]:
            k += 1
            if string1[i:i + k] in string2:  # Check if the substring is common
                common_substrings.append(string1[i:i + k])

print(common_substrings)


#7. 
input_string = "Python Program"

char = {} # Dictionary to store input characters as key and their occurances as values 

# Count frequencies of characters in the input string 
for i in input_string: #Python program 
    if i in char:
        char[i] += 1 #This is how we access a value associated with a key in a dictionary 
    else:
        char[i] = 1 


most_freq_char = max(char, key=char.get) # using max function we can call the maximum item in the dictionary , the key parameter is used to get key as the outpu 

print("Most frequent character:", most_freq_char)


#8.
str1 = "free"
str2="reef"
    
str1 = str1.replace(" ", "").lower() # Removing the spaces and convert to lowercase
str2 = str2.replace(" ", "").lower()
    
    
if len(str1) != len(str2): # Checking if the lengths of the strings are different
    print("not an anagram")
    
else:   # Sort the characters in both strings and compare
    if sorted(str1) == sorted(str2):
        print("Its an anagram")
    else:
        print("Its not an anagram")
    


#9.
str1=input("Enter the string:")
print(len(str1))
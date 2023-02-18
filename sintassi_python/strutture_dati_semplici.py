print('hello')

# NUMBER
# create a variable with integer value.
num1 = 100
print("The type of variable having value", num1, " is ", type(num1))

# create a variable with float value.
num2 = 10.2345
print("The type of variable having value", num2, " is ", type(num2))

# create a variable with complex value.
num3 = 100+3j
print("The type of variable having value", num3, " is ", type(num3))

# STRINGS
str1 = "string in a double quote"
str2 = 'string in a single quote'
print(str1)
print(str2)

# using ',' to concatenate the two or several strings
print(str1, "concatenated with", str2)

# using '+' to concate the two or several strings
print(str1+" concated with "+str2)


# LIST
lis = [1, 2, 3, "Ciao", "comparima"]
print(lis)
print(type(lis))

# TUPLE: IMMUTABLE data: in a tuple is write-protected.
tup = (1, 2, 3, "ciao", "comparima")
print(tup)
print(type(tup))

# DICTIONARY: unordered sequence of data of key-value pair form (HASHMAP)
dict = {1: "first name", 2: "last name", "age": 40}

# print value having key=1
print(dict[1])
# print value having key=2
print(dict[2])
# print value having key="age"
print(dict["age"])
print(type(dict))

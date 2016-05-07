print ("I will now count my chickens:")
# Division happens before addition  
print ("Hens", 25 + 30 / 6)
# Multiplication and mod have same precedence, left to right evaluation.
print ("Roosters", 100 - 25 * 3 % 4)

print ("Now I will count the eggs:")
# Division and mod same precedence, left to right evaluation
# Division yields floating point numbers and gives results in decimals
print (3 + 2 + 1 -5 +4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7?")
# Logical evaluation results in "True" or "False" values
print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2)

print ("What is 5 - 7?", 5 - 7)

print ("Oh, that's why it is false.")

print ("How about some more.")

print ("Is it greater?", 5 > -2)
print ("Is it greater or equal?", 5 >= -2)
print ("Is it less or equal?", 5 <= -2 )
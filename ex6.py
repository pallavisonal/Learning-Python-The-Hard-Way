# Not only variables , we can directly put numbers 
x = "there are %d types of people." % 10
binary = "binary";
do_not = "don't"
y = " Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

# %r takes anything , here it took another string containing formatting characters inside of it
# Interestingly , here %r replaced by %x is displayed in quotes.
print ("I said: %r." % x)
# Here we have explicitly put quotes
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Another interesting point- below looks like mod, but it is between two strings, so its just replacement of variables.
print (joke_evaluation % hilarious)

#String concatenation
w = "This is the left side of..."
e = "a string with a right side."

print (w + e)
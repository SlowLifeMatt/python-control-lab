# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
letter = input("Input a letter of the alphabet: ").lower()
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
if letter in vowels:
    print(f"{letter} is a vowel.")
elif letter in consonants:
    print(f"{letter} is a consonant")
else:
    print("Invalid") 
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':



# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
phrase = ""
while phrase != 'quit':
    phrase = input("Enter a word or phrase: ")
# 2. Print the following message:
#      - What you entered is xx characters long
print("What you entered is", len(phrase), "characters long")
# 3. Return to step 1, unless the word 'quit' was entered.


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
human_age = int(input("Input a dog's age in human years: "))


# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
if human_age <= 2:
    dog_age = human_age * 10
#      - Any remaining years count as 7 years each
else:
    dog_age = (2 * 10) + (human_age -2) * 7
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
# Hint:  Use the int() function to convert the string returned from input() into an integer
print(f"The dog's age in dog years is{dog_age}")


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
a = float(input("Enter the lengths of side A of a triangle: "))
b = float(input("Enter the lengths of side B of a triangle: "))
c = float(input("Enter the lengths of side C of a triangle: "))
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length

if a == b == c:
    triangle_type = "equalateral"
elif a == b or a == c or b == c:
    triangle_type = "isosceles"
else:
    triangle_type = "scalene"


# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print(f" A triangle with sides of {a}, {b} & {c} is a {triangle_type} triangle")



# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hint: The next number is found by adding the two numbers before it

# Note: This way takes forever to process. Next option is super fast
# def term(n):
#   if (n==0) or (n==1):
#     return(1)
#   else:
#     return term(n-1)+term(n-2)
# for i in range(50):
#   print(i+1,term(i))

def term(n):
    a=0
    b=1
    if n == 1:
        print(a)
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
print(term(300))



# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
month = input("Input the month")
# 2. Then promptshtt the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

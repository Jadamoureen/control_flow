# use of while loop with condition in middle
vowels = "aeiouAEIOU"
# infinite loop
while True:
    v = input("Enter a vowel: ")
    if v in vowels:
        break
    print("That is not a vowel. Try again.")
print("thank you")

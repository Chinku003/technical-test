""" 
the string takes in whatever the user writes, later the words are split on the second 
line. each word  and stored in the variable text we use the for loop to iterate 
through the words in text one by one, then each  first letter is capitalized and added
to results and a space after each word.  then we use the  strip  function
 to delete any extra spaces and we print the final text

"""

string=input("write down some text:  ")

texts=string.split()

results=""

for text in texts:
    capitalized_text =text.capitalize()
    results += capitalized_text + " "
     
final_text=results.strip()

print(final_text)
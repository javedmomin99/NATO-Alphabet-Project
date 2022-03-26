#Keyword Method with Iterrows
#{new_key:new_value for (index,row) in df.iterrows()}  ##index,row is fixed always, Dont Change it

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

#Since Excel File is already in the form of Data Frame, No need to convert it into Data Frame
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)
def generate_phonetic():
  word = input("Enter a Word: ").upper()
  #for letter in word:
  #letter = phonetic_dict[letter]
  #print(letter)
  #The Above # code can be shortened by List Comprehension as below code (Both works exactly the same)
  try:
    output = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("Sorry, Only Letters in the Alphabet Please!")
    generate_phonetic()
  else:
    print(output)
  
generate_phonetic()
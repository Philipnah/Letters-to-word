# get dictionary

from itertools import permutations 


def Assembly(letters):
     # We put each character from the input string into a list.
     letterList = []
     for char in letters:
          letterList.append(char)


     
     # Get all permutations of length of "lenght"
     y = 0
     tupleList = []
     while y < len(letterList):
          lenght = len(letterList) - y
          perm = permutations(letterList, lenght) 
          
          # we put all the obtained permutations in a list
          for i in list(perm): 
               tupleList.append(i)

          y += 1
     
     # Makes strings from the tuples and puts them in a list
     n = 0
     resultsList = []
     while n < len(tupleList):
          string = "".join(tupleList[n])
          resultsList.append(string)
          n += 1

     return resultsList

     

myInput = input("Input letters: ")
results = Assembly(myInput)



# We need to import and read the dictionary file and compare the strings

with open("dict.txt", "r") as file:
     dictList = file.readlines()

x = 0
while x < len(results):
     z = 0
     while z < len(dictList):
          if results[x] == dictList[z]:
               print("Result: " + results[x])
               break
          else:
               z += 1

     print(results[x])
     x += 1
     

# select only line containing letters
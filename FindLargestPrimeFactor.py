
#To Do:
#Is my math even right?
#edge cases 1, 0 negatives?
#What's going on with my while loop in find_first_factor?
#optimize checking for factors
#remove prints when they are no longer needed for testing
#implement console input of number to check
#There was another thing but I can't remember... (how to handle the case case where the number is prime?)


def find_first_factor(factorof):
  print("Finding first factor of: ", factorof)
  foundfactor = False
  testingfactor = 2
  while (foundfactor == False):
    print("Testing factor:", testingfactor)
    if factorof % testingfactor == 0:
      foundfactor = True
      print("Found first Factor: ", testingfactor)
      return testingfactor
    else:
      testingfactor = testingfactor + 1


def find_largest_pf(numbertotest):
  inversefactor = numbertotest
  while (inversefactor == numbertotest):
    inversefactor = numbertotest // find_first_factor(numbertotest)
    if inversefactor == 1: 
      return numbertotest
    else:
      numbertotest = inversefactor
print ("Largest prime of factor is: ", find_largest_pf(70))
  


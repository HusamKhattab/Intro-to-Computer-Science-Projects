# -*- coding: utf-8 -*-

"""

Created on Fri Nov 24 09:46:09 2017



@author: gg363d

"""



# This function is responsible to check the user input for the meteric.

# The function will only reurn True if the input is correct and Fals if its not.

def checkInput(metric):

    if  metric == "centimeters" or "Centimeters":

          return (True)

    elif metric == "pounds" or "Pounds":

          return (True)

    elif  metric == "meters" or "Meters":

          return (True)

    elif metric == "grams"  or "Grams":

           return (True)

    elif metric == "kilograms" or "Kilograms":

           return (True)

    elif metric == "feet"  or "Feet":

           return (True)

    elif metric == "inches"  or "Inches":

           return (True)

    else:

           return (False)



    

# This is conversions for any of the height metrics to inches

# All of the numbers should be converted into inches and printed

    

# This is conversions for any of the weight metrics to pounds

# All of the numbers should be converted into pounds and printed

    

                 

# This function expects two inputs (height and meteric)  and it will only return

# the hieght in the correct meteric

def checkHeight(height, metric):

  

   if metric == ('centimeters,Centimeters'):

        cent_to_inch = (height / 2.54)

        print (cent_to_inch)

        final_height = cent_to_inch

   elif metric == ('meters,Meters'):

        meters_to_inch = (height * 39.3701)

        print (meters_to_inch)

        final_height = meters_to_inch

   elif metric == ('feet'):

        feet_to_inches = (height * 12)

        print (feet_to_inches)

        final_height = feet_to_inches

   else:

      final_height = height

   print(final_height)

   return final_height 

 # checkWeight()

# This function expects two inputs (weight and meteric)  and it will only return

# the weight in the correct meteric.   

def checkWeight(weight, metric):

  #get_weight = float(input("Please enter your weight"))

  get_weight = weight

  get_weightmetric = metric

  #get_weightmetric = input("Please enter your preferred weight meteric.")

  checkInput(metric)

  if get_weightmetric == ('grams,Grams'):

        gram_to_pounds = (get_weight / 454)

        print (gram_to_pounds)

        final_weight = gram_to_pounds

  elif get_weightmetric == ('Kilogram,kilogram,kilograms,Kilograms'):

        kilo_to_pounds =  (get_weight * 2.20462)

        print (kilo_to_pounds) 

        final_weight = kilo_to_pounds

  else:

        final_weight = get_weight

  print(final_weight)

  return final_weight

    

# This function takes the "bmi" as an input and it will provide advice to the user based on the "bmi" result.

def checkBMIresult(bmi):

 

  if bmi < 18.5:

      print ("Your BMI is" + str(bmi) + "and this is underweight.")

  elif bmi < 24.9:

      print ("Your BMI is" + str(bmi) + "and this is average weight")

  else:

      print ("Your BMI is" + str(bmi) + "and this is overweight")

# The main function will capture the user input and it will call the above functions accodingly       

def main ():

    #height = float(input("Please enter your height. "))  

    valid  = False 

    while valid == False:

      metric = str(input("Please enter your preferred metric for height."))

      valid =  checkInput(metric)
      
    height = float(input("Please enter your height. ")) 

    final_height = checkHeight(height,metric)

    #get_weight = float(input("Please enter your weight")) 

    valid = False 

    while valid == False:

      get_weightmetric = input("Please enter your preferred weight meteric.")  

      valid =  checkInput(metric)              
      
    get_weight = float(input("Please enter your weight"))
    
    final_weight = checkWeight(get_weight,get_weightmetric)

    Bmi = (final_weight / (final_height**2)) * 703

    checkBMIresult(Bmi)

main()

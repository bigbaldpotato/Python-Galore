# Import math module to use mathematical methods (ex. math.pi) for integers and real numbers
import math

# The variable "yesorno" holds the string value for the user input that determines whether the user wishes to continue or end the loop
yesorno = "yes"

# While loop: As long as the user inputs "yes" when asked whether they wish to run the program again, the variable "yesorno" will continue to have the value of "yes" and the loop will continue to run
while yesorno == "yes":

  # Initializing variables
  heightofshape = 0
  diameterofshape = 0
  heightofcone = 0
  heightofcylinder = 0
  radius = 0
  volumeofcylinder = 0
  volumeofcone = 0
  volumeofshape = 0
  unit_of_measurement_height = 0
  unit_of_measurement_diameter = 0
  output_unit = 0

  # Imports module of computer's operating system (OS) dependent methods, allowing program to interact with the OS
  import os
  # Imports time dependent function of "sleep", based on OS's time (python needs system time to use the "sleep" function, to know how long to wait)
  from time import sleep
  # Defining the screen clear function so it may be called at the end of the loop
  def screen_clear():
    # name method is used to get information about the OS from the OS module imported above, info such as name, release, version of the OSsince each has its own clear screen command
    
    if os.name == 'posix':
      # for mac and linux(here, os.name is 'posix')
      # passing clear screen command into system method, output (which is the action of clearing the screen in this case)
      _ = os.system('clear')
    else:
      # for windows platfrom
      # passing clear screen command into system method, output (which is the action of clearing the screen in this case)
      _ = os.system('cls')



  # Outputs prompt for user to enter string value for the metric unit they wish their answer to be in, stored in the variable "output_unt"
  output_unit = str(input("Enter the metric unit you wish your answer to be in: \n"))
  # String value is converted to lower case to avoid errors, and allow values to be matched with an if statement come the sorting and conversion process of units of measurement below
  output_unit = output_unit.lower()  


  # Outputs prompt for user to enter the value of the height of the shape, stored in variable "heightofshape"
  heightofshape = float(input("Enter the height of the shape (without metric unit): \n"))

  # Outputs prompt for user to enter string value for the metric unit for the height of the shape
  unit_of_measurement_height = str(input("Enter the metric unit of the height of your shape: \n"))
  # String value is converted to lower case to avoid errors, and allow values to be matched with an if statement come the sorting and conversion process of units of measurement below
  unit_of_measurement_height = unit_of_measurement_height.lower()

  # Outputs prompt for user to enter the value of the diameter of the shape, stored in variable "heightofshape"
  diameterofshape = float(input("Enter the diameter of the shape (without metric unit: \n)"))

  # Outputs prompt for user to enter string value for the metric unit for the diameter of the shape
  unit_of_measurement_diameter = str(input("Enter the metric unit of the diameter of your shape: \n"))
  # String value is converted to lower case to avoid errors, and allow values to be matched with an if statement come the sorting and conversion process of units of measurement below
  unit_of_measurement_diameter = unit_of_measurement_diameter.lower()



  # Conversion of the real numbers of the height and diameter based on their respective metric units so the answer will be proportionate to the metric unit the user wants to their answer to be outputted in

  # If diameter is in m and height is in cm and user wants output to be in cubic metres
  if unit_of_measurement_diameter == "m" and unit_of_measurement_height == "cm" and output_unit == "m":
    
    heightofshape =  heightofshape/100


  # elif unit_of_measurement_diameter == "m" and unit_of_measurement_height == "m" and output_unit == "m": Both are in metres, no conversion needed

  # If diameter is in cm and height is in m and user wants output to be in cubic metres
  elif unit_of_measurement_diameter == "cm" and unit_of_measurement_height == "m" and output_unit == "m":

    diameterofshape  =  diameterofshape/100

  # If height and diameter are in cm and user wants output to be in cubic metres
  elif unit_of_measurement_diameter == "cm" and unit_of_measurement_height == "cm" and output_unit == "m": 

    diameterofshape  =  diameterofshape/100
    heightofshape =  heightofshape/100



  # If diameter is in m and height is in cm and user wants output to be in cubic centimetres
  elif unit_of_measurement_diameter == "m" and unit_of_measurement_height == "cm" and output_unit == "cm":
    
    diameterofshape  = diameterofshape *100

  # If diameter and height are in m and user wants output to be in cubic centimetres
  elif unit_of_measurement_diameter == "m" and unit_of_measurement_height == "m" and output_unit == "cm": 

    diameterofshape = diameterofshape *100
    heightofshape = heightofshape*100

  # If diameter is in cm and height is in m and user wants output to be in cubic centimetres
  elif unit_of_measurement_diameter == "cm" and unit_of_measurement_height == "m" and output_unit == "cm":

    heightofshape = heightofshape*100


  # elif unit_of_measurement_diameter == "cm" and unit_of_measurement_height == "cm" and output_unit == "cm": Both are in centimetres, no conversion needed


  
  # Calculations
  # The height of the cone is half the height of the shape
  heightofcone = heightofshape / 2

  # The height of the cylinder is half the height of the shape
  heightofcylinder = heightofshape / 2

  # The radius is half the diameter of the shape
  radius = diameterofshape / 2

  # Calculating the shapes seperately, the volume of the cylinder is π x r^2 x height 
  volumeofcylinder = math.pi * ((radius)**2) * heightofcylinder 

  # Calculating the shapes seperately, the volume of the cone is π x r^2 x (height/3) 
  volumeofcone = math.pi * ((radius)**2) * (heightofcone / 3)

  # Add the volume of the shapes together
  volumeofshape = volumeofcone + volumeofcylinder 



  # Outputting the individual volumes of the cone and cylinder, and the volume of the shape as a whole
  print ("The volume of the cylinder is", volumeofcylinder, "cubic", output_unit)
  print ("The volume of the cone is", volumeofcone, "cubic", output_unit)
  print ("The volume of the shape is", volumeofshape, "cubic", output_unit)

  # Asks user whether they want to run the program again, to obtain string value for varaible "yesorno", which will be used to determine whether the loop will run again
  yesorno = str(input("Would you like to run it again?"))

  #  wait for 5 seconds to clear screen
  sleep(5)

  #  now call clear screen function defined above
  screen_clear()

print ("Program has ended")

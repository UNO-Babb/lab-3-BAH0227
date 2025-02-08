#TempConvert.py
#Name: Brock Hoover
#Date: 2/7/2025
#Assignment: Temperature Lab


def main():
  #Prompt the user for a Fahrenheit temperature
  TempInput = input("Enter a Temperature in Fahrenheit: ")
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = TempInput

  tempC = (float(tempF) - 32) * 5/9 

  FinalC = round(tempC, 1)

  print(tempF, "is ", FinalC, "degrees celsius.")
if __name__ == '__main__':
  main()

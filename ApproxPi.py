#ApproxPi.py
#Name:Brock Hoover
#Date:2-8-25
#Assignment: Approximation of Pi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  UserDecimal = input("What Approximation of Pi do you want, (limit of 10):")
  if(int(UserDecimal) <= 10):
    start = time.time()
    #calculate pi using the approximation technique
    #Loop until the level of percision is reached
    approxPi = 4/1
    sign = -1
    denom = 3
    while round(approxPi, int(UserDecimal)) != round(realPi, int(UserDecimal)):
      approxPi = approxPi + (sign * 4 / denom)

      sign = sign * -1
      denom = denom + 2
    end = time.time()

    elapsedTime = end - start
    print("Elapsed Time:", elapsedTime, "seconds")
    print("Approximation of Pi:", approxPi)
  else:
    print("Calculation not Performed, input a value that is less than 10")
if __name__ == '__main__':
  main()

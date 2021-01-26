import math 
def sum_of_no(a,b) : 
  result_of_no = 0
  place_value = 1
  sum_of_digit = 0
  while (a or b) : 
      sum_of_digit = ((a % 10) + (b % 10)) 
      sum_of_digit = sum_of_digit % 10
      result_of_no = (sum_of_digit * place_value) + result_of_no 
      a = math.floor(a / 10) 
      b = math.floor(b / 10) 
      place_value = place_value * 10
  return result_of_no 
a = int(input())
b = int(input())
print (sum_of_no(a,b))

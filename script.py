# Python program to solve quadratic equation

 # Let's solve 8x^2 + 16x + 8 = 0

 # import complex math module  
import cmath  
a = float(input('Enter value for a: '))  
b = float(input('Enter value for b: '))  
c = float(input('Enter value for c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
ans1 = (-b-cmath.sqrt(d))/(2*a)  
ans2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(ans1,ans2))   
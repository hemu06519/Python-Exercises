# Create a Variable

#---------------------------------------------------------------------------------------------------------------------------
# In python a variable is created at the time a value is assigned to it. We dont have to declare it before initialisation.
#---------------------------------------------------------------------------------------------------------------------------

a = 1
print("value of a is ",a)

#---------------------------------------------------------------------------------------------------------------------------
# Python variables can be set to any type of value even after its first initialisation.
#---------------------------------------------------------------------------------------------------------------------------

a=5       # an integer value is assigned to a
a="Five"  # a string value is assigned to a
print("Value of a is ", a)

#---------------------------------------------------------------------------------------------------------------------------
# Varibales are case-sensitive. i.e.. variable a is different than variable A
#---------------------------------------------------------------------------------------------------------------------------

a = 5
A = 10
print("value of a is ", a)
print("value of A is ", A)

#in the above example you can see a=5 is not ovveridden by A=10. Both are created and initialised as two different variables

#---------------------------------------------------------------------------------------------------------------------------
# You can find which type of the value is stored in a variable using type() build in function (BIF)
#---------------------------------------------------------------------------------------------------------------------------

a = 5
b = "Five"
print("Type of a is ", type(a))
print("Type of b is ", type(b))


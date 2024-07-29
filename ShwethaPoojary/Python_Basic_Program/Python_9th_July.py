############################ Data type##########################

""" I)Numbers : 1)Integer
                2)Float
                3)Complex no

    II)Sequential : 1)String
                    2)List
                    3)Tuple

    III)Dictionary
    IV)Set
    V)Boolean

I) Number:
   1)Integer-
             *Immutable data type (Unchangable)
             *Consider +ve and -ve values
             * No limit
             *Only whole no

   2)Float-
            *Immutable data type (Unchanged)
            *Consider +ve and -ve values
            *No limit  (length)
            *Pointer or decimal values

   3)Complex no-
              *Combination of Real and Imaginary


II)Sequential:
   1)String-
           *Immutable data type
           *Define Single/Double/Triple quotes
           *Flows +ve and -ve Indexing
        Indexing: Ex:
                   str_a="PYTHON"

                   0  1  2  3  4  5       +ve Indexing
                   P  Y  T  H  O  N
                  -6 -5 -4 -3 -2 -1       -ve Indexing

                  p(str_a[0])   #P
                  p(str_a[-6])  #P

   2)List-
          * Mutable data type
          *It can contain all type of data
           int, float, str, list, tuple, dict, set, boolean
          *Consider +ve and -ve values
          * Values are comma separated

"""
##################Integer##########################
print("-"*30)

var1=100
print("Variable value :", var1, type(var1))

print("-"*30)

var1=-299            #-ve
var2=56              #+ve
var3=556679869493    #length
print("Variable 1:", var1, type(var1), " ", "Variable 2:", var2, type(var2), " ", "Variable 3:", var3, type(var3))

print("-"*30)

####################Float###########################
var1=55.456
var2=-680.30
var3=484474959
print("Variable 1:", var1, type(var1))   #float
print("Variable 2:", var2, type(var2))   #float'
print("Variable 3:", var3, type(var3))   #int

print("-"*30)

add=var1+var2
add2=var2+var3
print("Addition of variable 1 and 2", add, type(add))
print("Addition of variable 2 and 3", add2, type(add2))

print("-"*30)

##################Complex No############################

data1=10+20j
data2=15+18j
print(data1, type(data1))
print("Real value", data1.real, type(data1))
print("Imaginary value", data1.imag, type(data1))

print("Addition of data values :", data1+data2)
data= data1+data2
print("Addition of data values :", data)
print("Subtraction of data values :", data1-data2, type(data1-data2))

print("-"*30)

######################String#############################

str1=''
str2="H"
str3="Good Morning"
str4='My name is "XYZ"'
str5="My country is 'INDIA'"
str6=""" AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""
str7=''' BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'''
str8='''1.AAAAAAAAAAAAA
        2.BBBBBBBBBBBBBbbb
        3.CCCCCCCCCCCCCCCCCC'''
print("Values: ", str1, type(str1))
print("Values: ", str2, type(str2))
print("Values: ", str3, type(str3))
print("Values: ", str4, type(str4))
print("Values: ", str5, type(str5))
print("Values: ", str6, type(str6))
print("Values: ", str7, type(str7))
print("Values: ", str8, type(str8))

print("-"*30)

print(str3+" "+str4)
print(str3+" "+str4+" "+str5)
print("Indexing:", str3[3])
print("Indexing:", str5[14], str5[15], str5[16])

print("-"*30)

#############################List###############################
list2=[3,5,7]
list2.append(56)
print(list2)


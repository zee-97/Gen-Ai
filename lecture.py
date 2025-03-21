# #01 display the names in output

# print ("Hello World")
# print(96)
# print(False)
# #print[type(True 1549)]

# #02 legal names of variables

# name="zohaib" #simple case

# firstName = "Ahad" #camel case

# firstName = "Hoor" #pascal case

# first_name = "saad" #snake case

# name1st = "Mano" # numbercase; case sensitive;
# #1stname= "mano" # number cannnot be used in start

# _name = "amna" # we can't use this type of variable because it is used in function 
# # $name = no symbol in start can be used in python 

# # underscore help to seperate the words

# #hyphen can't be used during declartion of variables 

# #03 type of variables;

# print(type("Zohaib"))   #string
# print(type(23))         #integration 
# print(type(True))       #bool
# print(type(3.25))       #float
# print(type(1j))         #complex


# # 04 data type in python 

# # array is called List in python 

# a='string'
# b=True
# c=34
# d=34.5
# e=1j
# f=["aslam","amna","asma"]           #it is called list,| index = total length -1,| index = 2, length = 3
# print(len(f))                       # it show length(len) in output 3
# print(len(f)-1)                     # it show index in output 2
# g=("hello","world","!")          #mit(most important question)   #(immutable) tupple can't be change and consector is used to change it, using consector typecasting is used to change tupple into list than change the data and convert it back
#                                  # only tupple is immutable and all the other are muteable
# h={"name":"umar", "age":24}         #() braces/round braces, {} curly braces used in dictionary, [] square braces

# # what is diffence between list (index,number call) and dictionary ( {}use in pairing, keys and values)
 
# i=b"hello world"                    # bytes, 4 bits is called 01 nibble, 8 bits is called 02 nibbles
# j = {"hi","many","fight"}            #set

# print(type(j), j)

# # ---------------------------Most Important Question---------------------------
# # what is difference between mutable and immutable 


# # 05 math operation

# a = 4
# b = 2

# # sum = a + b
# # print(sum, type(sum)) # code runner ko kessy use karna ha like save code and old code kessy arrow sy reuse ho gye
# #print(a ** b)

# # 06 input type

# #a = input ("Enter your name : ")

# print(a, type(a))

# # cls command is used to clear terminal 
# # type casting is used for different type of data type

# # mit typecasting ku zarori ha ? / data type ku zarori ha ? (agar data string ma rahe toh like age kabhi change nahi ho gi thats why ussy data type int mai change ho jata ha)

# # 07 if conditions 

# num = 100

# if (num >= 45 and num <= 50 ) :   # first condition is "if"                   # single equal "=" is used to   / double equal "==" used to compare 
#     print("you are passed")
# elif (num >= 90 and num < 101 ) :              # "< or > is equal to <= or >= in this condition"      # in between the conditions
#     print("you are passed Grade A")
# else :                              # if all conditions not meet then else is used 
#     print("you are not passed")


# num = 20                #mit nestic condition---ak condition k true hony sy dusri condition py jyen varna else use ho ga 
# num2 = 60
# if num == 20:
#     if num2 == 40:
#         print("you got both right")
#     elif num2 == 60:
#         print("hurrey you got it")
#     else:
#         print("you got 2nd wrong")
# else:
#     print("you got both wrong")

# # 08 type casting (regex is used to prevent other type of data that is not needed)

# # num = "45"
# # num = int(num)          #any thing green is object
# # print(type(num))

# # num2 = "45"
# # num2 = str(num2)
# # print(type(num2))

# num3 = 45.6
# num3 = float(num3)
# print(type(num3))

# val = input("Enter your age in number : ")
# val1 = int(val)
# print(type(val1), type(val))                #java and python are based sinculus method(run first line than second and so on)



# # 09 multiline string

# #   "" quations represent string

# b = """hello world how are 
# you;"""
# print (b)

# c = "hello world"  # single length string ya multi length strin ki type ma koi farak ata ha ya length mai farak ata ha

# print(type(c), len(c))



# # 10 concatenation


# a = "hello"
# b = " world"
# print (a + "" + b)


# a = 42
# b = 43
# c = "hello world!"
# print(str(a) + str (b) + "" + c)

#11 format in string and integer/float
# marks = 45
# total = "your total marks is 100 and you got {}"

# object =  total.format(marks)
# print(object)

# age = 24
# total = 100
# obt = 90
# res = "your age is {0} and your total marks {2} and obtain marks {1}"   #indexing is start with 0 

# tot = res.format(age,obt,total)

# print (tot)



# 12 string slicing


# a = "hello world !"
# print(a[0:2])

# a = "hello world!"
# print(a[-3:-1])
# print(a[0:])
# print(a[:5])



# 13 split in string

                            #mit on notebook lecture 02
# a = "hello AI class"
# b = a.split(" ") 

# print(a , b)             #[] is the alamat of list



# 14  upper case and lower case in string


# st = "hello world"

# up = st.upper()
# lo = st.lower()

# print(up, lo)
# print(st.upper(),st.lower())

# st = "hello world"
# print(st.capitalize(),st.title())      # () after capitalize buz it is the nishani of funtion

# a = "hello"
# b = "world"
# print(a.capitalize()+ " " + b.capitalize())


# 15 replace methods

# a = "hello"
# b = a.replace("h","p")
# print(b)


# 15 Lists              most important thing

# ls = ["Lahore","faisalabad","jaranwala"]
# print(type(ls))

# ls = list(("Lahore","faisalabad","jaranwala"))      # when ever we made something and intentionally mention "list" and use double parentheses (()) than is called constructor method
# print(type(ls))

# ls = []
# ls = ["Lahore","faisalabad","jaranwala"]
# print(type(ls),ls)                            # alt+arrow to move line up/down.
# print(type(ls),ls)                      #joh value name "ls" k name k sath second time value den gye toh first wali ko cincornise kar dy ga 

# ls = ["Lahore","faisalabad","jaranwala"]
# print(ls[0:1])

# ls = ["Lahore","faisalabad","jaranwala"]
# print(ls[2:])

# ls = ["Lahore","faisalabad","jaranwala"]
# ls[1:2] = ["Multan"]                          #this method replace multiple values
# print(ls)

# ls = ["Lahore","faisalabad","jaranwala"]
# ls[1:2] = "Multan"                              #Multan ko direct ls consider 
# print(ls)

# ls = ["Lahore","faisalabad","jaranwala"]
# ls[1] = "Multan"                              #this method replace only single value 
# print(ls)


# ls = ["Lahore","faisalabad","jaranwala"]
# ls[0:1] = ["Karachi"]
# ls[2:] = ["Multan"]    
# ls[1:2] = ["Peshawar"]
#or add multiple
# ls[0:] = ["Lahore","Faisalabad","Jarawala","Peshawar"]                          
# print(ls)

# ls = ["Lahore","faisalabad","jaranwala"]
# ls.append(("Peshawar"))                       #append add value in end 
# print(ls)


# ls = ["Lahore","faisalabad","jaranwala"]
# ls.insert(1,"Peshawar")                         #insert add value in given location
# print(ls)

# ls = ["Lahore","faisalabad","jaranwala"]
# ls.pop(0)                                      #pop use to remove using index number
# print(ls)

# ls = ["Lahore","faisalabad","jaranwala"]
# ls.remove("faisalabad")                                      #remove use to remove using full name
# print(ls)


# ls = ["Lahore","faisalabad","jaranwala"]
# del ls[0]
# print(ls)

# x del ls
# x def __init__ 


# ls = ["Lahore","faisalabad","jaranwala"]
# ls.clear()                                      #clean use to clean everything in list
# print(ls)



# 16 for loops                  #wire loop available and do why loop not available in python


# ls = ("apple","banana","mango", "orange")  #by using () in ls it will made it tuple
# print(type(ls))

# print(ls)
# for item in ls:                     #item or val can be anything, item woh cheez ha joh value ko single single kar k show karta ha 
#     print(item)

# repositery in github


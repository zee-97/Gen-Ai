# age = input("enter your age : ")
# age = int(age)
# education = input ("enter your education : ")
# education = int(education)
# height =  input ("enter your height in feet :")
# height = float(height)

# if (height >= 5.6) :
#     if (education >= 12) :
#         print("Congratulation you paased the eligiblilty criteria")
# #    elif (age =>18 and age =<32): 
#         print("Congratulation you paased the eligiblilty criteria")




edu = int (input("Enter your education : "))
age = int (input ("Enter your age : "))
height = float(input("Enter your height : "))

if( edu => 12 and (age <= 32 and age >= 18)):
    hprint("passed")
elif( height =>5.6 and (edu => 12)) :
    print("passed")
elif(age <= 32 and age >= 18 and (height => 5.6))
    print("passed")
else("failed")
    


# assignment 02

# marks = int(input("Enter your marks : "))
# total_marks= int(input("Enter your total marks : ")) 
# print (marks/total_marks*100)


# assignment 03

# Bonus_Amount = float(input("Enter bonus amount : "))
# if Bonus_Amount < 0 :
#     print ("Invalid. Enter valid number.")
# Bonus_percentage = float(input("Enter bonus percentage : "))
# if Bonus_percentage < 0 or Bonus_percentage > 100 :
#     print ("Invalid percentage. Enter valid number.")
# total_salary = (Bonus_Amount/Bonus_percentage) * 100
# object
# print ("Total salary",total_salary)


# assignment 04

# st = "jaranwala faisalabad lahore"
# print(st[0].upper()+st[1:9], st[10].upper()+st[11:19], st[20].upper()+st[21:])



# assignment 05

# a = "jaranwala faisalabad lahore"
# print(a[0].lower()+a[1:9].upper(), a[10].lower()+a[11:20].upper(), a[21].lower()+a[22:].upper())



# assignment 06

# st = "jaranwala faisalabad lahore"
# print(st.replace("j","J").replace("f","F").replace("l","L"))


# assignment 07 

st = "Jaranwala Faisalabad Lahore Karachi Multan"
print(st.replace("J","j").replace("F","f").replace("L","l").replace("K","k").replace("M","m"))


#assignment 08

# ls = ["lahore","faisalabad","jaranwala"]
# for item in ls:
#     print(item.capitalize())

#   -------------------

# ls = ["lahore","faisalabad","jaranwala"]
# ls[0:1] = ["Lahore"]
# ls[1:2] = ["Faisalabad"]
# ls[2:] = ["Jaranwala"]
# print(type(ls), ls)

#   -------------------

# ls = ["lahore","faisalabad","jaranwala"]
# lp = []
# for x in ls:
#     p = x[0:1].upper()+ x[1:-1].lower()+ x[-1:].upper()
#     lp.append(p)
#     print(p)
# print(lp)

#   -------------------

# ls = ["lahore","faisalabad","jaranwala"]
# lp = []
# for x in ls:
#     p = x [1:2].upper()+x[0:-1]+x[-2:-1].upper()
#     lp.append(p)
# print(lp)


#   -------------------
ls = ["lahore","faisalabad","jaranwala"]
lp = []
for x in ls:                                                                    #insert has in and specific value 
    lp.insert(0,x) 
print(lp)

#   -------------------
#   -------------------
#10 cities ko sab sy play reverse than first and last digit ko capitalize and darmiyan mai capital ko bhi small kar dy 
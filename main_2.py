



#flask

#django
#fastApi

#variables
#LOGIC ARITHMETIC
#BODMAS
a=9*(85+5)
print(a)

#dictionary in python
#  diction= {
#     username:"Qwinpelumight",
#     password:"pelumight8",
#     profile:"photo.jpg",
#     Bio:"iam a cyber expert", 

# }

#control flow
# if staatement
# while
# for loop 
# for

# num=24 
# if 23==24:
#     print("this is even number")
# else: print("no, its not compatible")

# class_attendance=8
# while class_attendance==8:
#     print("class should start")

# christmas=12
# countdown=0
# while christmas!=countdown:
#     print("Not yet christmas")
#     break

# if christmas==countdown:
#     print("yay!its christmas!!!!")
# elif christmas==2:
#     print("viola!!! Its boxing day")
# else: print("oops sorry....")




# while True:
#     if christmas>0:
#         christmas=christmas-1
#         print(christmas)
#         if christmas==0:
#             print("yaayyyyyyyyyyy!!! we go do obleeee - it is christmas")
 
 
#List
students_in_cohort3=["Mr Odo", "Mr shina", "ms Oluwapelumi", "Mr Segun", "Mr Adeayo", "Miss Olaitan", "Mr obalabi",]
# print(students_in_cohort3[2])
# print(students_in_cohort3[2:])
fst=students_in_cohort3[0]
lst=students_in_cohort3[6]
# print(fst,lst)

#class work
Deyork_Auto=["mercedes", "Toyota camry", "Range rover","under","Micra","car",]
middle_to_the_last=Deyork_Auto[2:]
middle_to_the_front=Deyork_Auto[:2]
first_auto=Deyork_Auto[0]
last_auto=Deyork_Auto[5]
# print(middle_to_the_last)
# print(middle_to_the_front)
# print(first_auto,last_auto)




# variable name/ function name
# there are 3 way of wriying a variable name/ function name
# snake case everything is small letter with underscore eg addition_of_two_number
# camel case written with upper case and lower case eg AdditionOfTwoNumber
# PASCA 

def addition ():
    first_number=34
    second_number=289
    sum=first_number+second_number
#     print(sum)
    #codeblock
def return_string():
        return "Testing"
    
def call_two_function():
        addition()
        message=return_string ()
        print(message)

call_two_function()

username="Oluwapelumi"
password="qwin1234"
def user_validation(check_username,check_password):
    if check_username==username and check_password==password:
          print("username and password is authenticated, loggin in..")
    elif check_username!=username:
          print("incorrect username")
    elif check_password!=password:
          print("incorrect password")

user_validation("Oluwapelumi", "qwin1234")


# how to use boolean in program
# check_num1=2
# check_num2=4
# print(check_num1==check_num2)

if __name__=="_main__":
      user_validation()
      addition()
      return_string()
      call_two_function()


      
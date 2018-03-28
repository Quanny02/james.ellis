#james ellis     march 23, 2018

print  ("This will need your number grade so your average will be calculated.")

sub_one, grade_one = input("What subject is this?: "), float(input("what grade do you have?: "))
sub_two, grade_two = input("What subject is this?: "), float(input("what grade do you have?: "))
sub_three, grade_three = input("What subject is this?: "), float(input("what grade do you have?: "))
sub_four, grade_four =input("What subject is this?: "), float(input("what grade do you have?: "))
sub_five, grade_five = input("What subject is this?: "), float(input("what grade do you have?: "))
   
    
new_list= [sub_one, sub_two, sub_three, sub_four, sub_five]
new_listtwo= [grade_one, grade_two, grade_three, grade_four, grade_five]

grade_average= float((grade_one + grade_two + grade_three + grade_four + grade_five) / 5)
new_listtwo.append(grade_average)
new_list.append("average")

print new_list
print new_listtwo

if grade_average in range(1,59):
   print ("you are failing.")
    
if grade_average in range(60,78):
    print ("you are at average") 
    
if grade_average in range(79,88):
    print ("you are above average")
   
if grade_average in range(89,100):
    print("you are passing")
    

total_sum = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
#Write your code below this row 👇
  total_sum = total_sum + student_heights[n]
  
  #print("n : ",n)
  #print("student_heights : ",student_heights)
  #print("student_heights[n] : ",student_heights[n])

#print("total_sum : ",total_sum)
calculation =  total_sum/len(student_heights)
print("calculation", calculation)
print(round(calculation))




total_users = int(input("Enter total users:"))
staff_users = int(input("Enter staff users:"))
nonteaching_staff = staff_users//3
staff_users = staff_users + nonteaching_staff
student_users = total_users - staff_users
print("student users =",student_users)

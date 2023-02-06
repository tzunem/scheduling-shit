#weekdays
monday = [8.30, 3.12, 4.00, 6.30, 8.30]
tuesday = [8.30, 3.12, 3.00, 6.30, 8.30]
wednesday = [8.30, 2.20, 4.00, 6.30, 8.30]
thursday = [8.30, 3.12, 3.00, 6.30, 8.30]
friday = [8.30, 2.20, 4.00, 7.00, 9.30]

    #weekend
saturday = [9.00, 10.00, 11.30, 5.00, 10.00]
sunday = [9.00, 10.00, 11.00, 5.00, 8.30]
    #extra days off (monday off etc.)
sunday_extra_day = [9.00, 10.00, 11.30, 5.00, 10.00] #same as saturday schedules
extra_day_off = [9.00, 10.00, 11.00, 5.00, 8.30]
    #actual breaks (spring break etc.)
breakdays = [9.00, 10.00, 11.30, 5.00, 10.00]
lastbreakday = [9.00, 10.00, 11.00, 5.00, 8.30]

#Lineup 
weekdays = [monday, tuesday, wednesday, thursday, friday]

weekend = [saturday, sunday]

dayoff = [sunday_extra_day, extra_day_off]

actualbreaks = [breakdays, lastbreakday]


#----------------------------------------
usernames = input('''Hello! Please enter your first and last name. 

''')
print("Username has been saved. Remember it!!") 

password = input('''Please create a password.

''')

print('Your password has been saved. Remember it!')
#above is password and username that the user should know

userask = input("""Please type in your username. It's case-sensitive! 

""")
passask = input('''What is your password?

''')

if userask == usernames and passask == password:
    print("Welcome back", usernames, "!")
else: 
    print("Username or password is incorrect! Remember, it's case-sensitive.")


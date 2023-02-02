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
first_lastname = input('''Hello! Please enter your first and last name.

''')
print("Hello there " + first_lastname )

password = input('''Please make a password

''')

print(password + 'is now your password. Please remember it.')

userask = input("""Input your username

""")
passask = ('''Input your password
    
    ''')
if userask == (first_lastname):
    print("Right Username")
    
else:
    print("wrong user")

if passask == (password):
    print("right password")
else:
    print("wrong password")







thing = "#weekdays
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
first_lastname = input('''Hello! Please enter your first and last name.

''')
print("Hello there " + first_lastname )

password = input('''Please make a password

''')

print(password + 'is now your password. Please remember it.')

userask = input("""Input your username

""")
passask = ('''Input your password
    
    ''')
if userask == (first_lastname):
    print("Right Username")
    
else:
    print("wrong user")

if passask == (password):
    print("right password")
else:
    print("wrong password")"
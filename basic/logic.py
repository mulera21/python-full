# its time to add some logic

#logic - syntax
if 5 > 2:
    print("5 is greater than 2")    

#logic - syntax with if/elif/else

temp = 30

if temp >30:
    print("It's a hot day")

elif temp > 20:
    print("It's a nice day")

else:
    print("It's a cold day")

#nested if statements

panel_width = 900
panel_hieght = 2500

if panel_width < 1200:
        print("The panel width is acceptable")
else:
        print("The panel width is too large")
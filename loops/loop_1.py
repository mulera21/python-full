#loop
#---------------------------------------------
#iterating using while loop

big_number = 123456789

for digit in str(big_number):
    print(digit)

#---------------------------------------------
#nested for loop

course = [['math', 'science', 'history'],
          ['art', 'music', 'literature'],
            ['physics', 'chemistry', 'biology']]

for subject_list in course:
    print(f"stating the module:{subject_list}")

    for subject in subject_list:
        print(f"completing subject: {subject}")

        print("subject completed")
    print("module completed")
#---------------------------------------------
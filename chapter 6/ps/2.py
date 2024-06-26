subject1 = int(input("Enter marks in 1st subject: "))
subject2 = int(input("Enter marks in 2nd subject: "))
subject3 = int(input("Enter marks in 3rd subject: "))

total_marks = ((subject1+subject2+subject3) / 300) *100

if total_marks>=30:
    print("You passed, your total percentage: ", total_marks)
else:
    print("You failed, your total percentage: ", total_marks)
choice = "YES"
#repeats program as long as choice == "YES"

while choice == "YES":
    #grade input
    javaScore = float(input("Enter Java Programming score: "))
    cScore = float(input("Enter C Programming score: "))
    databaseScore = float(input("Enter Database Handling score: "))
    
    #average calculation
    sum = javaScore+cScore+databaseScore
    average = float(sum)/3
    
    if average < 75:
        finalGrade = 'F'
        print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is below 75.")
    elif average < 80:
        finalGrade = 'C'
        print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is between 75-79.")
    elif average < 90:
        finalGrade = 'B'
        print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is between 80-89.")
    else:
        finalGrade = 'A'
        print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is between 90-100.")
        
    choice = input("Do you want to continue? (YES/NO): ")
    if choice == "NO":
        print("Program terminated. Thank you!")

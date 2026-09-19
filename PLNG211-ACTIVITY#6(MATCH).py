choice = "YES"
#repeats program as long as choice is "YES"

while choice == "YES":
    #grade input
    javaScore = float(input("Enter Java Programming score: "))
    cScore = float(input("Enter C Programming score: "))
    databaseScore = float(input("Enter Database Handling score: "))
    
    #average calculation
    sum = javaScore+cScore+databaseScore
    average = float(sum)/3
    averageS = int(average)
    
    
    match (averageS):
        case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
            finalGrade = 'A'
            print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is between 90-100.")
        case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
            finalGrade = 'B'
            print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is between 80-89.")
        case 75 | 76 | 77 | 78 | 79:
            finalGrade = 'C'
            print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is between 75-79.")
        case _:
            finalGrade = 'F'
            print("Average:", round(average, 2), "| Grade:", finalGrade,"because the average is below 75.")
        
    choice = input("Do you want to continue? (YES/NO): ")
    if choice == "NO":
        print("Program terminated. Thank you!")

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.activity1ifelse;

/**
 *
 * @author VAL-SBH-CL3-WS-24
 */
import java.util.Scanner;

public class ACTIVITY1IFELSE {
    public static void main(String[] args) {
        Scanner grade = new Scanner(System.in);
        
        String choice;
        do {
        
        System.out.println("Java Score: ");
        double javaScore = grade.nextDouble();
        
        System.out.println("C Score: ");
        double cScore = grade.nextDouble();
        
        System.out.println("Database Handling Score: ");
        double databaseScore = grade.nextDouble();
        
        double average;
        average = (javaScore + cScore + databaseScore) / 3;
        String finalGrade;
        
        if(average < 75) {
            finalGrade = "F";
        }
        else if (average < 80) {
            finalGrade = "C";
        }
        else if (average < 90) {
            finalGrade = "B";
        }
        else {
            finalGrade = "A";
        }
        String roundedAverage;
            roundedAverage = String.format("%.3f", average);

        System.out.println("Output: "+finalGrade);
        System.out.println("The average of the student is "+roundedAverage+", so the student's grade is "+finalGrade+".");
        
        System.out.println("Do you want to continue (YES/NO): ");
        grade.nextLine();
        choice = grade.nextLine();
        } while (choice.equalsIgnoreCase("YES"));
    }

}

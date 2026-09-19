/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.activity1switch;

/**
 *
 * @author VAL-SBH-CL3-WS-24
 */
import java.util.Scanner;

public class ACTIVITY1SWITCH {
    public static void main(String[] args){
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
        average = (javaScore + cScore + databaseScore) / 3.0f;
        char finalGrade;
        int average1 = (int) average;
        
        finalGrade = switch (average1) {
                case 75, 76, 77, 78, 79 -> 'C';
                case 80, 81, 82, 83, 84, 85, 86, 87, 88, 89 -> 'B';
                case 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 -> 'A';
                default -> 'F';
            };
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

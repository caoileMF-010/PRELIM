/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.activity2;

/**
 *
 * @author VAL-SBH-CL3-WS-24
 */
import java.util.Scanner;
public class ACTIVITY2 {
    public static void main(String[] args) {
        Scanner value = new Scanner(System.in);
        
        String choice;
        do {
        System.out.println("Variable Values: ");
        System.out.printf("X = ");
        double x = value.nextDouble();
        
        System.out.printf("Y = ");
        double y = value.nextDouble();
        
        //Arithmetic Operations
        double sum = x+y, difference = x-y, product = x*y, quotient = (double) x/y,
        remainder = x%y;
        
        //Output
        System.out.println("\nArithmetic Operations");
        System.out.println("Addition: "+x+" + "+y+" = "+sum);
        System.out.println("Subtraction: "+x+" - "+y+" = "+difference);
        System.out.println("Multiplication: "+x+" * "+y+" = "+product);
        System.out.println("Division: "+x+" / "+y+" = "+quotient);
        System.out.println("Modulus: "+x+" % "+y+" = "+remainder);
        double increment = ++x;
        System.out.println("Increment: "+(--x)+"++ = "+increment);
        double decrement = --x;
        System.out.println("Decrement: "+(++x)+"-- = "+decrement);
        
        System.out.println("Do you want to continue? (YES/NO): ");
        value.nextLine();
        choice = value.nextLine();
        
        } while (choice.equalsIgnoreCase("YES"));
    }
}

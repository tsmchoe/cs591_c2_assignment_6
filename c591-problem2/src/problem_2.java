import java.util.Scanner;


/*
For this problem, you must create a console application which asks users to choose a shape
and will calculate the area and perimeter (or circumference), given the radius or length and
breadth of the shape. Your application only needs to account for 3 shapes: squares, rectangles,
and circles. You must use TDD to develop your solution.

Example:
Program prints “Choose a shape: (C)ircle or (R)ectangle or (S)quare”,
and the user answers “R” Then the program prints “Rectangle length?”
and the user answers “4” Then the program prints “Rectangle breadth?”
and the user answers “5” The program prints “Area: 20 square units and Perimeter: 18 units”
 */

public class problem_2 {

    public static void main(String[] args){
            System.out.println("Choose a shape: (C)ircle or (R)ectangle or (S)quare");
            Scanner myObj = new Scanner(System.in);  // Create a Scanner object
            String choice = myObj.nextLine();  // Read user input
            System.out.println(answerQuestion(choice));
    }

    /*
        Input: Asks users questions
        Output: Returns Answer
     */
    public static String answerQuestion(String choice){
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        if(choice.equals("C")){
            System.out.println("Circle's radius?");
            Double radius = myObj.nextDouble();
            Double area = circleArea(radius);
            Double perimeter = circlePerimeter(radius);
            return "Area: " + area + " square units and Perimeter: " + perimeter + " units";
        }
        else if(choice.equals("R")){
            System.out.println("Rectangle's length?");
            Double length = myObj.nextDouble();
            System.out.println("Rectangle's breadth?");
            Double breadth = myObj.nextDouble();
            Double area = rectangleArea(length, breadth);
            Double perimeter = rectanglePerimeter(length, breadth);
            return "Area: " + area + " square units and Perimeter: " + perimeter + " units";
        }
        else if(choice.equals("S")){
            System.out.println("Square's length?");
            Double length = myObj.nextDouble();
            Double area = squareArea(length);
            Double perimeter = squarePerimeter(length);
            return  "Area: " + area + " square units and Perimeter: " + perimeter + " units";
        }
        else{
            return "Please enter a Circle, Square or Rectangle";
        }
    }

    // Calculates the circle's perimeter
    public static Double circlePerimeter(Double radius) {
        if(radius >= 0){
            return 2 * Math.PI * radius;
        }
        return null;
    }

    // Calculate the circle's area
    public static Double circleArea(Double radius) {
        if(radius >= 0){
            return Math.PI * radius * radius;
        }
        return null;
    }

    // Calculate the square's perimeter
    public static Double squarePerimeter(Double length) {
        if(length >= 0){
            return 4 * length;
        }
        return null;
    }

    // Calculate the square's area
    public static Double squareArea(Double length) {
        if(length >= 0){
            return length * length;
        }
        return null;
    }

    // Calculate the rectangle's perimeter
    public static Double rectanglePerimeter(Double length, Double breadth) {
        if(length >= 0 & breadth >= 0){
            return 2 * length + 2 * breadth;
        }
            return null;

    }

    // Calculate the rectangle's area
    public static Double rectangleArea(Double length, Double breadth) {
        if(length >= 0 & breadth >= 0){
            return length * breadth;
        }
            return null;
    }

}

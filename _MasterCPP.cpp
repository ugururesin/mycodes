
// WELCOME TO C++-PROGRAMMING! - 2019
// By Ugur Uresin

// CONTENT
// 01 DATA TYPES & FORMATS
// 02 ARITHMETIC OPERATIONS
// 03 ARITHMETIC STATEMENTS
// 04 APPOINTMENT, INCREASE, DECREASE
// 05 TYPE TRANSFORMATIONS
// 06 INPUT/OUTPUT FUNCTIONS
// 07 EXAMPLE PROGRAM: AVERAGE CALCULATOR (SCANF)
// 08 EXAMPLE PROGRAM: PARABOLA ROOT CALCULATOR (SCANF)
// 09 LOGICAL STATEMENTS

// 10 CONDITIONALS (IF-ELSE)
// 11 CONDITIONALS (ELSE-IF)
// 12 SWITCH-CASE
// 13 LOOPS-1 (WHILE LOOP)
// 14 LOOPS-2 (DO-WHILE LOOP)
// 15 LOOPS-3 (FOR LOOP)
// 16 EXAMPLE PROGRAM: FIBONACCI SERIE (FOR LOOP)
// 17 EXAMPLE PROGRAM: SUM OF GIVEN NUMBERS (BREAK)
// 18 EXAMPLE PROGRAM: SUM OF EVEN NUMBERS (CONTINUE)

// 19 ARRAYS-1 (Integer Arrays)
// 20 ARRAYS-2 (Float Arrays)
// 21 ARRAYS-3 (String Arrays)
// 22 ARRAYS-4 (Multi-Dimension Arrays)
// 23 EXAMPLE PROGRAM: BUILDING AN 3x5 MATRIX (ARRAYS)

// 24 FUNCTIONS-1
// 25 FUNCTIONS-2 (Summation & Factorial Functions)
// 26 FUNCTIONS-3 (Prime Number Detection)
// 27 FUNCTIONS-4 (Arrays as parameter)
// 28 FUNCTIONS-5 (Strings as parameter)

// 29 POINTERS-1 (INTRODUCTION)
// 30 POINTERS-2
// 31 POINTERS-3 (Call By Value)
// 32 POINTERS-4 (Call By Reference)

// 33 ARRAYS & POINTERS
// 34 EXAMPLE PROGRAM: MAX FINDER BY ARRAY POINTER
// 35 STRINGS & POINTERS
// 36 FUNCTIONS WITH POINTER RETURN
// 37 POINTER ARRAYS (ARRAYS THAT STORE POINTERS)
// 38 EXAMPLE PROGRAM: BUBBLE SORTING

// 39 STRUCTURES-1
// 40 STRUCTURES-2
// 41 NESTED STRUCTURES
// 42 ARRAY STRUCTURES
// 43 FUNCTIONS & STRUCTURES
// 44 POINTERS & STRUCTURES
// 45 CALL BY REFERENCE IN STRUCTURES

// 46 FILES-1: fopen function
// 47 FILES-2: fputc function
// 48 FILES-3: fputs function


// -------------------------------------------------- //
// 01 HELLO WORLD!
#include <iostream>

int main() 
{
  std::cout << "Hello world, I am ready for C++";
  return 0;
}



// 02 NAMESPACE
/*Use the namespace keyword to simplify typing*/
#include <iostream>

using namespace std;
int main()
{
 cout << "Hey, writing std:: is pain, ";
 cout << "change the program so I don't have to write it.";
 return 0;
}


// 03 PRINT VARIABLES
/*GOAL: Practice writing to the console and learn 
**the variables types available in C++
**Print the sizes of each variable to the console.
**Print them in the following order:
**int, short, long, char, float, double, bool
*/
#include <iostream>

int main()
{
 using namespace std;
 cout<<"int size = "<<sizeof(int)<<"\n";
 cout<<"short size = "<<sizeof(short)<<"\n";
 cout<<"long size = "<<sizeof(long)<<"\n";
 cout<<"char size = "<<sizeof(char)<<"\n";
 cout<<"float size = "<<sizeof(float)<<"\n";
 cout<<"double size = "<<sizeof(double)<<"\n";
 cout<<"bool size = "<<sizeof(bool)<<"\n";
 return 0;
}

// 04 FORMATTING THE OUTPUT
/*Formatting Output 
**Goal: practice using cout to format output to console
**Print the variables in three columns:
**Ints, Floats, Doubles
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int a = 45;
    float b = 45.323;
    double c = 45.5468;
    int aa = a + 9;
    float bb = b + 9;
    double cc = c + 9;
    int aaa = aa + 9;
    float bbb = bb + 9;
    double ccc = cc + 9;

    cout << "Ints" << setw(13) << "Floats" << setw(15) << "Doubles" << "\n";
    cout << a  << setw(15) << b << setw(15) << c << "\n";
    cout << aa << setw(15) << bb << setw(15) << cc <<"\n";
    cout << aaa << setw(15) << bbb << setw(15) << ccc << "\n";
        
    return 0;
}


// 05 FILE IO
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
    string line;
    //create an output stream to write to the file
    //append the new lines to the end of the file
    ofstream myfileI ("input.txt", ios::app);
    if (myfileI.is_open())
    {
        myfileI << "\nI am adding a line.\n";
        myfileI << "I am adding another line.\n";
        myfileI.close();
    }
    else cout << "Unable to open file for writing";

    //create an input stream to read the file
    ifstream myfileO ("input.txt");
    //During the creation of ifstream, the file is opened. 
    //So we do not have explicitly open the file. 
    if (myfileO.is_open())
    {
        while ( getline (myfileO,line) )
        {
            cout << line << '\n';
        }
        myfileO.close();
    }

    else cout << "Unable to open file for reading";

    return 0;
}


// 06 POINTERS
/*  & -> for adress
    * -> value for that adress
*/    
int myVal = 5;
std::cout << "&a";   //where is a?

int * pointerToA = &a;
std::cout << * pointerToA;


// 07 ARRAYS
// variableType arrayName[] = {vars to be stored};
// variableType arrayName [arraysize]

// Multi-Dimensional Array
// typeOfVariable arrayName[size of dim.1][size of dim.2]...;

// Example
int array2Dimensions[2][3];             //declaration
int array2Dim[2][3] = {0,1,2,3,4,5};    //definition
for (int i=0; i<2;  i++)
    for (int j=0; j<3; j++)
        std::cout <<"array2Dim["<<i<<"]["<<j<<"]= " <<array2Dim[i][j] <<"\n";


// 08 FUNCTIONS
/* Format
returnedVariableType functionName (param1, ... ,paramN)
{
    statement(s);
}
*/
//Example
void printMessage()
{
    std::cout << "Hello world!";
}


// 09 IF-STATEMENTS
#include<iostream>

int main()
{
    std::cout<<"This program checks the value of a.\n";
    int a = 10;

    if(a == 0)
    {
        std::cout << "a is equal to 0!\n";
    }
    else
    {
        std::cout << "a is NOT equal to 0!\n";
    }
    return 0;
}


// 10 SWITCH STATEMENTS
/*Goal: demonstrate use cases for the switch statement.*/

#include <iostream>

int main()
{
    int menuItem = 1;
    
    std::cout<<"What is your favorite winter sport?: \n";
    std::cout<<"1.Skiing\n2: Sledding\n3: Sitting by the fire";
    std::cout<<"\n4.Drinking hot chocolate\n";
    std::cout<<"\n\n";
    
    switch(menuItem)
    {
        case(1): std::cout<<"Skiing?! Sounds dangerous!\n";
                 break;
        case(2): std::cout<<"Sledding?! Sounds like work!\n";
                 break; 
        case(3): std::cout<<"Sitting by the fire?! Sounds warm!\n";
                 break;
        case(4): std::cout<<"Hot chocolate?! Yum!\n";
                 break;
        default: std::cout<<"Enter a valid menu item";
    }
    
    char begin;
    std::cout<<"\n\nWhere do you want to begin?\n";
    std::cout<<"B. At the beginning?\nM. At the middle?";
    std::cout<<"\nE. At the end?\n\n";
    begin = 'M';  
    
    switch(begin)
    {
        case('B'): std::cout<<"Once upon a time there was a wolf.\n";
        case('M'): std::cout<<"The wolf hurt his leg.\n";
        case('E'): std::cout<<"The wolf lived happily everafter\n";
    }
    return 0;
}


// 11 FOR LOOPS
// TYPE.1 -> for ( declaration : range ) statement;
// TYPE.2 -> for (initialization; condition; increase) statement;

//Example
#include <iostream>
int main()
{
    float input;
    float sum = 0;

    for(int i=0; i<5; i++)
    {
        std::cout<<"What is the next number?\n";
        std::cin>>input;
        sum = sum + input;
    }//end of for loop

    std::cout<<"Sum = "<<sum<<"\n";
    std::cout<<"Average = "<<sum/5<<"\n";
    return 0;
}

// 11 FOR LOOPS





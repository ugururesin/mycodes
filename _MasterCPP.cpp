
// WELCOME TO C++  PROGRAMMING! - 2019

/* This Code is Written By Ugur Uresin
For training purposes! */

// CONTENT
// 01 HELLO WORLD!
// 02 NAMESPACE
// 03 PRINT VARIABLES
// 04 FORMATTING THE OUTPUT
// 05 FILE IO
// 06 POINTERS
// 07 ARRAYS
// 08 FUNCTIONS
// 09 IF-STATEMENTS
// 10 SWITCH STAT
// 12 FOR LOOPS
// 13 EXITING LOOPS
// 14 CLASSES


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


// 12 FOR LOOPS
// REGULAR WHILE LOOP
while(condition)
{
     statements;
}

// DO ... WHILE LOOP
do
{
     statements;
}while(condition );

//Example
#include <iostream>
int main()
{
    int count = 0;
    //This do..while loop will execute until count =5
    do
    {
        std::cout<<"Count = "<<count<<"\n";
        count++;
    }while(count < 5);


    int otherCount = 6; 
    //This do..while loop will execute once. Even though
    //otherCount > 5
    do
    {
        std::cout<<"othercount = "<<otherCount<<"\n";
        otherCount++;
    }while(otherCount < 5);
    
    return 0;
}


// 13 EXITING LOOPS
#include<iostream>

int main()
{
    int a = 0;
    while(a < 5)
    {
        std::cout<<"a = "<<a<<"\n";       
        a++;
        if(a == 3)
            break;
    }
    std::cout<<"The first statement after the first while loop\n\n";
    
    
    while(a < 15)
    {
        a++;
        if(a == 10)
        {
            std::cout<<"\tWhen a=10, go back to the top of the loop";
            std::cout<<"\n\tThis means a=10 is skipped.\n";
            continue;
        }
        std::cout<<"After continue a = "<<a<<"\n";           
    }
    return 0;
}



// 14 CLASSES
/*Now let's add the setName function
(functions in classes are also called methods) to our Student class.
Recall the default for members in a class is private.
We want the access functions to be public.
So we add the keyword "public" and all members listed
after it are accessible*/
class Student
{
        string name;
        int id;
        int gradDate;

    public:
        void setName(string nameIn);
        void setId(int idIn);
        void setGradDate(int dateIn);
        
        string getName();
        int getId();
        int getGradDate();
        
        void print();
};





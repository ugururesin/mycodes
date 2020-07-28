
// WELCOME TO C-PROGRAMMING! - 2019
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
// 01 DATA TYPES & FORMATS

// Single line comment

/* Multiple lines comment
	Comment-1
	Comment-2
*/

#include <stdio.h> // standard library!
#include <conio.h> // for getch();

int main() {
	
	/* DATA TYPES
		%d ---> integers
		%f ---> floats (6 digits by default eg. 4.200000)
		%c ---> char
		%s ---> string
		%.1f ---> 1 digit after comma
	*/

	int a1 = 42;
	char b1 = 66; //66 in ASCII: B
	char b2 = 'B';
	float c1 = 4.2;
	double d1 = 0.21;

	printf("%d %c %d %.1f %.2f %S\n",a1,b1,b2,c1,d1,“Hello World” );
	// 42 B 66 4.2 0.21 Hello World

	
	// HOW MANY BYTES ???
	printf("%d byte\n", sizeof(char));		//1 byte
	printf("%d byte\n", sizeof(int));		//4 byte
	printf("%d byte\n", sizeof(short int));	//2 byte
	printf("%d byte\n", sizeof(long int));	//4 byte
	printf("%d byte\n", sizeof(float));		//4 byte
	printf("%d byte\n", sizeof(double));	//8 byte

	getch(); //to keep the screen open in an older OS than WIN8!
	return 0;
}


// -------------------------------------------------- //
// 02 ARITHMETIC OPERATIONS
#include <stdio.h>

int main() {
	/* ARITHMETIC OPERATORS
		x+y ---> sum
		x-y ---> extract
		x*y ---> product
		x/y ---> division

		x%y ---> modulus

		+x ---> x * (+1)
		-x ---> x * (-1)
	*/

	int x1 = 1;
	int x2 = -1;

	printf("%d\n", 3+2);	//5
	printf("%d\n", 3-2);	//1
	printf("%d\n", 3*2);	//6
	printf("%d\n", 3/2);	//1 (%d is given, %f should be used!)
	printf("%d\n", 3%2);	//1

	printf("%d\n", -x1);	//-1
	printf("%d\n", -x2);	//1

	return 0;
}


// -------------------------------------------------- //
// 03 ARITHMETIC STATEMENTS
#include <stdio.h>

int main(){

	/* ARITHMETIC ORDER
		(+) (-) (-x,+x)		//1st priority! From right to left
		* / %				//2nd priority! From left to right
		+ - 				//3rd priority! From left to right

		In paranthesis is first!
	*/

	printf("%d\n",2*3-4);	//2
	printf("%d\n",2-3/4);	//2
	printf("%d\n",2+3%4);	//5
	printf("%d\n",2/3*4);	//0
	printf("%d\n",2%3/4);	//0

	return 0;
}


// -------------------------------------------------- //
// 04 APPOINTMENT, INCREASE, DECREASE
#include <stdio.h>

int main()
{
	/* 
	APPOINTMENT Examples:
	int x = 5;
	x = y; 
	x = y+1;

	INCREASE & DECREASE:
	i = i+1; 
	i +=1;
	
	++i; //prefix
	i++; //postfix

	Example:
	int i=4;
	printf("%d", i++ ); //Ekranda 4 gözükür! Sonra arttırır!
	printf("%d", ++i ); //Önce arttırır! Ekranda 5 gözükür!

	"iç-içe atamalar"
	i = j = k = 0;

	i = i % a;
	i %= a;

	*/

	return 0;
}

// -------------------------------------------------- //
// 05 TYPE TRANSFORMATIONS
#include <stdio.h>

int main()
{
	/*
	AUTOMATIC TRANSFORMATION EXAMPLE:
	3.6/2 operation: float/int
	It becomes 3.6/2.0 thus int (2) -> float (2.0)

	AUTOMATIC TRANSFORMATION TABLE:
	char
	short -> int -> float -> double -> long
										double

	MANUEL TRANSFORMATION EXAMPLE:
	int 3.2 ---> 3 (float to int)
	*/

	int x = 3;
	float y = 0.1;

	printf("%f\n", x/y); 		//30.000000
	printf("%f\n", 2*4.2);		//8.400000
	printf("%f\n", 12.5/2);		//6.250000
	printf("%d\n",(int)3.2);	//3
	printf("%f\n", (float)3);	//3.000000

	return 0;
}


// -------------------------------------------------- //
// 06 INPUT/OUTPUT FUNCTIONS
#include <stdio.h>
#define	PI = 3.14	//It has to be before main in C! (Not in C++)

int main()
{
	int radius;
	float volume;

	printf("Enter the value of the radius:");
	//scanf gets a value and assign to a variable (here radius)!
	scanf("%d", &radius);

	volume = (4/3.0)*PI*(radius*radius*radius);

	printf("The volume of the sphere is %.2f\n", volume);

	return 0;
}


// -------------------------------------------------- //
// 07 EXAMPLE PROGRAM: AVERAGE CALCULATOR (SCANF)
#include <stdio.h>

int main()
{
	int a,b,c,d,e; //Same type of variables can be defined in a line!
	float average;

	printf("Enter 5 numbers:");
	scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
	average = (a+b+c+d+e)/5.0;

	printf("The avarage of the given numbers is: %.2f\n",average);

	return 0;
}


// -------------------------------------------------- //
// 08 EXAMPLE PROGRAM: PARABOLA ROOT CALCULATOR (SCANF)
#include <stdio.h>
#include <math.h>	//for sqrt function

int main()
{
	int a,b,c; //Same type of variables can be defined in a line!

	printf("Enter the a value of the parabola:");
	scanf("%d", &a);
	printf("Enter the b value of the parabola:");
	scanf("%d", &b);
	printf("Enter the c value of the parabola:");
	scanf("%d", &c);
	
	delta = b*b - 4*a*c;

	x1 = -b + (sqrt(delta))/(2*a);
	x2 = -b - (sqrt(delta))/(2*a);

	printf("The first root is %.2f and the second root is %.2f\n",x1,x2);

	return 0;
}


// -------------------------------------------------- //
// 09 LOGICAL STATEMENTS
// logical not:	!
// logical and: &&
// logical or:	||
// Comparisons: >, <, >=, <=, !=, ==

#include <stdio.h>

int main()
{
	int a=1;
	int b=2;
	int c=3;
	int d=4;

	a >c && c <=d && (a >b || b <d) //False!

	return 0;
}


// -------------------------------------------------- //
// 10 CONDITIONALS (IF-ELSE)
// Here there is a new data type: bool (true/false)

/* Conditional Statements !!!
	Example:
	a = x >y ? x:y;
	If x >y is true (e.g. 10>4) then a=x!
	If x >y is false (e.g. 3>4) then a=y!
	*/ 

#include <stdio.h>

// EXAMPLE-1
int main()
{
	int note;

	printf("Enter your note:");
	scanf("%d", &note);

	if (note>60){

		printf("Congrats! You passed!");
	}
	else {
		printf("You failed! Study again!");	
	}

	return 0;
}

// EXAMPLE-2
int main()
{
	int midterm1, midterm2, final;
	float avarage;

	printf("Enter midterm1:");
	scanf("%d", &midterm1);
	printf("Enter midterm2:");
	scanf("%d", &midterm2);
	printf("Enter final:");
	scanf("%d", &final);

	avg = (midterm1+ midterm2+ final)/3.0;

	/* If single line codes are used in if-else
		No need to use curly brackets {} ! */
	if (avg>60)	printf("Congrats! You passed!");
	else 	printf("You failed! Study again!");

	return 0;
}


// -------------------------------------------------- //
// 11 CONDITIONALS (ELSE-IF)
#include <stdio.h>

// EXAMPLE-1
int main()
{
	int midterm1, midterm2, final;
	float avarage;

	printf("Enter midterm1:");
	scanf("%d", &midterm1);
	printf("Enter midterm2:");
	scanf("%d", &midterm2);
	printf("Enter final:");
	scanf("%d", &final);

	avg = (midterm1+ midterm2+ final)/3.0;

	if (avg>60) {
		printf("Congrats! You passed!");
	}
	else if (avg>50) {
		printf("Take the make-up exam!");
	}
	else {
		printf("You failed!");
	}

	return 0;
}

// EXAMPLE-2
int main()
{
	int midterm1, midterm2, final;
	float avarage;
	float gpa;

	printf("Enter midterm1:");
	scanf("%d", &midterm1);
	printf("Enter midterm2:");
	scanf("%d", &midterm2);
	printf("Enter final:");
	scanf("%d", &final);
	printf("Enter GPA:");
	scanf("%f", &gpa);

	avg = (midterm1*3/10.0+ midterm2*3/10.0+ final*4/10.0);

	if (avg>90) {
		printf("Your grade is AA and the average is %f",avg);
	}
	else if (avg>=85 && avg<90) {
		printf("Your grade is BA and the average is %f",avg);
	}
	else if (avg>=80 && avg<85) {
		printf("Your grade is BB and the average is %f",avg);
	}
	else if (avg>=75 && avg<80) {
		printf("Your grade is CB and the average is %f",avg);
	}
	else if (avg>=70 && avg<75) {
		printf("Your grade is CC and the average is %f\n",avg);
		if (gpa < 2.5){
			printf("Recommended that you take the lesson again!");
		}
	}
	else if (avg>=65 && avg<70) {
		printf("Your grade is DC and the average is %f\n",avg);
		if (gpa < 2.5){
		printf("Recommended that you take the lesson again!");
		}
	}
	else if (avg>=60 && avg<65) {
		printf("Your grade is DD and the average is %f\n",avg);
		if (gpa < 2.5){
		printf("Recommended that you take the lesson again!");
		}
	}
	else {
		printf("Your grade is FF and the average is %f\n",avg);
		printf("You failed from this lesson!");
	}

	return 0;
}


// -------------------------------------------------- //
// 12 SWITCH CASE
/* FORMAT:
	switch (operation) {
		case:
			operations;
			break;
		case:
			operations;
			break;
		case:
			operations;
			break;
	}

	// switch continues to enter the cases till reaches a 'break'!
	*/
#include <stdio.h>

int main()
{
	int transaction;
	int balance=1000;
	int amount;

	printf("Operations\n1:Cash Withdrawal\n2:Deposit\n3:Transfer\n4:Balance Inquiry\n5:Cancel\n\n\n");
	printf("Select the transaction:");
	scanf("%d",transaction);

	switch (transaction) {
		case 1:
			printf("Your balance is: %d\n",balance);
			printf("Enter the withdrawal amount:");
			scanf("%d",withdrawal);
			if (withdrawal > balance) {
				printf("Not enough balance!\n");
				break;
			}	
			balance -= withdrawal
			printf("Your new balance is: %d\n",balance);
			break;

		case 2:
			printf("Your balance is: %d\n",balance);
			printf("Enter the deposit amount:");
			scanf("%d",deposit);
			balance += deposit;
			printf("Your new balance is: %d\n",balance);
			break;

		case 3:
			printf("Your balance is: %d\n",balance);
			printf("Enter the transfer amount:");
			scanf("%d",transfer);
			if (transfer > balance){
				printf("Not enough balance!\n");
			}
			balance -= transfer
			printf("Your new balance is: %d\n",balance);
			break;
		
		case 4:
			printf("Your balance is: %d\n",balance);
			break;
		
		case 5:
			printf("Please take your card!\n");
			break;

		default:
			printf("Invalid operation!\n", ); 
			break;
	}

	return 0;
}


// -------------------------------------------------- //
// 13 LOOPS-1 (WHILE LOOP)
#include <stdio.h>

int main()
{
	int i;
	i = 0;

	while(i <10) {
		printf("Line number: %d\n",i);
		i++;
	}
	printf("In %dth step, while loop is over\n",i);
	
	return 0;
}

//EXAMPLE-1 (FACTORIAL CALCULATOR)
int main()
{
	int n;
	int factorial = 1;

	printf("Enter a number to calculate it's factorial:");
	scanf("%d",n);

	while(n !=0){
		factorial = factorial * n;
		n --;
	}
	printf("The factorial is %d\n",factorial);
	
	return 0;
}


// -------------------------------------------------- //
// 14 LOOPS-2 (DO-WHILE LOOP)
// DO-WHILE is not preferred in general!*
#include <stdio.h>
int main()
{
	int n=5;

	do {
		printf("%d\n",n);
		n--;
	}
	while(n>0);
	// 5 4 3 2 1 (in the new lines!)

	/* ATTENTION
	if n=0 initially,
	it prints 0 as well although while(n>0)!!!
	That's why this is not preferred in general!*
	*/
	
	return 0;
}

//EXAMPLE-1 (SUM OF DIGITS)
int main()
{
	int n, digits=0, sum=0;
	printf("Enter an integer value:");
	scanf("%d",&n)

	do{
		sum += (n %10); //to get the last digit
		digits++;
		n = n/10; //to drop the last digit

	}
	while(n>0);

	printf("Sum of the digits:%d &The number of digits:%d\n",sum,digits);

	return 0;
}


// -------------------------------------------------- //
// 15 LOOPS-3 (FOR LOOP)
/* FORMAT:
	for(start value; end value; increment){
		do something
	}
	*/
#include <stdio.h>

int main()
{
	int i;

	for(i=0; i <5; i++){
		printf("%d\n",i);
	}
	// 0 1 2 3 4

	return 0;
}

//EXAMPLE-1
int main()
{
	int i;
	int j;

	for(i=0, j=1; i<10 && j<5; i++, j++){
		printf("i:%d j:%d\n",i,j);
	}
	/* Result:
		i:0 j:1
		i:1 j:2
		i:2 j:3
		i:3 j:4
		*/ 
	return 0;
}

//EXAMPLE-2
int main()
{
	int i;
	int j;

	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			printf("i:%d j:%d\n",i,j);
		}
	}
	/* Result:
		i:0 j:0
		i:0 j:1
		i:0 j:2
		i:1 j:0
		i:1 j:1
		i:1 j:2
		i:2 j:0
		i:2 j:1
		i:2 j:2
		*/ 
	return 0;
}


// -------------------------------------------------- //
// 16 EXAMPLE PROGRAM: FIBONACCI SERIE (FOR LOOP)
// Fibonacci Serie: 1 1 2 3 5 8 13 21 34...
#include <stdio.h>

int main()
{
	int firstnumber = 1;
	int secondnumber = 1;
	int i;

	printf("%d\n%d\n",firstnumber,secondnumber);

	for(i=0; i <12; i++){

		int temp = secondnumber;
		secondnumber += firstnumber;
		firstnumber = temp;

		printf("d\n", secondnumber);
		// 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
	}

	return 0;
}


// -------------------------------------------------- //
// 17 EXAMPLE PROGRAM: SUM OF GIVEN NUMBERS (BREAK)
#include <stdio.h>

int main()
{

	/* This program sums the given numbers
		until the user enters a specific value (-1) */

	int sum = 0;
	int i;
	int value;

	for(i =0; true; i++){
		printf("Enter a value: (Enter -1 to exit)");
		scanf("%d",&value);

		if (value == -1){
			break;
		}	

		sum += value;
	}

	return 0;
}


// -------------------------------------------------- //
// 18 EXAMPLE PROGRAM: SUM OF EVEN NUMBERS (CONTINUE)
#include <stdio.h>

//WAY-1 (FOR LOOP)
int main()
{
	int sum = 0;
	int i;

	for(i =1; i <=10; i++){

		if (i %2 ==1) { //Odd number!
			continue; 	//Skip the below code! (However i++ works in for!)
		}

		sum += i;
	}
	printf("%d\n",sum);

	return 0;
}

//WAY-2 (WHILE LOOP)
int main()
{
	int sum = 0;
	int i = 0;

	while(i <=10){

		if (i %2 ==1) { //Odd number!
			i++;		//Must be here otherwise infinite loop occurs!
			continue; 	//Skip the below code! (However i++ works in for!)
		}

		sum += i;
	}
	printf("%d\n",sum);

	return 0;
}


// -------------------------------------------------- //
// 19 ARRAYS-1 (Integer Arrays)
#include <stdio.h>
// Stores many values of the same data type! 

int main()
{
	int values[] = {1,2,3,4,5}; //index start with 0!

	printf("%d\n",values[0]); 	//gives 1!
	printf("%d\n",values[2]); 	//gives 3!

	//printing the all values of an array!
	for (int i = 0; i <5; ++i)
	{
		printf("%d\n",values[i]); //1 2 3 4 5
	}

	return 0;
}


// -------------------------------------------------- //
// 20 ARRAYS-2 (Float Arrays)
#include <stdio.h>

int main()
{
	float sum = 0.0;
	float values[5];	//can take 5 values!
	int i;

	for (int i = 0; i <5; i++){

		printf("Enter a value:");
		scanf("%f",&values[i]);
	}

	for (int i = 0; i < count; ++i){

		sum += values[i];
	}

	printf("The average of the given numbers is %.2f",sum/5);
	

	return 0;
}


// -------------------------------------------------- //
// 21 ARRAYS-3 (String Arrays)
#include <stdio.h>

int main()
{
	char name[20];

	printf("Enter a name:");
	scanf("%s",name);				//scanf can't take after space!
	printf("Enter a name: %s",name);

	return 0;
}


// -------------------------------------------------- //
// 22 ARRAYS-4 (Multi-Dimension Arrays)
#include <stdio.h>

int main()
{
	/* Example: (2D-Array) 
		1 2 3	//0th row
		4 5 6	//1st row
		7 8 9	//2nd row
	*/

	int matrix[3][3] = {{1,2,3},{4,5,6},{7,8,9}};

	printf("%d\n",matrix[1][1]);	//gives 5!
	printf("%d\n",matrix[2][2]);	//gives 9!

	// building a matrix!
	int i,j;
	for (int i = 0; i < 3; i++)
	{
		scanf("%d",&matrix[i][j]);
	}

	// printing a matrix!
	int i,j;
	for (int i = 0; i < 3; i++)
	{
		printf("%d ",matrix[i][j]);
	}
	printf("\n");

	return 0;
}


// -------------------------------------------------- //
// 23 EXAMPLE PROGRAM: BUILDING AN 3x5 MATRIX (ARRAYS)
#include <stdio.h>

int main()
{
	/*
	1 2 3 4 5 
	6 7 8 9 10 
	11 12 13 14 15 

	Column Sums:
	18 21 24 27 30
	*/


	int matrix[3][5];
	int i,j;

	//building a matrix from entered values:
	for (int i = 0; i <3; i++)
	{
		for (int j = 0; j <5; j++) {
			scanf("%d",&matrix[i][j]);
		}
	}

	//printing the matrix from entered values:
	for (int i = 0; i <3; i++)
	{
		for (int j = 0; j <5; j++) {
			printf("%d ",matrix[i][j]);
		}
		printf("\n");
	}

	//summing the columns:
	int sum;
	for (int j = 0; j <5; j++)
	{
		for (int i = 0; i < 3; i++) {
			sum += matrix[i][j];
		}
		printf("%d ",sum);
		sum = 0;
	}

	return 0;
}


// -------------------------------------------------- //
// 24 FUNCTIONS-1
/*
	Function definition

	returntype functionname(parameters){
		////// function block

		operations
	}
*/

#include <stdio.h>

void  errorprint(int error){	//if no return output -> void!

	printf("Error code is %d\n",error);
}

int main()
{
	errorprint(404); //gives "Error code is 404"
	
	int value;
	printf("Please enter a non-negative number!:");
	scanf("%d",&value);

	if(value < 0) {
		errorprint(404);
	}
	else {
		printf("Congrats!");
	}

	return 0;
}


// -------------------------------------------------- //
// 25 FUNCTIONS-2 (Summation & Factorial Functions)
#include <stdio.h>

// EXAMPLE-1: Summation Function
int sumfunction(int value1, int value2) {
	return (value1+value2);
}

int main()
{
	int value1;
	int value2;

	scanf("%d %d",&value1, &value2);
	printf("Sum is %d\n",sumfunction(value1,value2));

	return 0;
}

// EXAMPLE-2: Factorial Function
int factorial(int value) {
	int fact=1;

	for (; value>0; value--) {

		fact *= value;
	}
	return fact;
}

int main()
{
	int n;
	printf("Enter a value to calculate it's factorial:");
	scanf("%d",&n);

	printf("Factorial is %d",factorial(n));

	return 0;
}


// -------------------------------------------------- //
// 26 FUNCTIONS-3 (Prime Number Detection)
#include <stdio.h>

int is_prime(int value) {

	int i;
	for (int i = 2; i <value; i++) {
		if (value %i == 0){
			return 0;
		}
	}
	return 1;
}

int main()
{
	int n;
	printf("Enter a value:");
	scanf("%d",&n);

	if (is_prime(n) == 0) {
		printf("Not a prime number!");
	}
	else {
		printf("It's a prime number!");	
	}

	return 0;
}


// -------------------------------------------------- //
// 27 FUNCTIONS-4 (Arrays as parameter)
#include <stdio.h>

void print_it(int matrix[][4], int size) { //2nd dim (4) must be given!

	int i,j;

	for (int i = 0; i <size; ++i) {

		for (int j = 0; j <4; j++) {
			printf("%d ",matrix[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	int matrix[3][4];
	int i,j;
	
	printf("Fill the matrix:");

	for (int i=0; i <3; i++) {

		for (int j=0; j <4; j++) {

			scanf("%d", &matrix[i][j]);
		}
	}

	print_it(matrix,3);
}


// -------------------------------------------------- //
// 28 FUNCTIONS-5 (Strings as parameter)
#include <stdio.h>
#include <string.h> //There is a function for that strlen()

int length_char(char name[]) {
	int length_char = 0;
	int i;
	
	/*
	C puts an \0 at the and of a char
	so as to define the end of a char!
	e.g. 'Tom' = 'T' 'o' 'm' '\0'
	*/

	for (i=0; name[i] != '\0'; i++) { 
		length_char++;
	}

	return length_char;
}
int main()
{
	char name[] = "Michael";

	printf("%d",length_char(name));

	return 0; //returns 7 for 'Michael'
}


// -------------------------------------------------- //
// 29 POINTERS-1 (INTRODUCTION)
#include <stdio.h>

// & gives the adress information!
// * gives the value in the adress!

// p represents the adress id
// u provides a better visualization!

int main()
{
	int i = 5; 		//variable i is assigned

	int *p = &i;	//p is a pointer and hold the adress of i

	printf("%p\n",p);	//gives the real adress of i (0x7ffed05411d8)
	printf("%d\n",*p); //gives the value in the adress (5)!

	return 0;
}


// -------------------------------------------------- //
// 30 POINTERS-2
#include <stdio.h>

int main()
{

	int 	a = 5,*ap;
	float 	b = 3.2,*bp;
	double 	c = 3.412,*cp;
	char 	d = 'a', *dp;

	int values[5] = {1,2,3,4,5};
	int *arrayp;

	ap = &a;
	bp = &b;
	cp = &c;
	dp = &d;

	arrayp = &values[1];

	printf("The int value in the adress %p is %d\n",ap,*ap);
	printf("The float value in the adress %p is %f\n",bp,*bp);
	printf("The double value in the adress %p is %lf\n",cp,*cp);
	printf("The char value in the adress %p is %c\n",dp,*dp);
	printf("The array values in the adress %p is %d\n",arrayp,*arrayp);

	return 0;
}

/* Results with %p
The int value in the adress 0x7fff2e99f118 is 5
The float value in the adress 0x7fff2e99f10c is 3.200000
The double value in the adress 0x7fff2e99f0f8 is 3.412000
The char value in the adress 0x7fff2e99f0ef is a
The array values in the adress 0x7fff2e99f0c4 is 2
*/

/* Results with %p
The int value in the adress 3184108872 is 5
The float value in the adress 3184108860 is 3.200000
The double value in the adress 3184108840 is 3.412000
The char value in the adress 3184108831 is a
The array values in the adress 3184108788 is 2
*/


// -------------------------------------------------- //
// 31 POINTERS-3 (Call By Value)
#include <stdio.h>
/* In the following function
	values are exchanged!
	However, a & b are local variables!
	Here, only values of x & y are copied!
	Thus, only values are called!
	Outside of the function, there is no a & b.
*/
void value_exchange(int a, int b) {
	int temp = a;
	a = b;
	b = temp;

	printf("a:%d b:%d\n",a,b);
}

int main()
{
	int x=5, y=10;
	value_exchange(x,y); 		//in function a=10, b=5
	printf("x:%d y:%d\n",x,y);	//however here x=5, y=10 (unchanged!)

	return 0;
}


// -------------------------------------------------- //
// 32 POINTERS-4 (Call By Reference)
#include <stdio.h>

void value_exchange(int a, int b) {
	int temp = *a;
	*a = *b;
	*b = temp;

	printf("a:%d b:%d\n",a,b);
}

int main()
{
	int x=5, y=10;
	value_exchange(&x,&y);		//in function a=10, b=5
	printf("x:%d y:%d\n",x,y);	//however here x=10, y=5 (changed!!!)


	return 0;
}


// -------------------------------------------------- //
// 33 ARRAYS & POINTERS
#include <stdio.h>

int main() {

	int values[5] = {1,2,3,4,5}; //reserves 5 places in the RAM!

	printf("%d\n",values[0]);	//1
	int *p = &values[0]; 		//the place where '1' is stored!
	//int *p = values;			//same with the upper! 1st adress of 'values' array!

	printf("%u\n",p);	//2174864176
	printf("%u\n",p+1);	//2174864180
	//the difference is '4' because an integer holds 4 bytes!

	return 0;
}

//Element call
int main() {

	int values[5] = {1,2,3,4,5}; //reserves 5 places in the RAM!

	int *p = values;			//same with the upper! 1st adress of 'values' array!

	printf("%d\n",p[0]); //1
	printf("%d\n",p[1]); //2
	printf("%d\n",p[2]); //3
	printf("%d\n",p[3]); //4
	printf("%d\n",p[4]); //5

	return 0;
}


// -------------------------------------------------- //
// 34 EXAMPLE PROGRAM: MAX FINDER BY ARRAY POINTER
#include <stdio.h>

//defining max function
int max(int a[], int length) {	//instead of a[], *a can be used to use pointers!!!
	int max_value = a[0];
	int i;

	for (i =1; i < length; i++) {
		if (a[i] > max_value) {
			max_value = a[i];
		}
	}

	return max_value;
}

int main()
{
	int values[5] = {3,5,25,10,15};
	int result = max(values, 5);

	printf("The maximum value in the array is: %d\n",result);
	//The maximum value in the array is: 25

	return 0;
}


// -------------------------------------------------- //
// 35 STRINGS & POINTERS
#include <stdio.h>
#include <string.h>	//for strlen() function

int main()
{
	char text[]= "head"; //RAM holds 'h' 'e' 'a' 'd' '\0'
	char *p = text;		//pointer holds the beginning adress of text!

	printf("%s \n",text);	//head
	printf("%s \n",p); 		//head
	printf("%s \n",p+1); 	//ead
	printf("%s \n",p+2); 	//ad

	printf("%d",strlen(text));	//4

	return 0;
}


// -------------------------------------------------- //
// 36 FUNCTIONS WITH POINTER RETURN
#include <stdio.h>
#include <string.h>
char *myfunc(char *p,int index) {

	int length = strlen(p);

	if (index > length) {
		return NULL;
	}
	else {
		return p+index;
	}

}

int main()
{
	char text[] = "software";
	char *p = myfunc(text,2); 

	if(p==NULL) {
		printf("Pointer NULL");
	}
	else {
		printf("%s",p); //ftware
	}

	return 0;
}


// -------------------------------------------------- //
// 37 POINTER ARRAYS (ARRAYS THAT STORE POINTERS)
#include <stdio.h>

char *dayname(char *daysarray[], int length, int whichday) {

	if (whichday >=1 && whichday <=7) {
		return daysarray[whichday-1];
	}
	else {
		return NULL;
	}
}

int main()
{
	char *days[7] = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"};

	char *p = dayname(days,7,5);

	if (p==NULL) {
		printf("NULL");
	}
	else {
		printf("%s\n",p); //friday
	}

	return 0;
}


// -------------------------------------------------- //
// 38 EXAMPLE PROGRAM: BUBBLE SORTING
#include <stdio.h>
#define MAX 50

void bublesort(int arr[], int size) {
	
	int i,j;

	for (i =0; i < size; i++) {
		for (j =1; j <size-i; j++) {
			if (arr[j-1] > arr[j]) {
				int temp = arr[j];
				arr[j] = arr[j-1];
				arr[j-1] = temp;
			}
		}
	}
}

int main()
{
	int array[MAX],size;
	int i;
	printf("Enter the size of the array:");
	scanf("%d ",&size);

	for (i =0; i < size; i++) {
		scanf("%d ",&array[i]);
	}

	bublesort(array,size);

	for (i =0; i < size; i++) {
		printf("%d ",array[i]);
	}
	
	return 0;
}


// -------------------------------------------------- //
// 39 STRUCTURES-1
#include <stdio.h>

struct Student{
	char name[15];
	char surname[15];

	int number;
	int age;
};

int main()
{
	struct Student robert = {"Robert","Jackson",2019501,22};
	printf("%s %s %d %d",robert.name,robert.surname,robert.number,robert.age);
	
	return 0;
}


// -------------------------------------------------- //
// 40 STRUCTURES-2
#include <stdio.h>

struct Vehicle{
	
	int num_wheels;
	int num_gears;
	int model;
	float engine;
	int horsepower;
}vehicle1,vehicle2;

int main()
{	
	//no need to type struct!
	vehicle1 = {0};	//a class in which all values are 0!
	vehicle2 = {4,7,2015,2.0,180}

	return 0;
}


// -------------------------------------------------- //
// 41 NESTED STRUCTURES
#include <stdio.h>
#include <string.h> //for strcpy()

struct Address {
	char state[15];
	char city[20];
	char street[15];
};

struct Student {
	char name[15];
	char surname[15];
	int number;
	int age;
	struct Address add;
};

int main()
{	
	struct Student stu1;

	//student1.name = "Thomas" <--- this code does not work!
	strcpy(stu1.name,"Thomas");
	strcpy(stu1.surname,"Jackson");
	stu1.number = 2018502;	
	stu1.age = 21;
	strcpy(stu1.add.state,"California");
	strcpy(stu1.add.city,"San Francisco");
	strcpy(stu1.add.street,"Broadway");

	printf("%s %s %d %d %s %s %s",stu1.name,stu1.surname,stu1.number,stu1.age,stu1.add.state,stu1.add.city,stu1.add.street);

	return 0;
}


// -------------------------------------------------- //
// 42 ARRAY STRUCTURES
#include <stdio.h>

struct Student {
	char name[15];
	char surname[15];
	int number;
};

int main()
{
	struct Student students[3];
	int i;

	for (i =0; i <3; i++) {
		printf("Enter the information of %dth student:\n",i+1);
		scanf("%s %s %d",&students[i].name,&students[i].surname,&students[i].number);
	}

	for (i =0; i <3; i++) {
		
		printf("The records of the %dth student: %s %s %d\n",i+1, students[i].name, students[i].surname, students[i].number);
	}

	return 0;
}



// -------------------------------------------------- //
// 43 FUNCTIONS & STRUCTURES
#include <stdio.h>

struct Student {
	char name[15];
	char surname[15];
	int number;
};
void show(struct Student a){
	printf("Student information: %s %s %d\n",a.name,a.surname,a.number);
};

int main()
{
	struct Student student1={"Tom","Bush",2018750};
	show(student1);

	return 0;
}

//EXAMPLE-1
#include <stdio.h>
struct Student {
	char name[15];
	char surname[15];
	int number;
};

void show(struct Student a){
	printf("Student information: %s %s %d\n",a.name,a.surname,a.number);
};

struct Student fillform() {

	struct Student new;
	printf("Enter the credentials:");
	scanf("%s %s %d",&new.name,&new.surname,&new.number);

	return new;
}

int main()
{
	struct Student student1=fillform();
	show(student1);

	return 0;
}


// -------------------------------------------------- //
// 44 POINTERS & STRUCTURES
/* The type of a pointer must be the same with the type of value!
	Example
	int a = 5;
	int *p = &a;

	Same is valid for the structures as well!
*/
#include <stdio.h>
#include <string.h> //for strcpy()

struct Student {
	char name[20];
	char surname[20];
	int number;
};

int main()
{
	struct Student *point;

	struct Student stud1;

	strcpy(stud1.name,"Thomas");
	strcpy(stud1.surname,"Jackson");
	stud1.number = 205;

	point = &stud1;

	printf("%s %s %d\n",stud1.name, stud1.surname, stud1.number);
	printf("%s %s %d\n",point->name, point->surname, point->number); //NEW NOTATION '->''

	return 0;
}


// -------------------------------------------------- //
// 45 CALL BY REFERENCE IN STRUCTURES
#include <stdio.h>
#include <string.h> //for strcpy()

struct Student {
	char name[20];
	char surname[20];
	int number;
};

void show(struct Student *p) {
	printf("Student's information\nName:%s\nSurame:%s\nNumber:%d\n",p->name, p->surname ,p->number);
}

int main()
{
	struct Student student1 = {"Tom","Blue",500};
	show(&student1);

	return 0;
	/*
	Student's information
	Name:Tom
	Surame:Blue
	Number:500
	*/
}


// -------------------------------------------------- //
// 46 FILES-1: fopen function
/* 
	fopen() function returns a pointer!
	fopen("file_name","open_mode")
		modes
			"w":write	(if there is no file, it creates)
			"r":read	(if there is no file, it return NULL)
			"a":append 	(if there is a file, it appends new content!)
			"w+":read & write
	
	fclose(filep);
	
	fputc(character, filep); //writes the character into the file!
*/
#include <stdio.h>

int main()
{
	FILE *filep = fopen("mytext.txt","w"); 

	if (filep == NULL) {
		printf("File is not created!");
	}
	else {
		printf("File is created");
	}

	return 0;
}


// -------------------------------------------------- //
// 47 FILES-2: fputc function
#include <stdio.h>
#include <string.h> 

int main()
{
	char data[25] ="Example text";
	int length = strlen(data);
	int i;

	FILE *filep = fopen("mytext.txt","w");

	if (filep == NULL) {
		printf("File is not created!");
	}
	else {
		for(i=0; i<length; i++) {

			fputc(data[i], filep);
			printf("The written character is %c\n",data[i]);	
		}
		printf("The file successfully is written!\n");
		/*
		The written character is E
		The written character is x
		The written character is a
		The written character is m
		The written character is p
		The written character is l
		The written character is e
		The written character is
		The written character is t
		The written character is e
		The written character is x
		The written character is t
		The file successfully is written!
		*/
	}
	return 0;
}



// -------------------------------------------------- //
// 48 FILES-3: fputs function
#include <stdio.h>
#include <string.h> 

int main()
{
	FILE *filep;
	char text[256];
	filep = fopen("edited_text.txt","a");

	if (filep == NULL) {
		printf("File is not created!");
	}
	else {
		printf("Write something: ");
		fgets(text,256,stdin);
		/*	scanf gets the input till space,
			fgets gets input till enter!!!
			fgets has 3 parameters: which_array, max_size, stdin (standard input)
		*/
		fputs(text,filep); //2 parameters: which_array, which_file
		printf("File is written!");
		fclose(filep);
		}
	return 0;
}

// -----------------END.OF.THIS.FILE----------------- // 
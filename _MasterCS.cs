// C# TEMPLATE
//----------------------------------------//

// MAIN
using System.IO;
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}

// VARIABLES
string Mystring;
Mystring = "Hello World!"; //or string Mystring="Hello World!"

char Mycharacter;
Mycharacter = 'A';

int Myinteger1, Myinteger2;
Myinteger1 = 2147483647;	//max positive integer
Myinteger2 = -2147483647;	//max negative integer

long Mylong1, Mylong2;
Mylong1 = 9223372036854775806;		//max positive long
Mylong2 = -9223372036854775806;		//min positive long

bool result;
result = true;


// PRINTING A VALUE
Console.WriteLine(Mystring);
Console.WriteLine(Mycharacter);
Console.WriteLine(Myinteger1);
Console.WriteLine(Myinteger2);
Console.WriteLine(Mylong1);
Console.WriteLine(Mylong2);
Console.WriteLine(result);


// DATETIME
//using System;
DateTime Now, Today;
Now = DateTime.Now;
Today = DateTime.Today;
Console.WriteLine("Now: " + Now);
Console.WriteLine("Today: " + Today);

string Detail;
Detail = "Today: "  + Today.ToString() + "\r\n";
Detail += "Day: "   + Today.Day.ToString() + "\r\n";
Detail += "Month: " + Today.Month.ToString() + "\r\n"; 
Detail += "Hour: "  + Today.Hour.ToString() + "\r\n";
Console.WriteLine(Detail);

Console.WriteLine(DateTime.Now.ToString("d")); 		//	3/27/2021
Console.WriteLine(DateTime.Now.ToString("D"));		//	Saturday, March 27, 2021
Console.WriteLine(DateTime.Now.ToString("f"));		//	Saturday, March 27, 2021 3:45 PM
Console.WriteLine(DateTime.Now.ToString("F"));		//	Saturday, March 27, 2021 3:45:30 PM
Console.WriteLine(DateTime.Now.ToString("g"));		//	3/27/2021 3:45 PM
Console.WriteLine(DateTime.Now.ToString("G"));		//	3/27/2021 3:45:30 PM
Console.WriteLine(DateTime.Now.ToString("t"));		// 	3:45 PM
Console.WriteLine(DateTime.Now.ToString("T"));		//	3:45:30 PM
Console.WriteLine(DateTime.Now.ToString("Y"));		//	March 2021
Console.WriteLine(DateTime.Now.ToString("M"));		//	March 27
Console.WriteLine(DateTime.Now.ToString("dd"));		//	27
Console.WriteLine(DateTime.Now.ToString("ddd"));	//	Sat
Console.WriteLine(DateTime.Now.ToString("dddd"));	// 	Saturday
Console.WriteLine(DateTime.Now.ToString("MM"));		//	03
Console.WriteLine(DateTime.Now.ToString("MMM"));	//	Mar
Console.WriteLine(DateTime.Now.ToString("MMMM"));	//	March
Console.WriteLine(DateTime.Now.ToString("yy"));		//	21
Console.WriteLine(DateTime.Now.ToString("yyy"));	//	2021
Console.WriteLine(DateTime.Now.ToString("hh"));		//	03
Console.WriteLine(DateTime.Now.ToString("HH"));		//	15
Console.WriteLine(DateTime.Now.ToString("mm"));		//	45
Console.WriteLine(DateTime.Now.ToString("ss"));		//	30
Console.WriteLine(DateTime.Now.ToString("ff"));		//	03
Console.WriteLine(DateTime.Now.ToString("fff"));	//	999	(miliseconds)


// STRING METHODS
string Mystring = " Hello World! ";

Console.WriteLine(Mystring.Length);			// 12 (NUMBER OF CHARACTERS)
Console.WriteLine(Mystring.ToLower());		// hello world!
Console.WriteLine(Mystring.ToUpper());		// HELLO WORLD!
Console.WriteLine(Mystring.Trim());			
Console.WriteLine(Mystring.TrimStart());
Console.WriteLine(Mystring.TrimEnd());
Console.WriteLine(Mystring.Trim());


// MATH OPERATORS
int num1 = 15, num2 = 30, max_value;
max_value = Math.Max(num1,num2);
Console.WriteLine(max_value);



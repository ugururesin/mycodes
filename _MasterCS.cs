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



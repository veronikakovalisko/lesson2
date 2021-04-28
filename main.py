"""
Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as
separate variables and then prints a message like this:

     “Good day <name>! <day> is a perfect day to learn some python.”


Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing res
"""
if __name__ == '__main__':
    name = input("Введіть ім'я")
    day = input("Введіть день")
    print(f"Good day {name}! {day} is a perfect day to learn some python. ")
    print("Good day {}! {} is a perfect day to learn some python. ".format(name, day))
"""
Task 2

Manipulate strings.

Save your first and last name as separate variables, then use string 
concatenation to add them together with a white space in between and print a greeting.
"""
if __name__ == '__main__':
    name = "nika"
    lastname = "kovalisko"
    print(f"Hello {name} {lastname}")
"""Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables a 
and b, then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division"""

if __name__ == '__main__':
    a = int(input("a="))
    b = int(input("b ="))
    print(f"a+b={a+b}")
    print(f"a-b={a-b}")
    print(f"a/b={a/b}")
    print(f"a*b={a*b}")
    print(f"а в степені б={a**b}")
    print(f"модуль {a//b}")
    print(f"a%b={a%b}")
    """
    (под звездочкой)

вариант задания осваивать форматирование строк. Заполните проч
ерк, чтобы получить вот такую ​​строку на выходе 

"000012 Василий 110110 32.10"

print («____________________». формат (12, «Василий», 54, 32.1))

(https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-33.php)

Попробуйте взять какое то одно слово в переменную и "собрать" из него другие слова.
Например взяли слово "Корован"  

s1 = "Корован"3


подумайте как вы из него вывести слово "ворона" (есть несколько вариантов)
    """
if __name__ == '__main__':
    print("0000{} {} {:b} {:.2f}".format(12, "Василь", 54, 32.1))
    s1 = 'Корован'
    print(s1[4:0:-1], s1[-1:4:-1], sep="")






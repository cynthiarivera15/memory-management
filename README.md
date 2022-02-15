# Project 2: Memory Management


University of Puerto Rico

Río Piedras Campus

Department of Computer Science

Student Name: Cynthia Marie Rivera Sánchez

Student Number: 801-19-5470

Course & Section: CCOM4017-002

## Contents of this file
* Description of the program
* Instructions on how to execute the program
* References used to perform the program

## Description
This project contains the following three files: ```lifo.py```, ```optimal.py``` and ```wsclock.py```.

The first file, ```lifo.py```, simulates the Last In First Out (LIFO) Page Replacement Algorithm. It will receive as an input the amount of pages the Physical Memory has and a file which contains a sequence of virtual page access requests. Then, it will start reading these requests and adding them in Physical Memory, if the Physical Memory is already full, then the last page added is going to be remove so it can be replace by the new one.

The second file, ```optimal.py```, simulates the Optimal Page Replacement Algorithm. It will receive as an input the amount of pages the Physical Memory has and a file which contains a sequence of virtual page access requests. Then, it will start reading these requests and adding them in Physical Memory, if the Physical Memory is already full, then it will remove from Physical Memory the page that will not be reference again or is the furthest away to being reference and replace it by the new one.

The third file, ```wsclock.py```, simulates the WSClock Page Replacement Algorithm. It will receive as an input the amount of pages the Physical Memory has, an interval of time which helps determine if a page forms part of the working set and a file which contains a sequence of virtual page access requests. Then, it will start reading these requests and adding them in Physical Memory, if the Physical Memory is already full, then it will remove from Physical Memory the page that is not reference and does not forms part of the working set. If all the pages are either reference or for part of the working set it will remove the page with the oldest time and replace it by the new one.

## Instructions
Each code will be execute it separately using ```python3```, for indications on how to execute a specific file read the indications below.

* ```lifo.py```:
Execution: To execute this file, the user has to put the file name in the command line along with a number that will indicate the amount of pages Physical Memory has room for and the name of the text file which simulates a sequence of virtual page access requests.

This code has two global variables, ```N``` which stores the amount of pages Physical Memory has room for and ```access_requests_list``` which is a list that stores the sequence of virtual page access requests. ```N``` will be receive as an input from the user, while ```access_requests_list``` will be done after the input file was read. Once the input file is read and the ```access_requests_list``` has the sequence of virtual page access requests, a while loop will go in until the last request is remove from the ```access_requests_list```. Inside that while loop, the first thing that will happen is that an object for a specific page will be created. After that, there is a function that will check if that page is or not inside of Physical Memory. If the page is inside Physical Memory, then the operation the page perform is going to be updated. If the page is not inside Physical Memory, then either two of the following things will happen. If the Physical Memory has room left, then the page is just going to be added to it, if it does not have room, then the last page added is going to be remove from Physical Memory so it can be replace with the new page.

* ```optimal.py```:
Execution: Just like the ```lifo.py``` file, to execute this file, the user has to put the file name in the command line along with a number that will indicate the amount of pages Physical Memory has room for and the name of the text file which simulates a sequence of virtual page access requests.

This code has two global variables, ```N``` which stores the amount of pages Physical Memory has room for and ```access_requests_list``` which is a list that stores the sequence of virtual page access requests. ```N``` will be receive as an input from the user, while ```access_requests_list``` will be done after the input file was read. Once the input file is read and the ```access_requests_list``` has the sequence of virtual page access requests, a while loop will go in until the last request is remove from the ```access_requests_list```. Inside that while loop, the first thing that will happen is that an object for a specific page will be created. After that, there is a function that will check if that page is or not inside of Physical Memory. If the page is inside Physical Memory, then the operation the page perform is going to be updated. If the page is not inside Physical Memory, then either two of the following things will happen. If the Physical Memory has room left, then the page is just going to be added to it, if it does not have room, then the ```access_requests_list``` will be evaluated to see which page in Physical Memory is never going to be requested again or will be the furthest away requested. After knowing that, if there is a page in Physical Memory that will never be requested again, then it will be removed and replace by the new one. On the contrary, if all the pages in Physical Memory are going to be requested in the future, then the furthest away is going to remove and replace by the new one.

* ```wsclock.py```:
Execution: To execute this file the user has to put the file name in the command line along with a number that will indicate the amount of pages Physical Memory has room for, another number which will help determine if a page forms part of the working set or not and the name of the text file which simulates a sequence of virtual page access requests.

This code has three global variables, ```N``` which stores the amount of pages Physical Memory has room for, ```position_pointer``` which function as index to know what page in Physical Memory is going to be evaluated first once the Physical Memory is out of room for new pages and ```access_requests_list``` which is a list that stores the sequence of virtual page access requests. ```N``` will be receive as an input from the user, while ```access_requests_list``` will be done after the input file was read. Once the input file is read and the ```access_requests_list``` has the sequence of virtual page access requests, a while loop will go in until the last request is remove from the ```access_requests_list```. Inside that while loop, the first thing that will happen is that an object for a specific page will be created. After that, there is a function that will check if that page is or not inside of Physical Memory. If the page is inside Physical Memory, then the operation perform, clock and reference bit of the page is going to be updated. If the page is not inside Physical Memory, then either two of the following things will happen. If the Physical Memory has room left, then the page is just going to be added to it, if it does not have room then the page that is going to be remove is the one whose ```reference_bit``` equals zero and is not on the working set. If the pages on Physical Memory are either reference (which means that the ```reference_bit``` equals one) or form part of the working set, the page that is going to remove so it can be replace by a new one is the one with the smallest time.

## References
To do this program multiple references where used:
* Classes: https://docs.python.org/es/3/tutorial/classes.html
* Changing the value of an object: https://programacion.net/articulo/como_funcionan_las_clases_y_objetos_en_python_1505
* How to send arguments from the command line: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
* How to open and read a file in python: https://www.kite.com/python/answers/how-to-split-a-file-into-a-list-in-python#use-str-splitlines
* How insert an element in a specific position of the list: https://thispointer.com/python-how-to-insert-an-element-at-specific-index-in-list/
* How to find objects inside a list: https://es.stackoverflow.com/questions/268781/instanciar-objetos-y-guardarlos-en-una-lista-con-bucle-for
* How to use the break function in python: https://www.tutorialspoint.com/python/python_loop_control.htm

Also the student Joniel Méndez explain to me how to get arguments from the command line and Gabriel Santiago help me with ```LocationRemovePage(tau, clock, physical_memory)``` function in ```wsclock.py``` file.

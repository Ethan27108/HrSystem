# Hr System

## Basic Information
This program is an Hr System made using python and the library pygame for the GUI as I wanted to learn how to code using pygame and create my own textboxes and pages so I knew how they were made.
This is also made with a Microsoft sql database as I was learning it so it is very basic with just simple storing, retreving and table creation commands.
This program uses many objects and classes that seem to serve no real prupose and thats because I wanted to undertsand how complex and embeeded you could create objects so the simple fix to be proper is to put all variables in the employee class and no subclasses to it.
The textbox class is very important and is more an actual class that should exist in this program alng with just the employee code.

## Description
The point of the project was to learn which is why it has some weird ways of doing stuff read basic info for more but it was also meant to be something proffesional which is why it uses databases and not textfiles and has a GUI and not just typing in a terminal.
What this does is simple it gets a bunch of data for employees some examples are first name address and phone number and much more and then stores it in a sql database you can edit or add or delete different employees by searching for them with just the employee number.
The employee number is the primary key and cannot be changed by the user and is something fully done with the system so that no duplicate exist and everyone has a unique employee number.

### Add function
The add function will bring you to a new page where it has a bunch of textboxes and you just click on the textbox and type the info you want in each following the header and at the end hit submit to submit it to the database or cancel to go back to main page.

### Edit function
This is the same as add function but it will automatically display the info that is already stored at the employee you choose with the employee number read add to see how it works.

### Delete function
This will take the employee number given and then delete it from the list and the database and correct all of the employee numbers so it goes from 1 to number of employees and there are no gaps(this could be changed if needed or you could save the deleted
to a different table so you dont lose the file if that is needed in the company)

## How to use
Download the folder and then open main.py and run it then it will bring you to a main page with three buttons and a search bar type a employee if you want add just press where it says add if you want to delete or edit you must put a valid employee number then click on the edit or add.
Make sure you have python and pygame installed.

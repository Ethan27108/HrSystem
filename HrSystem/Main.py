from Employee import *
from textbox import *
import sqlite3
import itertools
import os
import pygame
import math
def get_nested_attr(obj, attr):
    parts = attr.split('.')
    for part in parts:
        obj = getattr(obj, part)
    return obj

# Define the attribute path as a string
firstInd = "personalInfo.name.first"
middleInd = "personalInfo.name.middle"
lastInd = "personalInfo.name.last"
housenumberInd = "personalInfo.address.housenumber"
streetInd = "personalInfo.address.street"
cityInd = "personalInfo.address.city"
provinceInd = "personalInfo.address.province"
countryInd = "personalInfo.address.country"
ageInd = "personalInfo.birthInfo.age"
dayInd = "personalInfo.birthInfo.DateOfBirth.day"
monthInd = "personalInfo.birthInfo.DateOfBirth.month"
yearInd = "personalInfo.birthInfo.DateOfBirth.year"
cellInd = "contactInfo.phoneNumber.cell"
workNumInd = "contactInfo.phoneNumber.workNum"
homeInd = "contactInfo.email.home"
workInd = "contactInfo.email.work"
hourlyRateInd = "jobInfo.billing.hourlyRate"
hoursInd = "jobInfo.billing.hours"
bonusInd = "jobInfo.billing.bonus"
yearsWorkedInd = "jobInfo.yearsWorked.yearsWorked"
empNumInd = "empNum"
dataList = [firstInd, middleInd, lastInd, housenumberInd, streetInd,cityInd,provinceInd,countryInd, ageInd, dayInd,monthInd,yearInd,cellInd, workNumInd, homeInd,workInd, hourlyRateInd, hoursInd,bonusInd,yearsWorkedInd,empNumInd]
nameList=[["fName","mName","lName","houseNum","street"],["city","province","country","age","day"],["month","year","cellNum","workNum","homeEmail"],["workEmail","hourlyRate","hours","bonus","yearsWorked"]]
def creatingEmp(first, middle,last, housenumber, street,city,province,country, age, day,month,year,cell, workNum, home,work, hourlyRate, hours,bonus,yearsWorked,empNum):
    emp = Employee(first, middle,last, housenumber, street,city,province,country, age, day,month,year,cell, workNum, home,work, hourlyRate, hours,bonus,yearsWorked,empNum)
    emplist.insert((empNum-1),emp)
    storingInfo(emp)
    empNum+=1
    return empNum

    
def dataBaseToList(first, middle,last, housenumber, street,city,province,country, age, day,month,year,cell, workNum, home,work, hourlyRate, hours,bonus,yearsWorked,empNum):
    emp = Employee(first, middle,last, housenumber, street,city,province,country, age, day,month,year,cell, workNum, home,work, hourlyRate, hours,bonus,yearsWorked,empNum)
    emplist.append(emp)

"""def storingAllInfo():
    connection = sqlite3.connect("EmpDatabase.db")
    cursor = connection.cursor()
    for i in emplist:
        valList=[]
        for j in dataList:
            valList.append(get_nested_attr(i, j))
        cursor.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (valList))
    connection.commit()
    connection.close()
"""

def storingInfo(emp):
    connection = sqlite3.connect("EmpDatabase.db")
    cursor = connection.cursor()
    valList = []
    for j in dataList:
        valList.append(get_nested_attr(emp, j))
    cursor.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (valList))
    connection.commit()
    connection.close()  
    
def creatingTable():
    connection = sqlite3.connect("EmpDatabase.db")
    cursor = connection.cursor()
    showAllTables = """SELECT name FROM sqlite_master WHERE type='table'"""
    cursor.execute(showAllTables)
    if ('data',) not in cursor.fetchall(): 
        sql_command = """CREATE TABLE data (
            first VARCHAR(30),
            middle VARCHAR(30),
            last VARCHAR(30),
            housenumber VARCHAR(30),
            street VARCHAR(30),
            city VARCHAR(30),
            province VARCHAR(30),
            country VARCHAR(30),
            age VARCHAR(30),
            day VARCHAR(30),
            month VARCHAR(30),
            year VARCHAR(30),
            cell VARCHAR(30),
            workNum VARCHAR(30),
            home VARCHAR(30),
            work VARCHAR(30),
            hourlyRate VARCHAR(30),
            hours VARCHAR(30),
            bonus VARCHAR(30),
            yearsWorked VARCHAR(30),
            empNum INTEGER)
        """
        cursor.execute(sql_command)
        connection.commit()
    connection.close()
    
def retrieveInfo():
    empNum = 1
    connection = sqlite3.connect("EmpDatabase.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM data")

    results=cursor.fetchall()
    for i in results:
        dataBaseToList(*i)
        empNum += 1
    connection.close()
    return empNum

def deleteInfo(empNum):
    connection = sqlite3.connect("EmpDatabase.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE empNum=?", (empNum,))
    for i in emplist:
        if (get_nested_attr(i, empNumInd)) == empNum:
            ind= emplist.index(i)
            del emplist[ind]
    connection.commit()
    connection.close()
    
def printeverything(emp):
    for j in dataList:
        print(get_nested_attr(emp, j),end=" "),
    print()
        

def updatingInfo(change):
    for i in emplist:
        val = get_nested_attr(i, empNumInd)
        if (val > change):
            i.empNum = change
            change += 1
            storingInfo(i)
            deleteInfo(change)
            
def deleteAndUpdate(empNum):
    deleteInfo(empNum)
    updatingInfo(empNum)  

def editEmp(first, middle,last, housenumber, street,city,province,country, age, day,month,year,cell, workNum, home,work, hourlyRate, hours,bonus,yearsWorked,empNum):
    'UPDATE data SET first = "John" WHERE empNum = 1' # thats a thing
    deleteInfo(empNum)
    creatingEmp(first, middle,last, housenumber, street,city,province,country, age, day,month,year,cell, workNum, home,work, hourlyRate, hours,bonus,yearsWorked,empNum)
    
choice = 0
emplist = []   
creatingTable()
empNum=retrieveInfo()
pygame.init() 
font = pygame.font.Font("AnonymousPro-Regular.ttf", 20)
clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
running = True
white = (255, 255, 255)
black = (0, 0, 0)

colorActive = pygame.Color("#808080")  
colorPassive = pygame.Color("#FFFFFF") 
color = colorPassive 


page = "main"
active = False
confirmation = ''
size = "small"
clicked=False
user_text = ''
while running: 
    #stopping process
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running=False
        pygame.display.update()
    
        if page == "main":
            if (size == "big"):
                window = pygame.display.set_mode((500,500))
                size = "small"
                user_text = ''
            addRect = pygame.Rect(75, 233, 50, 24) 
            editRect = pygame.Rect(216.8, 233, 66.7, 24) 
            deleteRect = pygame.Rect(350, 233, 100, 24) 
            

            searchRect = pygame.Rect(100, 150, 300, 32) 
            #display info
            text = font.render(confirmation, False, white)
            textRect = text.get_rect()
            textRect.center = (250, 300)
            window.blit(text, textRect)
            
            text = font.render("Employee List ", False, white)
            textRect = text.get_rect()
            textRect.center = (250, 25)
            window.blit(text, textRect)
            
            text = font.render("Add", False, white)
            textRect = text.get_rect()
            textRect.center = (100, 250)
            window.blit(text, textRect)
            
            text = font.render("Edit", False, white)
            textRect = text.get_rect()
            textRect.center = (250, 250)
            window.blit(text, textRect)
            
            text = font.render("Delete", False, white)
            textRect = text.get_rect()
            textRect.center = (400, 250)
            window.blit(text, textRect)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.draw.rect(window, (black),
                    [0, 275, 500, 500], 0)
                    if addRect.collidepoint(event.pos):
                        page="add"
                        startList=[[],[],[],[]]
                        for i in range(4):
                            for j in range(5):
                                EmpDatabase = textbox(50+150*j,50+100*i,nameList[i][j],'')   
                                startList[i].append(EmpDatabase)
                    elif editRect.collidepoint(event.pos):
                        if user_text.isnumeric():
                            
                            if int(user_text)<empNum and empNum>0:
                                count=0
                                page="edit"
                                startList=[[],[],[],[]]
                                for i in range(4):
                                    for j in range(5):
                                        EmpDatabase = textbox(50+150*j,50+100*i,nameList[i][j],(get_nested_attr(emplist[int(user_text)-1],dataList[count])))   
                                        startList[i].append(EmpDatabase)
                                        count+=1
                            else:
                                confirmation = "There is no employee with the employee number of " + user_text
                        else:
                            confirmation = "Error must be a number"
                    elif deleteRect.collidepoint(event.pos):
                        if user_text.isnumeric():
                            if int(user_text)<empNum and empNum>0:
                                page="delete"
                                
                            else:
                                confirmation = "There is no employee with the employee number of " + user_text
                        else:
                            confirmation = "Error must be a number"
                    elif searchRect.collidepoint(event.pos): 
                        
                        active = True
                        confirmation = ''
                    else: 
                        active = False 
                        confirmation = ''  
                        
            if active: 
                color = colorActive       
                if event.type == pygame.KEYDOWN: 
                    
                    
                    # Check for backspace 
                    if event.key == pygame.K_BACKSPACE: 
        
                        # get text input from 0 to -1 i.e. end. 
                        user_text = user_text[:-1] 
        
                    # Unicode standard is used for string formation 
                    else: 
                        user_text += event.unicode
            else: 
                color = colorPassive 
            pygame.draw.rect(window, color, searchRect) 
            textnew = user_text[-20:]
            text_surface = font.render(textnew, False, (0, 0, 0)) 
            window.blit(text_surface, (searchRect.x+5, searchRect.y+5)) 
            searchRect.w = max(300, text_surface.get_width()+10)     
                
        elif page == "add" or page=="edit":
            
            if (size == "small"):
                window=pygame.display.set_mode((1000,600))
                size="big"
            for i in range(4):
                for j in range(5):  
                    startList[i][j].drawing(window)  
            
            submitRect = pygame.Rect(525, 488, 50, 24) 
            cancelRect = pygame.Rect(425, 488, 50, 24) 
            text = font.render("Submit", False, white)
            textRect = text.get_rect()
            textRect.center = (550, 500)
            window.blit(text, textRect)
            
            text = font.render("Cancel", False, white)
            textRect = text.get_rect()
            textRect.center = (450, 500)
            window.blit(text, textRect)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1 and clicked==False:   
                    for i in range(4):
                        for j in range(5):  
                            startList[i][j].resetColor(window)
                    clicked=True
                    indRightX=-1
                    indRightY=-1
                    x, y = pygame.mouse.get_pos()
                    
                    temp=x-49
                    indwrong=math.ceil(temp/150)
                    x=x-(150*indwrong)
                    if (-100<=x<=0):
                        indRightX=indwrong-1
                        
                    temp=y-49
                    indwrong=math.ceil(temp/100)
                    y=y-(100*indwrong)
                    if (-30<=y<=-10):
                        indRightY=indwrong-1
                    
                    if (indRightX!=-1 and indRightX<=4) and (indRightY!=-1 and indRightY<=3):
                        startList[indRightY][indRightX].clickedOn(window)
                    if submitRect.collidepoint(event.pos):
                        tempList=[]
                        for i in range(4):
                                for j in range(5):  
                                    tempList.append(startList[i][j].getVal())
                        if page=="edit":
                            tempList.append(int(user_text))
                            editEmp(*tempList)
                        elif page=="add":
                            tempList.append(empNum)
                            empNum=creatingEmp(*tempList)      
                        page="main"
                    elif cancelRect.collidepoint(event.pos):
                        page="main"    
                        
            if event.type == pygame.KEYDOWN: 
                    # Check for backspace 
                if event.key == pygame.K_BACKSPACE: 
        
                        # get text input from 0 to -1 i.e. end. 
                    for i in range(4):
                        for j in range(5):  
                            startList[i][j].delKey() 
        
                    # Unicode standard is used for string formation 
                else: 
                    for i in range(4):
                        for j in range(5):  
                            startList[i][j].keyInput(event.unicode)          
            if event.type == pygame.MOUSEBUTTONUP:
                clicked=False
                
        elif page=="delete":
            if (size == "small"):
                window = pygame.display.set_mode((500,150))
                size = "big"
                
            confirmRect = pygame.Rect(175, 88, 50, 24)         
            cancelRect = pygame.Rect(275, 88, 50, 24)         
            
                
            text = font.render("Are you sure you want to delete?", False, white)
            textRect = text.get_rect()
            textRect.center = (250, 25)
            window.blit(text, textRect)
            
            text = font.render("Confirm", False, white)
            textRect = text.get_rect()
            textRect.center = (200, 100)
            window.blit(text, textRect)
            
            text = font.render("Cancel", False, white)
            textRect = text.get_rect()
            textRect.center = (300, 100)
            window.blit(text, textRect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if confirmRect.collidepoint(event.pos):
                        deleteAndUpdate(int(user_text))
                        empNum-=1
                        page="main"
                    elif cancelRect.collidepoint(event.pos):
                        page="main"
                
    
        
    # display.flip() will update only a portion of the 
    # screen to updated, not full area 
    pygame.display.flip() 
    
    # clock.tick(60) means that for every second at most 
    # 60 frames should be passed. 
    clock.tick(60) 





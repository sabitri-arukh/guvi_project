import mysql.connector
import re
     
class connection_db:
    def __init__(self):
        self.db = mysql.connector.connect(
                host ="localhost",
                user ="root",
                password = "Mysql#2024",
                database = "schoolmanagementsystem"
            )
            
    def creat_table(self,tableName,tableValues):
        try:
            cursor = self.db.cursor()
            query =f"create table {tableName} {tableValues}"
            cursor.execute(query)
            print("Table created")
        except Exception as e:
            print(str(e))
    def addDataToTable(self,tableName,fieldstoAdd,values): 
        try:
            cursor = self.db.cursor() 
            query = f'insert into {tableName} {fieldstoAdd} values {values}' 
            cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print(str(e)) 

    def readData(self,tableName):
        try:
            cursor = self.db.cursor() 
            query = f'select * from {tableName}' 
            cursor.execute(query)
            value = cursor.fetchall()
            return value
        except Exception as e:
            print(str(e))

    def question_method(self):
        try:
            que = input('1 for read the data\n2 for insert a new data\n3 for upadate a new data\n4 for delete a data\n') 
            return que
        except:
            print('Error')

    def get_values(self,columns_to_be_added):
        datas = tuple([i for i in re.split('[(,)]',columns_to_be_added)if i])
        out_data=tuple(input(f'{i}: ') for i in datas)
        return out_data
        
    def update_values(self,tableName,idName,id,fieldstoUpdate,newValue):
        try:
            cursor = self.db.cursor()
            query= f"update {tableName} set {fieldstoUpdate} = {newValue} where {idName}={id}"
            cursor.execute(query)
            self.db.commit()
            print('The data got updated')
        except:
            print('Error in update')
    
    def delete_data(self,tableName,idName,id):
        try:
            cursor = self.db.cursor()
            query = f'delete from {tableName} where {idName}= {id}'
            cursor.execute(query)
            self.db.commit()
            print('It is successfully deleted')
        except:
            print('It is failed to be deleted')


conn = connection_db()
'''conn.creat_table('Student','(sno int auto_increment primary key ,StudentId int ,StudentName varchar(255),PythonMark int, MathMark int, PhysicsMark int)')
conn.creat_table('Teacher','(sno int auto_increment primary key,TeacherId int ,TeacherName varchar(255),TeacherSalary int,TeacherJoiningDate date)')
conn.creat_table('Principal','(sno int auto_increment primary key,PrincipalId int ,PrincipalName varchar(255),PrincipalSalary int,PrincipalJoiningDate date)')
conn.creat_table('Admin','(sno int auto_increment primary key,AdminId int ,AdminName varchar(255),Password varchar(255))')
'''
# conn.addDataToTable('Admin','(AdminId,AdminName,Password)',(1,'Basudev','2901'))
# conn.addDataToTable('Admin','(AdminId,AdminName,Password)',(2,'Sabitri','2308'))
# conn.addDataToTable('Student','(StudentId,StudentName,PythonMark,MathMark,PhysicsMark)',(101,'Aradhya',90,95,80))
# conn.addDataToTable('Student','(StudentId,StudentName,PythonMark,MathMark,PhysicsMark)',(102,'Vikash',95,80,88))
# conn.addDataToTable('Teacher','(TeacherId,TeacherName,TeacherSalary,TeacherjoiningDate)',(202, 'Rohan',50000,'2017-11-23'))
admin_check = False
while not admin_check:
    adminId = input('Enter Your AdminId: ')
    adminPasswd = input('Enter Your adminPassword: ')
    data_admin = conn.readData('Admin')
    # print(data_admin)
   
    for i in data_admin:
        # print(i[1], i[-1], adminId, adminPasswd)
        if adminId == str(i[1]) and adminPasswd == i[-1]:
            admin_check = True
            break

    if admin_check:
        print('You are a valid Admin') 
        selection_admin = input('What you wanted to see\n1 for Student\n2 for Teacher\n3 for Principal\n')
        if selection_admin== '1':
            tableName= 'Student'
            columns_to_be_added = '(StudentId,StudentName,PythonMark,MathMark,PhysicsMark)'
            print('You have entered into Student section')
            print()
            select_output = conn.question_method()
            if select_output== '1':
                select_output=conn.readData(tableName)
                print("The Student Details:")
                print(select_output)
            elif select_output== '2':
                select_output=conn.get_values(columns_to_be_added)
                print(select_output)
                conn.addDataToTable('Student',columns_to_be_added,select_output)
            elif select_output== '3':
                tableName= 'Student'
                id = int(input('Enter the studentId in which you want to update: '))
                fieldstoUpdate = input('Enter the columnName in which you want to update: ')
                newValue= input('Enter the new data: ')
                idName= "StudentId"
                conn.update_values(tableName,idName,id,fieldstoUpdate,newValue)
            elif select_output== '4':
                tableName= 'Student'
                id = int(input('Enter the studentId in which you want to delete: '))
                idName= "StudentId"
                conn.delete_data(tableName,idName,id)
            
        elif selection_admin== '2':
            tableName= 'Teacher'
            columns_to_be_added = '(TeacherId,TeacherName,TeacherSalary,TeacherJoiningDate)'
            print('You have entered into Teacher section')
            print()
            select_output = conn.question_method()
            if select_output== '1':
                select_output=conn.readData(tableName)
                print("The Teacher Details:")
                print(select_output)
            elif select_output== '2':
                select_output=conn.get_values(columns_to_be_added)
                print(select_output)
                conn.addDataToTable('Teacher',columns_to_be_added,select_output)
            elif select_output== '3':
                tableName= 'Teacher'
                id = int(input('Enter the teacherId in which you want to update: '))
                fieldstoUpdate = input('Enter the columnName in which you want to update: ')
                newValue= input('Enter the new data: ')
                idName= "TeacherId"
                conn.update_values(tableName,idName,id,fieldstoUpdate,newValue)
            elif select_output== '4':
                tableName= 'Teacher'
                id = int(input('Enter the teacherId in which you want to delete: '))
                idName= "TeacherId"
                conn.delete_data(tableName,idName,id)

        elif selection_admin== '3':
            tableName= 'Principal'
            columns_to_be_added = '(PrincipalId,PrincipalName,PrincipalSalary,PrincipalJoiningDate)'
            print('You have entered into Principal section')
            print()
            select_output = conn.question_method()
            if select_output== '1':
                select_output=conn.readData(tableName)
                print("The Principal Details:")
                print(select_output)
            elif select_output== '2':
                select_output=conn.get_values(columns_to_be_added)
                print(select_output)
                conn.addDataToTable('Principal',columns_to_be_added,select_output)
                
            elif select_output== '3':
                tableName= 'Principal'
                id = int(input('Enter the principalId in which you want to update: '))
                fieldstoUpdate = input('Enter the columnName in which you want to update: ')
                newValue= input('Enter the new data: ')
                idName= "PrincipalId"
                conn.update_values(tableName,idName,id,fieldstoUpdate,newValue)
            elif select_output== '4':
                tableName= 'Principal'
                id = int(input('Enter the principalId in which you want to delete: '))
                idName= "PrincipalId"
                conn.delete_data(tableName,idName,id)
    else:
        print('You are not a valid Admin .Enter proper credentials')
  
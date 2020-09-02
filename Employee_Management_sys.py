import pickle

class Employees:

    def __init__(self, employee_id, name, Department, Title, Salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__Department = Department
        self.__Title = Title
        self.__Salary = Salary

    def get_employee_id(self):
        return self.__employee_id
    def get_name(self):
        return self.__name
    def get_Department(self):
        return self.__Department
    def get_Salary(self):
        return self.__Salary

    def set_employee_id(self,employee_id):
        self.__employee_id = employee_id
    def set_name(self,name):
        self.__name = name
    def set_Department(self,Title):
        self.__Title = Title
    def set_Salary(self,Salaty):
        self.__Salary = Salary
    def __str__(self):
        return ("Employee ID: {}\n\tName: {}\n\tDepartment: {}\n\tTitle: {}\n\tSalary: {}"\
                . format (str(self.__employee_id),self.__name,self.__Department,self.__Title,str(format(self.__Salary,",.2f"))))

    

def main ():
    print("Welcome to Employee Management System (EMS)")
    file_name ="employee.dat"
    db=load (file_name)
        
    
    
    EXIT =False
    while EXIT == False:
        
        user_selction = input ("Main Menu:\n\
1.	Add an Employee\n\
2.	Find an Employee (By Employee ID)\n\
3.	Find an Employee (By Name)\n\
4.	Delete an Employee\n\
5.	Display Statistics\n\
6.	Display All Employees\n\
7.	Exit\n\
Enter you selection (1..7):\n").lower()
# Checking the user selection
        while (user_selction) not in ["1","2","3","4","5","6","7"]:
              print ("Invalid selection.")
              user_selction = input ("Enter you selection (1..7):\n").lower()
              
              
        else:
            
            if user_selction == '1':
                add_employee_ID(EXIT,db)
            elif user_selction == '2':
                find_employee_ID(EXIT,db)
            elif user_selction == '3':
                find_employee_name(EXIT,db)
            elif user_selction == '4':
                delete_employee (EXIT,db)
            elif user_selction == '5':
                statistics(db)
            elif user_selction == '6':
                all_employee(db)
            elif user_selction == '7':
    
                save(db,file_name)
                print ("Thank you for using Employee Management System (EMS)")
           
            
                EXIT = True
# Add new user with an Unique employee ID   
def add_employee_ID(e,x):
    
    employee_id = input ("Enter an Employee ID or QUIT to stop:\n").lower()
    while employee_id != 'quit':
        try:
            employee_id=int(employee_id)
            # Checking if the employee ID had been already used
            
            if (employee_id in x):
                employee_id= input(" This Employee ID already exist re enter new Id or quit to exit:")
                break
            if  employee_id != 'quit' :
                
                name = input ("Enter employee name:\n")
                Department= input ("Enter employee department:\n")
                Title = input ("Enter employee title:\n")
                Salary = float(input ("Enter employee salary:\n"))
                # Adding the employee information 
                employee_info = Employees(employee_id,name,Department,Title,Salary)
                x[employee_id]=employee_info
                
                break
        except ValueError:
            employee_id = input ("Enter an Employee ID or QUIT to stop:\n").lower()
                    
                
    else:
        e = True
    return (e,x)
# Finding employee by the ID number 

def find_employee_ID(e,x):
    found = False
    employee_id = input ("Enter an Employee ID or QUIT to stop:\n").lower()
    if employee_id != 'quit':
        employee_id=int (employee_id)
        for emp_id in x:
            if emp_id == employee_id:
                found = True
        if found == True:
            print ("Employee ID: {}\n\tName: {}\n\tDepartment: {}\n\tTitle: {}\n\tSalary: {}". format(emp_id,x[emp_id]['Name'],x[emp_id]['Department'],\
                                                                                            x[emp_id]['Title'],(format (x[emp_id]['Salary'],",.2f"))))
        else :
            print("Employee ID: {} was not found in the database.". format(employee_id))
            employee_id = input ("Enter an Employee ID or QUIT to stop:\n").lower()
    else:
        e =True

    return (e,x)
#Finding the employee by name 
def find_employee_name(e,x):
    account = 0
    employees_names ={}
    employee_name = input ("Enter an employee name or QUIT to stop:\n")
    if employee_name !="quit":
        for emp_id in x.keys():
            if (x[emp_id]["Name"])== (employee_name):
                employees_names[emp_id]=x[emp_id]
                account = account+1
        print ("Found {} employee with that name.". format(account))
        for emp_id in employees_names:
            print ("Employee ID: {}\n\tName: {}\n\tDepartment: {}\n\tTitle: {}\n\tSalary: {}". format(emp_id,x[emp_id]['Name'],x[emp_id]['Department'],\
                                                                                            x[emp_id]['Title'],(format (x[emp_id]['Salary'],",.2f"))))
        
    else:
        e = True
    
# Delete Employee by the ID   
def delete_employee(e,x):
    employee_id = int(input ("Enter an Employee ID or QUIT to stop:\n"))
    if employee_id != 'quit':
        y = x.pop(employee_id,"Employee ID unavailble")
        if y == "Employee ID unavailble":
            print ("Employee ID unavailble")
    else:
        e = True

    return (e,x)
# Employees Summary 
def statistics(x):
    account = 0
    emp_info={}
    max_salary = 0
    min_salary = 0
    total_s = 0
    
    
    for employee_id in x.keys():
        
        dep_name = x[employee_id].get_Department()
        
        if dep_name not in emp_info.keys():
            account = 1
            max_salary = x[employee_id].get_Salary()
            min_salary = x[employee_id].get_Salary()
            total_s= x[employee_id].get_Salary()
            emp_info[dep_name]={"account":account,"max_salary":max_salary\
                                            ,"min_salary":min_salary,"Total_salary":total_s}
     
        else:
            emp_info[dep_name]["account"] += 1
            
            if x[employee_id].get_Salary() > emp_info[dep_name]["max_salary"]:
                emp_info[dep_name]["max_salary"]= x[employee_id].get_Salary()
            if x[employee_id].get_Salary() < emp_info[dep_name]["min_salary"] :
                emp_info[dep_name]["min_salary"] = x[employee_id].get_Salary()
            emp_info[dep_name]["Total_salary"] += x[employee_id].get_Salary()
            emp_info[dep_name]={"account":emp_info[dep_name]["account"],"max_salary":emp_info[dep_name]["max_salary"]\
                                            ,"min_salary":emp_info[dep_name]["min_salary"],"Total_salary":emp_info[dep_name]["Total_salary"]}
            
# Checking if the Database empty 
    if len(emp_info)== 0 :
        print ("There are no departments in the database.")
        print ("Employee database is empty.")
    else:
        print("Department Statistics:")
        for dep in sorted(emp_info.keys()):
            print ("\tDepartment: {} - {} employee{}". format(dep,emp_info[dep]["account"],"s"if len(emp_info)>1 else""))
            print ("\t\tMaximum Salary: $ {}". format(format (emp_info[dep]["max_salary"],",.2f")))
            print ("\t\tMinimum Salary: $ {}". format(format (emp_info[dep]["min_salary"],",.2f")))
            print ("\t\tAverage Salary: $ {}". format(format (emp_info[dep]["Total_salary"]/emp_info[dep]["account"],",.2f")))
        if len(emp_info.keys()) == 1 :
            print ("There is {} department in the database.". format (len(emp_info.keys())))
        else:
            print ("There are {} departments in the database.". format (len(emp_info.keys())))
        Total = len(x.keys())
        if Total ==1:
            print ("There is {} employee in the database.". format (Total))
        else:
            print ("There are {} employees in the database.". format (Total))
               
    
        
    
def all_employee(x):
    Total = 0
    if x =={}:
        print("Employee database is empty.")
    else:
        for employee_id in x.keys():
            print (x.get(employee_id))

        print("There are {} employees in the database." . format(len(x.keys())))
   
         
# Loading the saved information
def load(filename):
    try:
        main_file = open (filename,"br")
    
        x=pickle.load(main_file)       
        
        main_file.close()
        
    except:
        print ("Unable to load the database from binary file employee.dat.\nCreating an empty database.")
        x={}
    return x
         
        
# Save all information
def save(x,file_name):
    
    file_input = open(file_name,"bw")
    
    x=pickle.dump(x,file_input)

    file_input.close()

    return(x,file_input)
    
    
main()



    


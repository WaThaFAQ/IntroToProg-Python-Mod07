# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   JNoumeh,11/30/2023,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Data ------------------------------------- #
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


# Create Class for Getter and Setters for a person
class Person:
    """
    A class representing person data.

    Properties:
        student_first_name (str): The student's first name.
        student_last_name (str): The student's last name.

    ChangeLog:
        - JNoumeh, 12.2.2023: Created the class.
    """

    # TODO Add first_name and last_name properties to the constructor (Done)
    def __init__(self, student_first_name: str = '', student_last_name: str = ''):
        """
        Initialises student name to empty strings

        :param student_first_name: empty string 1
        :param student_last_name: empty string 2

         ChangeLog:ll
        - JNoumeh, 12.2.2023: Created the class.
        """
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

    # TODO Create a getter and setter for the first_name property (Done) as in the Student class
    @property  # (Use this decorator for the getter or accessor)
    def student_first_name(self):

        return self.__student_first_name.title()  # formatting code

    @student_first_name.setter
    def student_first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__student_first_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Create a getter and setter for the last_name property (Done)
    @property
    def student_last_name(self):
        return self.__student_last_name.title()  # formatting code

    @student_last_name.setter
    def student_last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Override the __str__() method to return Person data (Done)
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name}'


# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    """
    A class representing student data.

    Properties:
        student_first_name (str): The student's first name.
        student_last_name (str): The student's last name.
        course_name (str): The course the student is registered for.

    ChangeLog: (Who, When, What)
    JNoumeh,12.2.2023,Created Class
    """

    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, student_first_name: str = '', student_last_name: str = '', course_name: str = ''):
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)
        # TODO add a assignment to the course_name property using the course_name parameter (Done)
        self.course_name = course_name

    # TODO add the getter for course_name (Done)
    @property # getter
    def course_name(self):
        return self.__course_name

    # TODO add the setter for course_name (Done)
    @course_name.setter # setter
    def course_name(self, value: str):
        self.__course_name = value

    # TODO Override the __str__() method to return coma separated string Student data (Done)
    # Override the Parent __str__() method behavior to return a coma-separated string of data
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name},{self.course_name}'


# Processing ------------------------------------- #
class FileProcessor:
    """
    Contains two methods:
    First Method - Reads json file and stores to a variable (list of dictionaries)
    Second Method - Writes a variable (list of dictionaries) to a json file

    ChangeLog: (Who, When, What)
    JNoumeh,11.30.2023,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of objects

        ChangeLog: (Who, When, What)
        JNoumeh,12.2.2023,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """
        try:
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)
            for student in list_of_dictionary_data:
                student_object: Student = Student(student_first_name=student["FirstName"],
                                                  student_last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(message='Text file must exist before running this script!', error=e)
        except Exception as e:
            IO.output_error_messages(message='Error: There was a non-specific error!', error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data (list of objects) to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        JNoumeh,12.2.2023,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for student in student_data:
                student_json: dict \
                    = {"FirstName": student.student_first_name,
                       "LastName": student.student_last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages(message="Please check that the data is a valid JSON format", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a non-specific error!", error=e)
        finally:
            if file.closed == False:
                file.close()


# Presenting ------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    output_error_messages: prints param:message to the user and prints error information
        if param:error contains one


    ChangeLog: (Who, When, What)
    JNoumeh,12.2.2023,Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays a message and an error message to the user

            ChangeLog: (Who, When, What)
            JNoumeh,12.2.2023,Created Class

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end='\n\n')
        if error is not None:
            print('-- Technical Error Message --')
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ Prints the menu to the user

            ChangeLog: (Who, When, What)
            JNoumeh,12.2.2023,Created Class

        :param menu: string with menu options for user to choose from

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ prompts the user to enter a menu choice and stores that choice

            ChangeLog: (Who, When, What)
            JNoumeh,12.2.2023,Created Class

        :return: string with user choice
        """
        choice = "0"
        try:
            choice = input('Enter your menu choice number: ')
            if choice not in ('1', '2', '3', '4'):
                raise Exception('Please, choose only 1, 2, 3, or 4')
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ Retrieves student name and course and appends it to a list in dictionary format

            ChangeLog: (Who, When, What)
            JNoumeh,12.2.2023,Created Class

        :param student_data: list containing dictionaries

        :return: list of dictionaries appended with user data
        """
        try:
            # Input the data
            student = Student()
            student.student_first_name = input("Enter the student's first name: ")
            student.student_last_name = input("Enter the student's last name: ")
            student.course_name = input('Please enter the name of the course: ')
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message='Error: There was a problem with your entered data.', error=e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """ Prints out the student and course stored in a list of dictionaries

            ChangeLog: (Who, When, What)
            JNoumeh,12.2.2023,Created Class

        :param student_data: list of dictionaries

        :return: None
        """
        print('-'*50)
        for student in student_data:
            message = "{} {} is enrolled in {}"
            print(message.format(student.student_first_name, student.student_last_name, student.course_name))
        print('-'*50)


# Start of main body
# When the program starts, read the file data into a list of dictionaries
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == '1':
        IO.input_student_data(student_data=students)

    # Present the current data
    elif menu_choice == '2':
        IO.output_student_courses(students)

    # Save the data to a file
    elif menu_choice == '3':
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

    # Stop the loop
    elif menu_choice == '4':
        break
    else:
        print('Please only choose option 1, 2, or 3')

print('Program Ended')

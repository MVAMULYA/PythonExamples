import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_pwd, db):
    '''Function to establish a connection to server

    '''
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_pwd,
            database=db
        )
        print("MySql database connection successful")
    except Error as err:
        print(f'Error : "{err}"')
    return connection

def create_database(connection, query):
    '''Function to create a database

    '''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f'Error : "{err}"')
    finally:        
        cursor.close()

def execute_query(connection, query):
    '''Function to execute SQL Queries

    '''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit() # to make sure commands in the query are executed
        print("Query executed successfully")
    except Error as err:
        print(f'Error : {err}')
    finally:
        cursor.close()

def execute_list_query(connection, query, val_list):
    '''Function to execute SQL Queries

    '''
    cursor = connection.cursor()
    try:
        cursor.executemany(query, val_list)
        connection.commit() # to make sure commands in the query are executed
        print("Query executed successfully")
    except Error as err:
        print(f'Error : {err}')
    finally:
        cursor.close()

def query_fetch(connection, query):
    '''Function to read data from tables

    '''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f'Error: {err}')

pwd = 'M19@mulya' # password to connect to server
db = "School"
connection = create_server_connection("localhost", "root", pwd, db)
create_teacher_table = """
CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    language_1 VARCHAR(3) NOT NULL,
    language_2 VARCHAR(3),
    dob DATE,
    tax_id INT UNIQUE,
    phone_no VARCHAR(20)

);
"""
create_client_table = """
CREATE TABLE Client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(20) NOT NULL,
    address VARCHAR(40) NOT NULL,
    industry VARCHAR(20)
);
"""
create_participant_table = """
CREATE TABLE Participant (
    participant_id INT PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    phone_no VARCHAR(20),
    Client INT
);
"""
create_course_table = """
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(40) NOT NULL,
    language  VARCHAR(20) NOT NULL,
    level VARCHAR(20),
    course_length_weeks INT,
    start_date DATE,
    in_school BOOLEAN,
    teacher INT,
    client INT
);
"""
#execute_query(connection, create_client_table)
#execute_query(connection, create_course_table)
#execute_query(connection, create_participant_table)
#execute_query(connection, create_teacher_table)

alter_participant = """
ALTER TABLE participant 
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""
alter_course_teacher_f_key = """
ALTER TABLE course
ADD FOREIGN KEY(teacher)
REFERENCES teacher(teacher_id)
ON DELETE SET NULL;
"""

alter_course_client_f_key = """
ALTER TABLE course
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""
create_takeCourse_table = """
CREATE TABLE takecourse (   
participant_id INT,
course_id INT,
PRIMARY KEY(participant_id, course_id),
FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
); 
"""
#execute_query(connection, alter_participant)
#execute_query(connection, alter_course_teacher_f_key)
#execute_query(connection, alter_course_client_f_key)
#execute_query(connection, create_takeCourse_table)

pop_teacher = """
INSERT INTO teacher VALUES 
(3, 'dncasjkvn', 'fvs', 'ENG', NULL, '1989-05-03', 12345, '+98765432'),
(4, 'skdvmks', 'fvd', 'ENG', NULL, '1989-05-04', 23456, '+98765432'),
(5, 'lvsforeal', 'ewkfmcs', 'ENG', NULL, '1989-05-05', 34567, '+98765432'),
(6, 'fvms', 'nvskfn', 'ENG', NULL, '1989-05-06', 45678, '+98765432'),
(7, 'vsfdv', 'fvndk', 'ENG', NULL, '1989-05-07', 56789, '+98765432'),
(8, 'fcska', 'fcsdzk', 'ENG', NULL, '1989-05-08', 98764, '+98765432');


"""
#execute_query(connection, pop_teacher)

pop_client = """
INSERT INTO client VALUES
(101, 'business1', 'address1', 'NGO'),
(102, 'business2', 'address2', 'retail'),
(103, 'business3', 'address3', 'joint'),
(104, 'business4', 'address4', 'ecomm'),
(105, 'business5', 'address5', 'banking');
"""
#execute_query(connection, pop_client)
pop_participant = """
INSERT INTO participant VALUES
(101,'loreal1','ipsum1','+26758699',101),
(102,'loreal2','ipsum2','+26758691',102),
(103,'loreal3','ipsum3','+26758692',103),
(104,'loreal4','ipsum4','+26758693',101),
(105,'loreal5','ipsum5','+26758694',104),
(106,'loreal6','ipsum6','+26758695',105),
(107,'loreal7','ipsum7','+26758696',105),
(108,'loreal8','ipsum8','+26758697',103);

"""
#execute_query(connection, pop_participant)
pop_course = """
INSERT INTO course VALUES
(12, 'English', 'ENG', 'A1', 10, '2020-02-01', TRUE,  1, 105),
(13, 'Beginner English', 'ENG', 'A2', 40, '2019-11-12',  FALSE, 6, 101),
(14, 'Intermediate English', 'ENG', 'B2', 40, '2019-11-12', FALSE, 6, 101),
(15, 'Advanced English', 'ENG', 'C1', 40, '2019-11-12', FALSE, 6, 101),
(16, 'Mandarin', 'MAN', 'B1', 15, '2020-01-15', TRUE, 3, 103),
(17, 'French', 'FRA', 'B1',  18, '2020-04-03', FALSE, 2, 101),
(18, 'Deutsch', 'DEU', 'A2', 8, '2020-02-14', TRUE, 4, 102),
(19, 'Intermediate English', 'ENG', 'B2', 10, '2020-03-29', FALSE, 1, 104),
(20, 'Russian', 'RUS', 'C1',  4, '2020-04-08',  FALSE, 5, 103);
"""
#execute_query(connection, pop_course)
pop_takescourse = """
INSERT INTO takecourse VALUES
(101, 15),
(101, 17),
(102, 17),
(103, 18),
(104, 18),
(105, 18),
(106, 13),
(107, 13),
(108, 13),
(101, 14),
(102, 15),
(103, 16),
(104, 20),
(105, 16),
(106, 12),
(107, 19),
(108, 19);
"""
insert_many = """
INSERT INTO teacher( teacher_id,first_name,last_name,language_1,language_2,dob,tax_id,phone_no) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""
# use %s only for any type of data. it acts only as a placeholder. Do not use %d for int 
val = [
    (9, 'sdgdf', 'fvnergedk', 'ENG', None, '1989-05-07', 43216, '+98765432'),
    (10, 'fcfvdfska', 'fctgtrsdzk', 'ENG', None, '1989-05-08', 76523, '+98765432')
]

execute_list_query(connection, insert_many, val)

#execute_query(connection, pop_takescourse)
display_table = """
SELECT * FROM teacher;

"""
results = query_fetch(connection, display_table)
for result in results:
    print(result)

get_columns_name = """
SELECT column_name FROM information_schema.columns WHERE table_name='teacher';
"""
columns_name = [col_id[0] for col_id in query_fetch(connection, get_columns_name)]

df = pd.DataFrame(results, columns=columns_name) # load table to a dataframe
print(df)

connection.close()

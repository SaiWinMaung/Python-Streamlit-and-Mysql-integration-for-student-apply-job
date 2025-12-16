import streamlit as st
import mysql.connector
from mysql.connector import Error
def test_connection():
    try:
        connection = mysql.connector.connect(
            host=st.secrets["mysql"]["localhost"],
            user=st.secrets["mysql"]["root"],
            password=st.secrets["mysql"]["sai345543"],
            database=st.secrets["mysql"]["student_db"],
            auth_plugin="caching_sha2_password",
        )
        if connection.is_connected():
            print("Connection is successful")
            return connection
    except Error as e:
        print(f"Error : {e}")
AddStudent = st.Page('addstudent.py', title= 'Add Student')
StudentList = st.Page('studentlist.py', title= 'Student List')
StudentReport = st.Page('studentreport.py', title= 'Student Report ')

page = st.navigation(
    {
        'Add Student:' : [AddStudent],
        'Student List:' : [StudentList],
        'Student Report:' : [StudentReport]
    }
)

page.run()

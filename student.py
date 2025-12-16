import streamlit as st

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

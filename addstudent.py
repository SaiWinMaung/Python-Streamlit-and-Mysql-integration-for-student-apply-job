import streamlit as st
import mysql.connector
from mysql.connector import Error

st.title('Add Student')
def test_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sai345543",
            database="db_student",
            auth_plugin="caching_sha2_password",
        )
        if connection.is_connected():
            print("Connection is successful")
            return connection
    except Error as e:
        print(f"Error : {e}")


def save_student(name, gender, major, grade):
    conn = test_connection()
    cursor = conn.cursor()
    query = """insert into studentlist(name,gender,major,grade) values (%s,%s,%s,%s)"""
    cursor.execute(query,(name, gender, major, grade))
    conn.commit()
    st.success('Student Added')
    conn.close()


with st.form("Add student"):
    name = (st.text_input("Student Name", placeholder="Enter Student Name"))
    gender = (st.radio("Please choose gender", ["Male", "Female"]))
    major = (
        st.selectbox(
            "Please select one major",
            [
                "Civil",
                "Electronic",
                "Electrical",
                "Mechanical",
                "IT",
                "Mechatronic",
                "Textile",
            ],
        )
    )
    grade = st.selectbox("Please select your grade", ["A", "B", "C", "D", "E"])
    submit = st.form_submit_button("Save")
    if submit:
        save_student(name, gender, major, grade)
        st.rerun()



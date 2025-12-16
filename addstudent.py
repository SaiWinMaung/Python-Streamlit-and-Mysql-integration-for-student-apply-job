import streamlit as st
from db import get_engine

st.title('Add Student')

def save_student(name, gender, major, grade):
    conn = get_engine()
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



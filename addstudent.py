import streamlit as st
from sqlalchemy import text
from db import get_engine

st.title('Add Student')
engine = get_engine()
def save_student(name, gender, major, grade):
    query = text("""
        INSERT INTO studentlist (name, gender, major, grade)
        VALUES (:name, :gender, :major, :grade)
    """)
    with engine.begin() as conn:
        conn.execute(
            query,
            {"name": name, "gender": gender, "major": major, "grade": grade}
        )

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



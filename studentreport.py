import streamlit as st
from studentlist import show_data
import plotly.express as px

st.title('Student Report')


data = show_data()

gender_count = data['gender'].value_counts().reset_index()
gender_count.columns = ['Gender', 'Count']

fig = px.pie(
    gender_count,
    names= 'Gender',
    values= 'Count',
    title = 'Student Gender Distribution'
)
st.plotly_chart(fig, use_container_width=True)

#bar chart in major

major_count = data['major'].value_counts().reset_index()
major_count.columns =['Major', 'Count']

fig = px.bar(
    major_count,
    x= 'Major',
    y= 'Count',
    title ='Students in each major',
    labels={
        'Count': 'Total Students'
    },
    text ='Count'
)
st.plotly_chart(fig, use_container_width=True)


#bar chart with gender and grade
gender_grade_counts = data.groupby(["grade", "gender"]).size().reset_index(name="count")

fig = px.bar(
    gender_grade_counts,
    x="grade",
    y="count",
    color="gender",
    barmode="group",  # 'stack' for stacked bars
    labels={"grade": "Grade", "count": "Number of Students", "gender": "Gender"},
    title="Student High Rank by Gender"
)

st.plotly_chart(fig, use_container_width=True)

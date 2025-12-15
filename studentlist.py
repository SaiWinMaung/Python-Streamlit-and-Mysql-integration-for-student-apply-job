import streamlit as st
from addstudent import test_connection
import pandas as pd

st.title('List of students who will apply for jobs')
def show_data():
    conn = test_connection()
    query = "select * from studentlist order by id "
    df = pd.read_sql(query, conn)
    return df

df = show_data()
df.insert(0, "No.", range(1, len(df) + 1))
df["Delete"] = False
edited_df = st.data_editor(
    df,
    hide_index=True,
    column_config={
        "Delete": st.column_config.CheckboxColumn(
            "Delete",
            help="Check to delete row"
        )
    },
    disabled=["id", "name", "gender", "major", "grade"]
)
if st.button("Delete Selected Rows"):
    rows_to_delete = edited_df[edited_df["Delete"] == True]
    conn = test_connection()
    cursor = conn.cursor()
    for _, row in rows_to_delete.iterrows():
        cursor.execute("DELETE FROM studentlist WHERE id = %s", (row["id"],))

    conn.commit()
    st.success("Selected rows deleted successfully!")
    st.rerun()

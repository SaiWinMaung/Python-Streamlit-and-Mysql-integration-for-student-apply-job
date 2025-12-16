import streamlit as st
from sqlalchemy import text
from db import get_engine
import pandas as pd

st.title('List of students who will apply for jobs')

def show_data():
    engine = get_engine()
    with engine.connect() as conn:
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
    if not rows_to_delete.empty:
        engine = get_engine()
        delete_query = text("DELETE FROM studentlist WHERE id = :id")
        with engine.begin() as conn:  # begins a transaction and commits automatically
            for _, row in rows_to_delete.iterrows():
                conn.execute(delete_query, {"id": row["id"]})

        st.success("Selected rows deleted successfully!")
        st.rerun()
from sqlalchemy import create_engine
import streamlit as st

def get_engine():
    user = st.secrets["mysql"]["root"]
    password = st.secrets["mysql"]["sai345543"]
    host = st.secrets["mysql"]["127.0.0.1"]
    database = st.secrets["mysql"]["db_student"]
    port = st.secrets["mysql"]["3306"]
    

    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

    engine = create_engine(
        db_url,
        pool_pre_ping=True
    )
    return engine


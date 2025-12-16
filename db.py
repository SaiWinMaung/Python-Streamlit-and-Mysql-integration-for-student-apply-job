from sqlalchemy import create_engine
import streamlit as st

def get_engine():
    user = st.secrets["mysql"]["user"]
    password = st.secrets["mysql"]["password"]
    host = st.secrets["mysql"]["host"]
    database = st.secrets["mysql"]["database"]
    port = st.secrets["mysql"]["port"]  
    

    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

    engine = create_engine(
        db_url,
        pool_pre_ping=True
    )
    return engine


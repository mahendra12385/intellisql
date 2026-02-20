import streamlit as st
import os
import sqlite3
import pandas as pd
from google import genai
from dotenv import load_dotenv

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY not found in .env file")
    st.stop()

# Create Gemini client
client = genai.Client(api_key="AIzaSyAkU3ObfomkSNJk4WIMq237UvtLjCo9clI")

# -------------------------
# Prompt for SQL generation
# -------------------------
PROMPT = """
You are an expert in converting English questions into SQL queries.

Database name: STUDENT

Columns:
- NAME (TEXT)
- CLASS (TEXT)
- SECTION (TEXT)
- MARKS (INTEGER)

Rules:
- Only generate SELECT queries
- Do NOT generate INSERT, UPDATE, DELETE, DROP
- Do NOT include ``` or the word sql
- Output only pure SQL

Examples:

Question: Show all students
SQL: SELECT * FROM STUDENT;

Question: Show students with marks above 80
SQL: SELECT * FROM STUDENT WHERE MARKS > 80;
"""

# -------------------------
# Gemini function
# -------------------------
def get_gemini_response(question):

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"{PROMPT}\n\nQuestion: {question}"
        )

        sql = response.text.strip()

        return sql

    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------
# Execute SQL query
# -------------------------
def run_sql_query(sql):

    if not sql.lower().startswith("select"):
        raise Exception("Only SELECT queries are allowed")

    conn = sqlite3.connect("student.db")

    df = pd.read_sql_query(sql, conn)

    conn.close()

    return df


# -------------------------
# Pages
# -------------------------

def home_page():

    st.title("🚀 IntelliSQL")
    st.subheader("AI-powered SQL Assistant")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/2920/2920349.png",
            width=250
        )

    with col2:
        st.markdown("""
        ### Features
        
        - Convert English to SQL  
        - Execute SQL instantly  
        - Powered by Google Gemini AI  
        - SQLite database support  
        """)


def query_page():

    st.title("🧠 Intelligent Query Assistance")

    question = st.text_input(
        "Enter your question:",
        placeholder="Example: show all students"
    )

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question")
            return

        sql = get_gemini_response(question)

        if sql.startswith("Error"):
            st.error(sql)
            return

        st.subheader("Generated SQL:")
        st.code(sql, language="sql")

        try:
            df = run_sql_query(sql)

            st.subheader("Query Result:")
            st.dataframe(df)

        except Exception as e:
            st.error(str(e))


def about_page():

    st.title("About IntelliSQL")

    st.write("""
    IntelliSQL converts natural language into SQL queries using Google's Gemini AI.

    It allows users to query databases without writing SQL manually.
    """)

    st.image(
        "https://cdn-icons-png.flaticon.com/512/9850/9850877.png",
        width=200
    )


# -------------------------
# Navigation
# -------------------------
def main():

    st.set_page_config(
        page_title="IntelliSQL",
        layout="wide"
    )

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Home", "Query Assistant", "About"]
    )

    if page == "Home":
        home_page()

    elif page == "Query Assistant":
        query_page()

    elif page == "About":
        about_page()


# -------------------------
# Run app
# -------------------------
if __name__ == "__main__":
    main()


    

# intellisql
# 🧠 Intelligent Query Assistance using Streamlit, Gemini AI, and SQLite

## 📌 Project Overview

The **Intelligent Query Assistance** project is an AI-powered web application that allows users to interact with a database using natural language instead of writing SQL queries manually.

This application uses **Google Gemini AI** to convert user questions into SQL queries and retrieves results from a **SQLite database**, displaying them through a clean **Streamlit web interface**.

This project demonstrates the integration of:

* Generative AI (Google Gemini)
* Database systems (SQLite)
* Web application development (Streamlit)
* Natural Language Processing (NLP)

---

## 🚀 Features

* ✅ Convert natural language questions into SQL queries
* ✅ Automatically execute SQL queries on SQLite database
* ✅ Display results in user-friendly format
* ✅ Interactive Streamlit web interface
* ✅ Fast and lightweight database (SQLite)
* ✅ Secure API key integration
* ✅ Easy to deploy and run locally

---

## 🛠️ Technologies Used

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| Python            | Programming language               |
| Streamlit         | Web application framework          |
| SQLite            | Database                           |
| Google Gemini AI  | Natural language to SQL conversion |
| google-genai      | Gemini API client                  |
| dotenv (optional) | Secure API key management          |

---

## 📂 Project Structure

```
IntelliSQL/
│
├── app.py              # Main Streamlit application
├── sql.py              # Database creation and helper functions
├── data.db             # SQLite database file
├── requirements.txt    # Required Python packages
├── .env                # API key file (not uploaded to GitHub)
└── README.md           # Project documentation
```

---

## ⚙️ Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/intelligent-query-assistance.git

cd intelligent-query-assistance
```

---

### Step 2: Create virtual environment (recommended)

```bash
python -m venv venv

source venv/bin/activate    # Mac/Linux

venv\Scripts\activate       # Windows
```

---

### Step 3: Install required packages

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install streamlit google-genai python-dotenv
```

---

## 🔑 Step 4: Setup Gemini API Key

Get API key from:

https://ai.google.dev/

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

Or directly add in code:

```python
client = genai.Client(api_key="your_api_key_here")
```

---

## 🗄️ Database Schema

Example table: **students**

| Column | Type    |
| ------ | ------- |
| id     | INTEGER |
| name   | TEXT    |
| age    | INTEGER |
| grade  | TEXT    |

---

## ▶️ Running the Application

Run Streamlit app:

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 💬 Example Queries

You can type questions like:

```
show all students

list students with age greater than 20

show student names

get students with grade A
```

Gemini converts them into SQL like:

```sql
SELECT * FROM students;
```

---

## 🧠 How It Works

1. User enters question in Streamlit UI
2. Gemini AI converts question → SQL query
3. SQLite executes SQL query
4. Results displayed in web interface

---

## 📸 Example Output

```
User Input:
show all students

Generated SQL:
SELECT * FROM students;

Output:
(1, John, 20, A)
(2, Mary, 21, B)
```

---

## ⚠️ Troubleshooting

### Error: quota exceeded

Solution:

* Create new Gemini API key
* Replace in code or .env file

---

### Error: model not found

Use:

```python
model="gemini-2.0-flash"
```

---

## 🌐 Future Improvements

* Add chat interface
* Support multiple tables
* Deploy online (Streamlit Cloud / AWS)
* Add authentication
* Export results to CSV

---

## 📦 Requirements

```
streamlit
google-genai
python-dotenv
sqlite3
```

---

## 👨‍💻 Author

Mahendra Karuturi

---

## 📄 License

This project is for educational purposes.

---

## ⭐ GitHub Submission Checklist

Before submitting:

* ✅ Code runs without errors
* ✅ requirements.txt included
* ✅ README.md included
* ✅ API key NOT uploaded
* ✅ .env added to .gitignore

---

## 🎯 Conclusion

This project successfully demonstrates how AI can simplify database interaction by allowing users to query databases using natural language, improving usability and efficiency.

---

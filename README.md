# ATS Resume Analyzer

An AI-powered resume analyzer that compares a candidate's resume with a job description and provides insights into **ATS compatibility, matching skills, missing skills, keywords, and areas for improvement**.

## 🚀 Features

* 📄 Upload resume in PDF format
* 📝 Enter a job description
* 🔍 Analyze resume against the job
* 🧠 Identify matching and missing skills
* 📊 Generate estimated ATS match percentage
* 🔑 Find matching and missing keywords
* 💡 Get personalized skill improvement suggestions

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Groq API**
* **Qwen LLM**
* **PyPDF2**
* **python-dotenv**

## 📂 Project Structure

```text
ATS-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```
git clone <your-repository-url>
cd ATS-Resume-Analyzer
```

Create and activate a virtual environment:

```
python -m venv .venv
```

Windows:

```
.\.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the local Streamlit URL in your browser.

## 📊 Analysis Options

The application provides three analysis modes:

1. **Resume Analysis** – Reviews the resume against the job description.
2. **Skill Improvement** – Identifies missing and partially demonstrated skills.
3. **Percentage Match** – Provides an estimated ATS compatibility and keyword match.

> **Note:** The ATS percentage is an AI-generated estimate and does not represent the score of any company's proprietary ATS.

## 🔮 Future Improvements

* DOCX resume support
* OCR for scanned resumes
* Resume optimization
* Semantic skill matching
* ATS-friendly resume generation
* Downloadable analysis reports



LinkedIn: `<your-linkedin-profile>`

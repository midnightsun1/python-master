import streamlit as st
import sys
import os
from io import StringIO
import contextlib
import time

# Robust import for curriculum
try:
    from python_master.curriculum import curriculum
except ImportError:
    try:
        from curriculum import curriculum
    except ImportError:
        # Fallback to local import path
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from curriculum import curriculum

st.set_page_config(
    page_title="Python Master - Roman Urdu",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =================== CUSTOM CSS ===================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main-title {
        background: linear-gradient(135deg, #2E8B57 0%, #1f77b4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 54px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #4B5563;
        margin-bottom: 30px;
        font-weight: 300;
    }
    
    .topic-title {
        color: #2E8B57;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    
    .theory-text {
        font-size: 16px;
        color: #374151;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .teacher-tip {
        background: linear-gradient(145deg, #FFFBEB, #FEF3C7);
        border-radius: 12px;
        padding: 16px;
        margin: 15px 0;
        border-left: 5px solid #F59E0B;
        color: #92400E;
        font-size: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .task-box {
        background: linear-gradient(145deg, #EFF6FF, #DBEAFE);
        border-radius: 12px;
        padding: 16px;
        margin: 15px 0;
        border-left: 5px solid #3B82F6;
        color: #1E40AF;
        font-size: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .footer {
        text-align: center;
        color: #6B7280;
        margin-top: 50px;
        padding: 25px;
        border-top: 1px solid #E5E7EB;
    }
    
    .progress-text {
        font-size: 14px;
        color: #374151;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# =================== CODE RUNNER ===================
def run_user_code(code, inputs=""):
    """User ka Python code safely run karo. input() ke liye values bhi support karta hai."""
    if not code.strip():
        return "", "Code khali hai.", 0
    
    # Process inputs line by line (preserving blank inputs if intended)
    input_lines = inputs.split("\n")
    input_iter = iter(input_lines)
    
    def custom_input(prompt=""):
        try:
            return next(input_iter)
        except StopIteration:
            raise EOFError("Input khatam ho gaya. Neeche 'Inputs' box mein value daalo.")
    
    output = StringIO()
    env = {
        "__builtins__": __builtins__,
        "input": custom_input
    }
    
    start = time.time()
    try:
        # NOTE: Standard exec runs in the local Streamlit process context.
        # Secure this if deploying publicly (e.g. by running in Docker or restricted sandbox).
        with contextlib.redirect_stdout(output):
            exec(code, env)
        elapsed = time.time() - start
        return output.getvalue(), None, elapsed
    except Exception as e:
        elapsed = time.time() - start
        return output.getvalue(), f"{type(e).__name__}: {str(e)}", elapsed


# Flatten topics for progress tracking
all_topics = []
for level, topics in curriculum.items():
    for topic in topics:
        all_topics.append((level, topic))

# Initialize session states
if "completed" not in st.session_state:
    st.session_state.completed = set()

if "run_results" not in st.session_state:
    st.session_state.run_results = {}

if "example_results" not in st.session_state:
    st.session_state.example_results = {}

if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = {}

# =================== UI: TITLE ===================
st.markdown('<div class="main-title">🐍 Python Master</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Roman Urdu mein Zero se Hero — Python + AI/ML sab kuch yahin!</div>', unsafe_allow_html=True)

# =================== SIDEBAR ===================
st.sidebar.title("📚 Navigation")

page = st.sidebar.radio(
    "Select karo:",
    ["🎓 Python Course", "📋 Cheat Sheet", "🛠️ Practice Projects", "🤖 AI/ML Roadmap"]
)

# Progress
completed_count = len(st.session_state.completed)
total_count = len(all_topics)
progress = completed_count / total_count if total_count > 0 else 0
st.sidebar.progress(progress)
st.sidebar.markdown(f"<div class='progress-text'>Progress: {completed_count}/{total_count} topics</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("""
👨‍🏫 **Teacher ka paigham:**
- Roz 1-2 topics karo
- Har topic ke baad code likh kar dekho
- Projects banao — yeh confidence badhata hai
- Galatiyan hongi — wohi seekhne ka rasta hai!
""")

# =================== RENDER: PYTHON COURSE ===================
if page == "🎓 Python Course":
    tab1, tab2, tab3, tab4 = st.tabs(list(curriculum.keys()))
    
    tabs_map = {
        "🌱 Beginner": tab1,
        "🚀 Intermediate": tab2,
        "🔥 Advanced": tab3,
        "🤖 AI/ML Basics": tab4
    }
    
    for level, tab in tabs_map.items():
        with tab:
            st.markdown(f"## {level}")
            st.markdown(f"**Total topics:** {len(curriculum[level])}")
            
            for idx, topic in enumerate(curriculum[level]):
                topic_id = f"{level}|{topic['title']}"
                
                # Standard Container with border is valid HTML and prevents DOM breakdown
                with st.container(border=True):
                    
                    col1, col2 = st.columns([0.8, 0.2])
                    with col1:
                        st.markdown(f'<div class="topic-title">{topic["title"]}</div>', unsafe_allow_html=True)
                    with col2:
                        if topic_id in st.session_state.completed:
                            if st.button("✅ Completed", key=f"comp_{topic_id}"):
                                st.session_state.completed.discard(topic_id)
                                st.rerun()
                        else:
                            if st.button("Mark Complete", key=f"comp_{topic_id}"):
                                st.session_state.completed.add(topic_id)
                                st.rerun()
                    
                    st.markdown(f'<div class="theory-text">{topic["theory"]}</div>', unsafe_allow_html=True)
                    
                    st.markdown("**👨‍🏫 Misaal (Example):**")
                    st.code(topic["example"], language="python")
                    
                    col_run, col_inputs = st.columns([0.3, 0.7])
                    with col_run:
                        run_example = st.button(f"▶ Misaal Chalao", key=f"ex_run_{topic_id}")
                    with col_inputs:
                        example_inputs = topic.get("example_inputs", "")
                        st.caption("Agar misaal input mangay to value neeche dalo")
                    
                    example_input_text = st.text_area(
                        "Misaal ke liye inputs (input() ke liye, har line mein aik value):",
                        value=example_inputs,
                        key=f"ex_inp_{topic_id}",
                        height=60
                    )
                    
                    if run_example:
                        output, error, elapsed = run_user_code(topic["example"], example_input_text)
                        st.session_state.example_results[topic_id] = {
                            "output": output,
                            "error": error,
                            "elapsed": elapsed
                        }
                    
                    # Persist example outputs
                    ex_res = st.session_state.example_results.get(topic_id)
                    if ex_res:
                        if ex_res["error"]:
                            st.error(f"⚠️ {ex_res['error']}")
                        else:
                            st.success(f"✅ {ex_res['elapsed']:.3f} seconds mein chala")
                            st.text_area("Output", ex_res["output"], height=120, key=f"ex_out_val_{topic_id}")
                    
                    # Teacher tip
                    st.markdown(f'<div class="teacher-tip">{topic["tip"]}</div>', unsafe_allow_html=True)
                    
                    # Practice task
                    st.markdown(f'<div class="task-box">**📝 Ab aapki baari (Practice Task):**<br>{topic["task"]}</div>', unsafe_allow_html=True)
                    
                    # Practice code editor
                    user_code = st.text_area(
                        "✍️ Yahan apna code likho:",
                        height=160,
                        key=f"code_{topic_id}",
                        placeholder="# Apna Python code yahan likho..."
                    )
                    
                    user_inputs = st.text_area(
                        "🔹 Inputs (agar aapka code input() use karta hai, har line mein aik value):",
                        height=60,
                        key=f"inp_{topic_id}"
                    )
                    
                    c1, c2, c3 = st.columns([0.25, 0.25, 0.5])
                    with c1:
                        run_user = st.button(f"🚀 Apna Code Chalao", key=f"run_{topic_id}")
                    with c2:
                        if st.button(f"💡 Hint", key=f"hint_{topic_id}"):
                            st.info("Misaal ko dheyan se parho. Ussi pattern ko apni task par lagao. Galat hona bhi seekhna hai!")
                    with c3:
                        if st.button(f"🧹 Code Saaf Karo", key=f"clear_{topic_id}"):
                            st.session_state[f"code_{topic_id}"] = ""
                            if topic_id in st.session_state.run_results:
                                del st.session_state.run_results[topic_id]
                            st.rerun()
                    
                    if run_user:
                        output, error, elapsed = run_user_code(user_code, user_inputs)
                        st.session_state.run_results[topic_id] = {
                            "output": output,
                            "error": error,
                            "elapsed": elapsed
                        }
                    
                    # Persist user outputs
                    user_res = st.session_state.run_results.get(topic_id)
                    if user_res:
                        if user_res["error"]:
                            st.error(f"⚠️ {user_res['error']}")
                            if user_res["output"].strip():
                                st.text_area("Partial Output (error se pehle)", user_res["output"], height=80, key=f"user_pout_val_{topic_id}")
                        else:
                            st.success(f"✅ Code chal gaya! ({user_res['elapsed']:.3f}s)")
                            st.text_area("Aapka Output", user_res["output"], height=140, key=f"user_out_val_{topic_id}")
                    
                    # Quiz
                    with st.expander("🎯 Quick Quiz"):
                        quiz = topic["quiz"]
                        user_ans = st.radio(quiz["question"], quiz["options"], key=f"quiz_opt_{topic_id}")
                        
                        if st.button("Jawab Check Karo", key=f"quiz_check_{topic_id}"):
                            is_correct = (user_ans == quiz["answer"])
                            st.session_state.quiz_results[topic_id] = {
                                "is_correct": is_correct,
                                "answer": quiz["answer"]
                            }
                        
                        quiz_res = st.session_state.quiz_results.get(topic_id)
                        if quiz_res:
                            if quiz_res["is_correct"]:
                                st.success("🎉 Sahi jawab! Aap achay learner ban rahe ho.")
                            else:
                                st.error(f"❌ Ghalat. Sahi jawab: **{quiz_res['answer']}**")

# =================== RENDER: CHEAT SHEET ===================
elif page == "📋 Cheat Sheet":
    st.markdown("## 📋 Python Cheat Sheet")
    st.markdown("Yeh woh sab kuch hai jo har Python learner ko yaad rehna chahiye.")
    
    cheat_data = {
        "Variables & Data Types": [
            "x = 10  # int",
            "y = 3.14  # float",
            "name = 'Ali'  # str",
            "is_ok = True  # bool",
            "fruits = ['saib', 'kela']  # list",
            "point = (2, 3)  # tuple",
            "data = {'a': 1}  # dict"
        ],
        "Operators": [
            "a + b, a - b, a * b, a / b",
            "a // b  # floor division",
            "a % b   # remainder",
            "a ** b  # power",
            "a == b, a != b, a > b, a < b",
            "a and b, a or b, not a"
        ],
        "Conditions": [
            "if condition:",
            "elif condition:",
            "else:"
        ],
        "Loops": [
            "for i in range(10):",
            "for item in list:",
            "while condition:",
            "break  # loop roko",
            "continue  # agli iteration",
            "pass  # kuch nahi"
        ],
        "List Methods": [
            "lst.append(x)",
            "lst.insert(i, x)",
            "lst.remove(x)",
            "lst.pop()",
            "lst.sort()",
            "lst.reverse()",
            "len(lst), sum(lst), max(lst), min(lst)"
        ],
        "String Methods": [
            "s.upper(), s.lower()",
            "s.strip()",
            "s.replace('a', 'b')",
            "s.split(',')",
            "s.startswith('a')",
            "len(s)"
        ],
        "Dictionary": [
            "d['key'] = value",
            "d.get('key')",
            "d.keys(), d.values(), d.items()",
            "for k, v in d.items():"
        ],
        "Functions": [
            "def func(a, b=5):",
            "    return a + b",
            "func(10)  # call",
            "lambda x: x**2"
        ],
        "File Handling": [
            "with open('file.txt', 'r') as f:",
            "    data = f.read()",
            "with open('file.txt', 'w') as f:",
            "    f.write('text')"
        ],
        "OOP": [
            "class MyClass:",
            "    def __init__(self, x):",
            "        self.x = x",
            "    def method(self):",
            "        pass",
            "obj = MyClass(10)"
        ],
        "Error Handling": [
            "try:",
            "    # code",
            "except ValueError:",
            "    # handle",
            "finally:",
            "    # always"
        ],
        "Comprehension": [
            "[x**2 for x in range(10)]",
            "[x for x in lst if x > 5]",
            "{k:v for k,v in data.items()}"
        ],
        "Useful Modules": [
            "import math, random, datetime",
            "import json, csv, re",
            "import requests  # external",
            "import numpy as np",
            "import pandas as pd",
            "from sklearn import ..."
        ]
    }
    
    cols = st.columns(3)
    items = list(cheat_data.items())
    for i, (category, items_list) in enumerate(items):
        with cols[i % 3]:
            with st.expander(f"**{category}**", expanded=True):
                for item in items_list:
                    st.markdown(f'<div class="cheat-item" style="background: #fff; border-radius: 8px; padding: 10px; margin: 6px 0; border: 1px solid #ddd;"><code>{item}</code></div>', unsafe_allow_html=True)

# =================== RENDER: PROJECTS ===================
elif page == "🛠️ Practice Projects":
    st.markdown("## 🛠️ Practice Projects")
    st.markdown("Har project ko apne level ke hisaab se karo. Yeh sab kuch combined seekhne ka best tareeqa hai.")
    
    projects = [
        ("Beginner", "🧮 Calculator", "Basic input, operators, conditions use karke calculator banao."),
        ("Beginner", "🎮 Number Guessing Game", "Computer aik number sochay, user guess kare. Loops aur conditions use karo."),
        ("Beginner", "📝 To-Do List (Simple)", "List use karke tasks add/remove/show karo."),
        ("Intermediate", "📒 Contact Book", "Dictionary use karke naam → phone number store karo, search karo."),
        ("Intermediate", "💰 Expense Tracker", "File ya dictionary mein expenses save karo, total aur category wise report banao."),
        ("Intermediate", "🔐 Password Generator", "Random module se strong password generate karo."),
        ("Intermediate", "📊 CSV Analyzer", "Pandas use karke CSV file read karo, summary statistics nikalo."),
        ("Advanced", "🌐 Weather App", "API se weather data lo aur display karo."),
        ("Advanced", "🗄️ Student Management System", "SQLite database use karke CRUD operations banao."),
        ("Advanced", "🤖 Spam Email Classifier", "Scikit-learn se text classify karo: spam ya not spam."),
        ("Advanced", "🏠 House Price Predictor", "Linear regression se ghar ka price predict karo."),
        ("Advanced", "🧠 Image Classifier (Basic)", "Neural network se handwritten digits recognize karo (MNIST).")
    ]
    
    level_filter = st.selectbox("Level select karo:", ["Sab", "Beginner", "Intermediate", "Advanced"])
    
    for level, name, desc in projects:
        if level_filter == "Sab" or level_filter == level:
            with st.container(border=True):
                st.markdown(f"**{name}**  \n*{level}*  \n{desc}")

# =================== RENDER: AI/ML ROADMAP ===================
elif page == "🤖 AI/ML Roadmap":
    st.markdown("## 🤖 AI/ML Seekhne Ka Roadmap")
    st.markdown("Agar aap AI/ML expert banna chahte hain, to yeh rasta follow karo.")
    
    roadmap = [
        ("Python Strong Karo", "Variables, loops, functions, OOP, file handling achay se seekho.", "1-2 months"),
        ("Math Basics", "Linear Algebra, Calculus, Statistics basics. Sirf ML ke liye zaroori hissay.", "1 month"),
        ("Numpy & Pandas", "Data manipulation ka king combo.", "2-3 weeks"),
        ("Data Visualization", "Matplotlib, Seaborn, Plotly se graphs aur dashboards banao.", "2 weeks"),
        ("ML Algorithms", "Linear Regression, Logistic Regression, Decision Trees, SVM, KNN, Clustering.", "2 months"),
        ("Model Evaluation", "Cross-validation, precision, recall, F1, ROC-AUC, hyperparameter tuning.", "3-4 weeks"),
        ("Feature Engineering", "Data cleaning, scaling, encoding, feature selection.", "1 month"),
        ("Deep Learning", "Neural Networks, TensorFlow/Keras, CNN, RNN basics.", "2-3 months"),
        ("Projects", "Minimum 3-4 end-to-end projects GitHub par upload karo.", "Continuous"),
        ("Deployment", "Flask/Streamlit, Docker, cloud (AWS/Heroku) par model deploy karo.", "1 month")
    ]
    
    for i, (title, desc, duration) in enumerate(roadmap, 1):
        with st.container(border=True):
            st.markdown(f"""
            <div class="topic-title">Step {i}: {title}</div>
            <p>{desc}</p>
            <p><b>⏱️ Duration:</b> {duration}</p>
            """, unsafe_allow_html=True)
    
    st.info("🎯 Salah: Pehle Python mazboot karo, phir step by step ML ki taraf barho. Projects sab se zaroori hain!")

# =================== FOOTER ===================
st.markdown("---")
st.markdown("""
<div class="footer">
    <h3>🐍 Python Master — Roman Urdu Learning App</h3>
    <p>Complete Python + AI/ML basics in one place.</p>
    <p><b>Yaad rakho:</b> Har expert kabhi beginner tha. Rojana practice karo, projects banao, aur shuru karo! 💪🚀</p>
</div>
""", unsafe_allow_html=True)

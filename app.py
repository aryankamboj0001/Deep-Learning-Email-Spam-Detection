import streamlit as st
import pickle
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color:white;
}

textarea{
    font-size:18px !important;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    background:#2563eb;
    color:white;
}

.stButton>button:hover{
    background:#1d4ed8;
}

.block{
    padding:20px;
    border-radius:15px;
    background:#1e293b;
    border:1px solid #374151;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Download NLTK
# -----------------------------
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

# -----------------------------
# Load Files
# -----------------------------
model = load_model("gru_model.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("config.pkl", "rb") as f:
    config = pickle.load(f)

with open("label_mapping.pkl", "rb") as f:
    label_mapping = pickle.load(f)

MAX_LENGTH = config["max_length"]

stops = set(stopwords.words("english"))

# -----------------------------
# History
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("📧 AI Spam Detector")

    st.markdown("---")

    st.write("### Model")
    st.success("GRU Deep Learning")

    st.write("### Tech Stack")

    st.write("""
- TensorFlow
- Streamlit
- NLTK
- Python
    """)

    st.markdown("---")

    st.subheader("Prediction History")

    if len(st.session_state.history)==0:
        st.write("No predictions yet.")
    else:
        for item in reversed(st.session_state.history):
            st.write(item)

    st.markdown("---")

    st.caption("Developed by Aryan Kumar")

# -----------------------------
# Preprocessing
# -----------------------------
def remove_special(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def clean_text(text):
    text=text.lower()
    text=remove_special(text)

    words=word_tokenize(text)

    words=[word for word in words if word not in stops]

    return " ".join(words)

# -----------------------------
# Main UI
# -----------------------------
st.title("📧 AI Email Spam Detector")

st.caption(
    "Detect Spam Emails using a Deep Learning GRU Model."
)

email = st.text_area(
    "Paste your email below",
    height=250
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🚀 Detect Spam"):

    if email.strip()=="":

        st.warning("Please enter an email.")

    else:

        st.subheader("📊 Email Statistics")

        c1,c2,c3=st.columns(3)

        c1.metric("Words",len(email.split()))
        c2.metric("Characters",len(email))
        c3.metric("Lines",len(email.splitlines()))

        cleaned=clean_text(email)

        sequence=tokenizer.texts_to_sequences([cleaned])

        padded=pad_sequences(
            sequence,
            maxlen=MAX_LENGTH,
            padding="post"
        )

        with st.spinner("Analyzing Email..."):

            prediction=model.predict(
                padded,
                verbose=0
            )[0][0]

        spam_prob=float(prediction)
        ham_prob=1-spam_prob

        st.markdown("---")

        if spam_prob>=0.5:

            st.error("🚨 Spam Email Detected")

        else:

            st.success("✅ Legitimate Email")

        st.subheader("Confidence")

        col1,col2=st.columns(2)

        with col1:

            st.metric(
                "Spam",
                f"{spam_prob*100:.2f}%"
            )

            st.progress(spam_prob)

        with col2:

            st.metric(
                "Ham",
                f"{ham_prob*100:.2f}%"
            )

            st.progress(ham_prob)

        st.subheader("Processed Text")

        st.code(cleaned)

        report=f"""
AI Email Spam Detection Report

Prediction : {"Spam" if spam_prob>=0.5 else "Ham"}

Spam Probability : {spam_prob*100:.2f}%

Ham Probability : {ham_prob*100:.2f}%

Processed Text

{cleaned}
"""

        st.download_button(
            "📄 Download Report",
            report,
            file_name="spam_prediction_report.txt"
        )

        st.session_state.history.append(
            f'{"🚨 Spam" if spam_prob>=0.5 else "✅ Ham"} ({spam_prob*100:.1f}%)'
        )

st.markdown("---")
st.caption("Built with ❤️ using TensorFlow + Streamlit + GRU")
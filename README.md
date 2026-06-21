# 📧 Deep Learning Email Spam Detection

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Neural%20Networks-red?style=for-the-badge&logo=keras)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An **End-to-End Email Spam Detection System** built using **Deep Learning** and **Natural Language Processing (NLP)**. This project compares **RNN**, **LSTM**, and **GRU** architectures for email classification and deploys the best-performing model through an interactive **Streamlit** web application.

---

# 🚀 Features

- ✅ Email Spam Classification using Deep Learning
- ✅ Compared RNN, LSTM and GRU models
- ✅ GRU selected as the best-performing model
- ✅ Complete NLP preprocessing pipeline
- ✅ Interactive Streamlit Web Application
- ✅ Real-time Spam/Ham Prediction
- ✅ Prediction Confidence Score
- ✅ Email Statistics Dashboard
- ✅ Download Prediction Report
- ✅ Clean and Responsive User Interface

---

# 🧠 Deep Learning Models

This project implements and compares three sequential neural network architectures:

- Recurrent Neural Network (RNN)
- Long Short-Term Memory (LSTM)
- Gated Recurrent Unit (GRU)

After experimentation, the **GRU model** achieved the best performance and was selected for deployment.

---

# 🛠 Tech Stack

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pandas
- NLTK
- Pickle
- Git & GitHub

---

# 📂 Project Structure

```
Deep-Learning-Email-Spam-Detection
│
├── app.py
├── spamclassification.ipynb
├── combined_data.csv
├── gru_model.keras
├── tokenizer.pkl
├── config.pkl
├── label_mapping.pkl
├── requirements.txt
├── README.md
└── screenshots
```

---

# 🔄 Workflow

```
Email Input
      │
      ▼
Text Cleaning
      │
      ▼
Tokenization
      │
      ▼
Stopword Removal
      │
      ▼
Sequence Padding
      │
      ▼
GRU Neural Network
      │
      ▼
Spam / Ham Prediction
```

---

# 🧹 NLP Preprocessing

The following preprocessing techniques were applied:

- Lowercase Conversion
- Punctuation Removal
- Tokenization
- Stopword Removal
- URL Cleaning
- Number Cleaning
- Sequence Padding
- Tokenization using Keras Tokenizer

---

# 📊 Model Comparison

| Model | Status |
|--------|--------|
| RNN | Implemented |
| LSTM | Implemented |
| **GRU** | ✅ Selected |

---

# 📷 Application Preview

### Home Page

<img width="1920" height="1080" alt="Screenshot (150)" src="https://github.com/user-attachments/assets/f69a1ff2-71b4-4345-a94b-d99261f46d3b" />


### Spam Prediction

<img width="1920" height="1080" alt="Screenshot (148)" src="https://github.com/user-attachments/assets/98314249-7d1f-43a6-92a7-e47daa5bb761" />


### Ham Prediction

<img width="1920" height="1080" alt="Screenshot (149)" src="https://github.com/user-attachments/assets/4f564c56-9a9a-49ef-a983-71d9739a6b49" />


---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/aryankamboj0001/Deep-Learning-Email-Spam-Detection.git
```

Move into the project directory

```bash
cd Deep-Learning-Email-Spam-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

- Bidirectional GRU
- Attention Mechanism
- Transformer (BERT)
- Explainable AI (LIME / SHAP)
- REST API using FastAPI
- Docker Deployment
- AWS/Azure Cloud Deployment
- Multi-language Spam Detection
- Mobile Application
- Email Attachment Analysis

---

# 👨‍💻 Author

**Aryan Kumar**

B.Tech Artificial Intelligence & Data Science

GitHub: https://github.com/aryankamboj0001

LinkedIn: *(Add your LinkedIn profile here)*

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

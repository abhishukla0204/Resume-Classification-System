# 📄 Resume Screening App

An intelligent resume classification application powered by Machine Learning and Natural Language Processing. Upload a resume and get instant job category predictions from 25 different categories.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)

## ✨ Features

- **Smart Classification**: Automatically categorizes resumes into 25 job categories
- **Multiple File Formats**: Supports PDF, DOCX, and TXT files
- **Modern UI**: Beautiful dark/light theme with smooth animations
- **Real-time Analysis**: Instant predictions with confidence display
- **Text Extraction**: View extracted text from uploaded resumes

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit with custom CSS |
| **ML Model** | Support Vector Classifier (SVC) |
| **Text Processing** | TF-IDF Vectorization |
| **NLP** | Text preprocessing with regex |
| **File Parsing** | PyPDF2, python-docx |

## 📁 Project Structure

```
Resume-Screening-App/
├── app.py                              # Main Streamlit application
├── clf.pkl                             # Trained SVC model (generated)
├── tfidf.pkl                           # TF-IDF vectorizer (generated)
├── encoder.pkl                         # Label encoder (generated)
├── Resume Screening with Python.ipynb  # Model training notebook
├── UpdatedResumeDataSet.csv            # Training dataset
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore file
└── README.md                           # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhishukla0204/Resume-Classification-System
   cd Resume-Classification-System
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model** (First time only)
   
   Open and run all cells in `Resume Screening with Python.ipynb` to generate:
   - `clf.pkl` - Trained classifier model
   - `tfidf.pkl` - TF-IDF vectorizer
   - `encoder.pkl` - Label encoder

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   
   Navigate to `http://localhost:8501`

## 📊 Supported Job Categories (25)

| | | | |
|---|---|---|---|
| Advocate | Arts | Automation Testing | Blockchain |
| Business Analyst | Civil Engineer | Data Science | Database |
| DevOps Engineer | DotNet Developer | Electrical Engineering | ETL Developer |
| Hadoop | Health and Fitness | HR | Java Developer |
| Mechanical Engineer | Network Security Engineer | Operations Manager | PMO |
| Python Developer | SAP Developer | Sales | Testing |
| Web Designing | | | |

## 🎨 UI Features

- **Theme Toggle**: Switch between dark and light modes
- **Responsive Design**: Works on desktop and mobile
- **Animated Elements**: Smooth transitions and hover effects
- **Color Palette**: Warm orange-red gradient theme

## 📝 How It Works

1. **Text Extraction**: Resume content is extracted from PDF/DOCX/TXT
2. **Preprocessing**: Text is cleaned (URLs, emails, special characters removed)
3. **Vectorization**: Cleaned text is converted to TF-IDF features
4. **Classification**: SVC model predicts the job category
5. **Display**: Results shown with category badge and extracted text

## 🔧 Configuration

The app uses the following model files (must be in the project root):

| File | Description | Size |
|------|-------------|------|
| `clf.pkl` | Trained SVC classifier | ~220 MB |
| `tfidf.pkl` | TF-IDF vectorizer | ~0.15 MB |
| `encoder.pkl` | Label encoder for categories | ~0.01 MB |

## 📦 Dependencies

```
streamlit>=1.28.0
scikit-learn>=1.3.0
python-docx>=0.8.11
PyPDF2>=3.0.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
joblib>=1.3.0
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👤 Author

**Abhinav Shukla**

- Email: [shukla.abhinav0204@gmail.com](mailto://shukla.abhinav0204@gmail.com)

---

⭐ Star this repository if you find it helpful!

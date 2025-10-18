# Diabetes Prediction System

A machine learning-powered web application that predicts the likelihood of diabetes based on medical diagnostic measurements. Built with Flask and scikit-learn.

## 📋 Overview

This project implements a diabetes prediction system using a trained machine learning model. Users can input their medical information through a web interface, and the system provides an instant prediction about their diabetes risk.

## ✨ Features

- **User-Friendly Interface**: Clean and intuitive web form for data input
- **Real-Time Predictions**: Instant diabetes risk assessment
- **Data Validation**: Client-side and server-side input validation
- **Responsive Design**: Works seamlessly across different devices
- **Pre-trained Model**: Uses a machine learning model trained on diabetes dataset

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Model Serialization**: Pickle

## 📊 Input Features

The prediction model requires the following 8 medical parameters:

1. **Pregnancies**: Number of times pregnant
2. **Glucose**: Plasma glucose concentration
3. **Blood Pressure**: Diastolic blood pressure (mm Hg)
4. **Skin Thickness**: Triceps skin fold thickness (mm)
5. **Insulin**: 2-Hour serum insulin (mu U/ml)
6. **BMI**: Body mass index (weight in kg/(height in m)²)
7. **Diabetes Pedigree Function**: Diabetes pedigree function score
8. **Age**: Age in years

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/diabetes-prediction.git
cd diabetes-prediction
```

### Step 2: Install Dependencies

```bash
pip install flask numpy scikit-learn
```

### Step 3: Ensure Model Files Are Present

Make sure the following files are in your project directory:
- `diabetes_model.pkl` (trained machine learning model)
- `scaler.pkl` (data scaler for preprocessing)

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

## 📁 Project Structure

```
diabetes-prediction/
│
├── app.py                  # Main Flask application
├── diabetes_model.pkl      # Trained ML model
├── scaler.pkl             # Data preprocessing scaler
│
├── templates/
│   ├── index.html         # Home page with input form
│   └── result.html        # Results display page
│
├── static/
│   ├── styles.css         # Styling
│   └── script.js          # Client-side validation
│
├── link.txt               # Colab notebook link
└── README.md              # Project documentation
```

## 💻 Usage

1. Navigate to `http://127.0.0.1:5000/` in your web browser
2. Fill in all the required medical parameters
3. Click the "Predict" button
4. View your prediction result (Diabetic 😢 or Not Diabetic 😊)
5. Click "Go Back" to make another prediction

## 🔬 Model Training

The machine learning model was trained using the Pima Indians Diabetes Database. For details on the training process, refer to the Colab notebook:

[View Training Notebook](https://colab.research.google.com/drive/1TC32ffR6kGEW5ggdvmjXiPSD6hjXPK03?usp=sharing)

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Aashish Joshi - [AAs6395](https://github.com/AAs6395)

## 🙏 Acknowledgments

- Pima Indians Diabetes Database from the National Institute of Diabetes and Digestive and Kidney Diseases
- Flask documentation and community
- scikit-learn developers

---

**Note**: Remember to replace placeholder links and author information with your actual details.

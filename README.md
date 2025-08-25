# 🌸 Iris Flower Classification

This project classifies Iris flowers into three species (**Setosa**, **Versicolor**, **Virginica**) using the famous [Iris dataset from Kaggle](https://www.kaggle.com/datasets/uciml/iris).  
It uses machine learning to predict the species based on flower measurements like **sepal length, sepal width, petal length, and petal width**.

## 🔗 Quick Links
- 🚀 **Live App**: [Iris Flower Classifier](https://iris-flower-classification-fardeen.streamlit.app/)  
- 📓 **Training Notebook**: [Iris Flower Training Notebook](https://github.com/Fedo-911/iris-flower-classification/blob/main/Notebooks/Iris_Flower_Classification.ipynb)  
- 📊 **Dataset (Kaggle)**: [Iris Dataset](https://www.kaggle.com/datasets/uciml/iris) 



## 🚀 Project Workflow
1. **Data Preprocessing**
   - Loaded dataset (`Iris.csv`) from Kaggle
   - Dropped unnecessary `Id` column
   - Encoded flower species labels
   - Scaled features using `StandardScaler`

2. **Model Training**
   - Used **Logistic Regression** classifier
   - Achieved accuracy of **95–98%** on test data

3. **Evaluation**
   - Accuracy score
   - Classification report
   - Confusion matrix visualization

4. **Deployment**
   - Built an interactive **Streamlit app**
   - Users can input flower measurements to get predictions
   - Added input validation (ensures values are within realistic ranges)



## 📂 Project Structure

iris-flower-classification/

│── app.py # Streamlit web app

│── iris_model.pkl # Trained Logistic Regression model

│── scaler.pkl # StandardScaler for feature scaling

│── label_encoder.pkl # LabelEncoder for mapping predictions

│── Iris.csv # Dataset from Kaggle

│── requirements.txt # Dependencies

│── README.md # Project documentation

│

└── Notebooks/

└── Iris_Flower_Classification.ipynb   # Model training notebook




## 🌸 Streamlit App Preview
The app allows users to enter **flower measurements** and predicts the species.  
It validates input values to ensure they fall within realistic ranges.

### Example Input:
- Sepal Length = `6.0`  
- Sepal Width = `2.7`  
- Petal Length = `4.5`  
- Petal Width = `1.5`  

👉 **Predicted Species: Iris-versicolor**



## ⚙️ Installation & Usage

### 1. Clone the repository

git clone https://github.com/Fedo-911/Iris-Flower-Classification.git

cd iris-flower-classification

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the Streamlit app
streamlit run app.py

# 📊 Dataset

The dataset comes from Kaggle’s Iris dataset:

• 150 samples

• 3 species: Setosa, Versicolor, Virginica

• 4 features: Sepal Length, Sepal Width, Petal Length, Petal Width

# 🔮 Future Improvements

• Try different ML algorithms (SVM, Random Forest, XGBoost)

• Hyperparameter tuning for better accuracy

• Deploy on Streamlit Cloud with live demo link

# 👨‍💻 Author

Developed by Fardeen Tariq 🌱

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/fardeen-tariq)
 

# 📊 AI Regression Activity

This project demonstrates a complete machine learning workflow using **Linear Regression** to predict apartment rental prices based on real-world features. The goal is to show how to go from data analysis to a deployable REST API with a connected frontend.

## 📁 Project Structure

- **`rent.csv`**: Dataset used for training and evaluation.
- **`analisys-structure.py`**: Uses `pandas` to load and visualize dataset structure.
- **`analisys-data.py`**: Performs correlation analysis (Pearson) between features and the target variable `rent amount`.
- **`training.py`**: Trains a Linear Regression model using `scikit-learn` and saves it with `joblib`.
- **`try-model.py`**: Loads the trained model and runs test predictions.
- **`api.py`**: Serves the trained model through a Flask REST API, exposing an endpoint to make predictions.
- **`index.html`**: A simple frontend form that allows users to input values and get predictions via the API.

## 🌐 How It Works

1. **Data Analysis**: Understand and prepare the dataset.
2. **Correlation**: Identify the most influential features for rent prediction.
3. **Training**: Build and evaluate a regression model using selected features.
4. **Serving**: Expose the model via a Flask API.
5. **Frontend**: Use JavaScript to collect input and fetch predictions from the API.

## ⚖️ Tech Stack

- Python 3
- pandas
- scikit-learn
- Flask
- flask-cors
- joblib
- HTML + JavaScript (Vanilla)

## ✨ Example Usage

### Request (POST to `/preview_rent`)
```json
{
  "fire insurance": 23,
  "bathroom": 1,
  "parking spaces": 1
}
```

### Response
```json
{
  "previsao_rent_amount": 1580.75
}
```

## 🔧 Running Locally

1. Clone the repo
```bash
git clone https://github.com/augustosnk12/ia-regression-acitivity.git
cd ai-regression-activity
```

2. Install Python dependencies

3. Run the training script
```bash
python training.py
```

4. Start the Flask API
```bash
python api.py
```

5. Open `index.html` in your browser (e.g., with Live Server)

## 📅 License
This project is open-source and available under the [MIT License](LICENSE).

---

Made with ❤️ for learning purposes.


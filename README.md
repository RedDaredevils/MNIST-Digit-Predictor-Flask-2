# 🧠 MNIST-Digit-Predictor-Flask-2 🔢

![MNIST Classifier](https://raw.githubusercontent.com/your-username/mnist-digit-classifier/main/static/banner.png)  

A **deep learning-powered web app** that recognizes handwritten digits (0-9) using a model trained on the **MNIST dataset**. Built with **Flask, TensorFlow, and HTML/CSS**, this app provides a user-friendly interface for digit classification. 🚀

## ✨ Features
- 🎨 **Interactive UI** with a **3D animated background**
- 📸 **Upload handwritten digit images** (PNG, JPG, JPEG)
- 🔮 **AI-powered predictions** using a trained MNIST model
- ⚡ **Fast and accurate results**
- 🌍 **Live deployment on Render**

## 📌 How It Works
1️⃣ Upload an image containing a single digit (0-9).  
2️⃣ Ensure the image has **black background** and **white digit**.  
3️⃣ Click **Predict 🔮**, and the AI model will classify the number.  

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Particle.js (for animation)
- **Backend:** Flask (Python)
- **Machine Learning:** TensorFlow (Deep Learning Model)
- **Deployment:** Render

## ⚠️ Image Requirements
✔ The image should contain **only one handwritten digit**.  
✔ Format: **PNG, JPG, or JPEG**.  
✔ Size **≤ 1MB** for faster processing.  
✔ **Background must be black**, and the **digit must be white**.  

## 🚀 Deployment on Render
This project is **live on Render!** You can check it out here:  
🔗 [Live Demo](https://mnist-classifier.onrender.com)  

Want to deploy it yourself? Follow these steps:
1️⃣ **Clone this repository:**  
   ```bash
   git clone https://github.com/your-username/mnist-digit-classifier.git
   ```
2️⃣ **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```
3️⃣ **Run the Flask app:**  
   ```bash
   python app.py
   ```
4️⃣ **Visit:** `http://127.0.0.1:5000/`

## 📂 Project Structure
```
mnist-digit-classifier/
│── static/
│   ├── styles.css
│── templates/
│   ├── index.html
│── app.py  (Flask backend)
│── mnist_model.h5 (Trained ML model)
│── requirements.txt (Dependencies)
│── Procfile (For deployment)
│── runtime.txt (Python version)
│── README.md (This file)
```

## 🤝 Contributing
Got ideas for improvements? Contributions are welcome! Feel free to **fork this repo**, make your changes, and submit a **pull request**. 😊

## ❤️ Credits
Made with passion by **Adeel** 🚀 | Bringing AI to Life!  

---
🌟 **Star this repo** if you like it! ⭐

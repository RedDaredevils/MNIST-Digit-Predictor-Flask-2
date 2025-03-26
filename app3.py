from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

# Home route - renders the HTML file
@app.route("/")
def home():
    return render_template("index.html")

# Route to predict digit from an image
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # 1️⃣ Get the uploaded image
        file = request.files["file"]
        img = Image.open(io.BytesIO(file.read())).convert("L")  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to match MNIST shape

        # 2️⃣ Convert image to array
        img_array = np.array(img) / 255.0  # Normalize pixel values (0-1)
        img_array = img_array.reshape(1, 28, 28, 1)  # Reshape for CNN

        # 3️⃣ Load model inside the route (Lazy Loading)
        model = tf.keras.models.load_model("mnist_model.h5")

        # 4️⃣ Make prediction
        predictions = model.predict(img_array)
        predicted_class = int(np.argmax(predictions))  # Get highest probability class
        confidence = round(100 * np.max(predictions), 2)  # Confidence score

        # 5️⃣ Return prediction and confidence
        return render_template("index.html", prediction=predicted_class, confidence=confidence)

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

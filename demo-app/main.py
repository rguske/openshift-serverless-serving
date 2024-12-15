from flask import Flask, render_template_string, send_from_directory
import os

port = int(os.environ.get("PORT", default=8080))
app = Flask(__name__)

# HTML template with a centered image and text
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>{{ message }}</h1>
</body>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web App</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #000000;
        }
        img {
            max-width: 70%;
            height: auto;
            margin-bottom: 20px;
        }
        h1 {
            color: #f502d9;
        }
    </style>
</head>
<body>
    <img src="{{ image_url }}" alt="Centered Image">
    <h1>{{ message }}</h1>
</body>
</html>
"""

@app.route("/")
def home():
    # Get the message and image path from environment variables or use defaults
    message = os.getenv("MESSAGE", "Hello, World!")
    image_path = os.getenv("IMAGE_PATH", "static/default.jpg")
    image_url = f"/images/{os.path.basename(image_path)}"
    print(f"Message: {message}, Image Path: {image_path}")  # Print to stdout
    return render_template_string(HTML_TEMPLATE, message=message, image_url=image_url)

@app.route("/images/<filename>")
def serve_image(filename):
    # Serve the image from the container
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
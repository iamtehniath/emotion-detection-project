from flask import Flask
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    response = emotion_detector("I am happy")
    return str(response)

@app.route("/")
def render_index_page():
    return "Emotion Detection App Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
"""
Emotion Detector Server

This module contains the server implementation for the Emotion Detector application.
It provides routes for analyzing text and rendering the index page.

Author: Chandra Mohan
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Analyze the emotion in a given text and return the result.

    Returns:
        str: A response message indicating the detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                        {response['anger']}, 'disgust': {response['disgust']}, \
                        'fear': {response['fear']}, 'joy': {response['joy']}, \
                        'sadness': {response['sadness']}. The dominant emotion is \
                        {response['dominant_emotion']}."

    return response_text

@app.route("/")
def render_index_page():
    """
    Render the index.html template.

    Returns:
        str: The rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

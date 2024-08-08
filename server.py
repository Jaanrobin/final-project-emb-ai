''' Executing this function initiates the application of Emotion Detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_analyzer():
    ''' This is a Function to alanyse!
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    f"'joy': {response['joy']}, 'sadness': {response['sadness']}. "
    f"The dominant emotion is <b>{response['dominant_emotion']}</b>.")

@app.route("/")
def render_index_page():
    ''' This Funtion rederds webapp from template File!
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

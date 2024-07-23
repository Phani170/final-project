from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_Detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    label = response['dominant_emotion']
    #score = response[label]

    if label is None:
        ans = "Invalid Input! Please try again."
    else:
        ans = "For the given statement, the system response is 'anger': " + str(response['anger']) + ", disgust: " + str(response['disgust']) + ", fear: " + str(response['fear']) + ", joy: " + str(response['joy']) + 'and sadness:' + str(response['sadness']) + ".The dominant emotion is " + label + "."
    return ans

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001)
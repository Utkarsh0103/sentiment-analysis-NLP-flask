from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

# This code receives the text from the HTML interface and 
# runs sentiment analysis over it using sentiment_analysis()
# function. The output returned shows the label and its confidence 
# score for the provided text.
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

# This function initiates the rendering of the main application
# page over the Flask channel
@app.route("/")
def render_index_page():
    return render_template('index.html')

# This functions executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

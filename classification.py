import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

def classification(post):
    vectorizer = joblib.load('files/tfidfVectorizer.joblib')
    classificator = joblib.load('files/fitNaiveBayes.joblib')

    toTest = vectorizer.transform([post]).todense()
    return classificator.predict(toTest)
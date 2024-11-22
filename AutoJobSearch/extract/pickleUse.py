import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def find_domain():
    with open('C:/Users/keyur/Desktop/VIT/EDI/edi5/AutoJobSearch/extract/rf_classifier_job_recommendation.pkl', 'rb') as file:
        model = pickle.load(file)

    with open('C:/Users/keyur/Desktop/VIT/EDI/edi5/AutoJobSearch/extract/tfidf_vectorizer_job_recommendation.pkl', 'rb') as file:
        vectorizer = pickle.load(file)  


    def cleanResume(txt):
        cleanText = re.sub(r'http\S+\s', ' ', txt)
        cleanText = re.sub(r'RT|cc', ' ', cleanText)
        cleanText = re.sub(r'#\S+\s', ' ', cleanText)
        cleanText = re.sub(r'@\S+', ' ', cleanText)
        cleanText = re.sub(r'[%s]' % re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
        cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
        cleanText = re.sub(r'\s+', ' ', cleanText)
        return cleanText


    def job_recommendation(resume_text):
        clean_text = cleanResume(resume_text)
        resume_tfidf = vectorizer.transform([clean_text])
        prediction = model.predict(resume_tfidf)  
        return prediction

    with open('resume_data.pkl','rb') as d :
        resume_data = str(pickle.load(d))

    result = job_recommendation(resume_data)
    print(result)

    with open('C:/Users/keyur/Desktop/VIT/EDI/edi5/AutoJobSearch/extract/models/rf_classifier_categorization.pkl','rb') as file1:
        model1 = pickle.load(file1)

    with open('C:/Users/keyur/Desktop/VIT/EDI/edi5/AutoJobSearch/extract/models/tfidf_vectorizer_categorization.pkl','rb') as file1:
        vectorizer1 = pickle.load(file1)

    def predict_category(resume_text):
        clean_text = cleanResume(resume_text)
        resume_tfidf = vectorizer1.transform([clean_text])
        prediction = model1.predict(resume_tfidf)
        return prediction


    print (resume_data)
    res = predict_category(resume_data)
    print(res)
    response = [res, result]
    return(response)
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from os import getcwd
from NetHyTech_Pyttsx3_Speak import speak
import Wiki_Reply
from Automation._intregation_automation import Automation
from FUNCTION.function_intregation import Function_cmd

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question': q, 'answer': a} for q, a in qna_pairs]
    return dataset

# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

# Train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    best_similarity = similarities[0, best_match_index]
    if best_similarity < 0.2:  # Adjust the threshold as needed
        return "I don't know"
    return dataset[best_match_index]['answer']

def mind(text):
    dataset_path = rf'{getcwd()}\data.txt'
    dataset = load_dataset(dataset_path)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, X, dataset)
    return answer# Returning the answer for potential further processing

def Query_brain(text):
    try:
        if "jarvis" in text:
            answer = mind(text)
            if "I don't know" in answer:
                answer = Wiki_Reply.get_wikipedia_summary(text)
                speak(answer, 3)
            else:
                speak(answer, 3)
                
        else:
            Automation(text)
            Function_cmd(text)
            
              # Speaking the original text if it's not related to "jarvis"
    except Exception as e:
        print("An error occurred:", e)


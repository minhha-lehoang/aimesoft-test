import spacy
import re

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Define stop words
stop_words = nlp.Defaults.stop_words

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Replace newlines with spaces
    text = text.replace('\n', ' ')

    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)

    # Remove digits
    text = re.sub(r'\d+', ' ', text)

    # Process text with spaCy
    doc = nlp(text)

    # Remove stopwords and lemmatize verbs only
    text = [token.lemma_ if token.pos_ == 'VERB' else token.text for token in doc if token.text not in stop_words]

    # Join tokens back into a single string
    text = ' '.join(text)

    # Remove double spaces
    text = re.sub(r'\s+', ' ', text)

    return text

if __name__ == '__main__':
    text = "This is a sample text for preprocessing. It includes punctuation, digits, and stopwords."
    print(preprocess_text(text))
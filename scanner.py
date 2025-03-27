from PyPDF2 import PdfReader

# Read the PDF file
reader = PdfReader('dummy.pdf')
text = ""
for page in reader.pages:
    text += page.extract_text()

print(text)  # Displays extracted resume content

import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Extract named entities (skills, job titles, etc.)
doc = nlp(text)
for entity in doc.ents:
    print(entity.text, entity.label_)
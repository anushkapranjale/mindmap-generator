import spacy

nlp = spacy.load("en_core_web_sm")

# 👇 Optional: apni list of boring/common words jo ignore karne hain
BLOCKLIST = { "type", "thing", "way", "data", "information"}

def extract_keywords(text):
    doc = nlp(text)
    keywords = [
        token.lemma_ for token in doc
        if token.pos_ in ['NOUN', 'PROPN']
        and not token.is_stop
        and token.lemma_.lower() not in BLOCKLIST
    ]
    return list(set(keywords))[:10]  # 👈 unique and top 10

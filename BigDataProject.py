#Umer Tahir L1F21BSCS0378 D-8
#Ali Zaman L1F21BSCS1119 D-8
#Lajwer Liaquat L1F21BSCS0821 D-8

import nltk
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

df = pd.read_csv('BigDataProject.csv')
df['Email'] = df['Email'].astype(str)
df['Text'] = df['Text'].astype(str)
df

#q1
def remove_email(text):
    email_regex = ('\w+@\w+\.\w+\.pk')
    removed_email= re.sub(email_regex, '', text)
    return removed_email
df['Email'] = df['Email'].apply(remove_email)
df

#q2
def remove_url(text):
    url_regex = ('https?://\S+')
    removed_url= re.sub(url_regex, '', text)
    return removed_url
df['Text'] = df['Text'].apply(remove_url)
df

#q3
df['Phone'] = df['Phone'].astype(str)
def check_phone_number(text):
    phone_numbers = re.findall('\d{4}-\d{7}', text)
    if phone_numbers:
        return phone_numbers[0]
    else:
        return ""
df['Phone'] = df['Phone'].apply(check_phone_number)
df

#q4
def convert_to_lowercase(text):
    words = re.findall(r'\b[A-Z][a-zA-Z]*\b', text)
    for word in words:
        text = text.replace(word, word.lower())
    return text
df['Text'] = df['Text'].apply(convert_to_lowercase)
df

#q5
def replace_words(text):
    word='ucp'
    replace = 'University of Central Punjab'
    replaced_text = re.sub(word,replace, text)
    return replaced_text
df['Text'] = df['Text'].apply(replace_words)
df

#q6
def remove_numbers(text):
    text_without_numbers = re.sub('\d+', '', text)
    return text_without_numbers

df['Text'] = df['Text'].apply(remove_numbers)

df

#q7
def remove_html_tags(text):
    cleaned_text = re.sub('<[A-Za-z0-9]+>', '', text)
    return cleaned_text
df['Text'] = df['Text'].apply(remove_html_tags)
df

#q8
def extract_words_ending_with_ing(text):
    words_ending_with_ing = re.findall("[A-Za-z0-9]+ing", text)
    return words_ending_with_ing

df['Text'] = df['Text'].apply(extract_words_ending_with_ing)
df

#q9
df['Text'] = df['Text'].astype(str)
def whitespace_characters(text):
    pattern = '\s+'
    replace = ''
    white_space = re.sub(pattern, replace, text) 
    return white_space

df['Text'] = df['Text'].apply(whitespace_characters)

df

#q10
def lemmatize_with_pos_tagging(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    def get_wordnet_pos(pos_tag):
        if pos_tag.startswith('J'):
            return wordnet.ADJ
        elif pos_tag.startswith('V'):
            return wordnet.VERB
        elif pos_tag.startswith('N'):
            return wordnet.NOUN
        elif pos_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN 

    lemmatized_tokens = []
    for token, pos_tag in tagged_tokens:
        wordnet_pos = get_wordnet_pos(pos_tag)
        lemmatized_token = lemmatizer.lemmatize(token, wordnet_pos)
        lemmatized_tokens.append(lemmatized_token)

    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text
df['Text'] = df['Text'].apply(lemmatize_with_pos_tagging)
df
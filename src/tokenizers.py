'''
This module contains the following functions for tokenizing text from Stack
Exchange posts.

tokenize_title - Tokenizes question titles.
tokenize_body - Tokenizes the body of posts.
'''
import re
from bs4 import BeautifulSoup as bs
import se_post_processing as sepp

def tokenize_title(title, lemmatizer, stops):
    '''
    Convert the title of Stack Exchange question to a list of tokens.

    Arguments
    ---------
    post - str
        A Stack Exchange question title as recorded in the "Title" column of
        the Stack Exchange data dumps.
    lemmatizer - WordNetLemmatizer
        A lemmatizer for converting words to lemmas.
    stops - set(str)
        A set of stop words to exclude as tokens.

    Returns
    -------
    clean_tokens - list[str]
        A list of tokens extracted from the post.
    '''
    # Get words from title and convert to lowercase.
    words = [word.lower() for word in title.split()]

    # Loop through words and tokenize.
    tokens = []
    for word in words:
        # Ignore words which contain characters whcih are not English letters.
        if not re.match('[a-z]+$', word):
            continue

        # Ignore stop words.
        if word in stops:
            continue

        # Convert to lemma.
        lemma = lemmatizer.lemmatize(word)

        # Ignore null lemmas.
        if len(lemma) == 0:
            continue

        # Add prefix to indicate that the word came from the title.
        token = 'title_' + lemma
        tokens.append(token)

    return tokens
    
def tokenize_post(post, lemmatizer, stops):
    '''
    Convert a Stack Exchange post to a list of tokens.

    Arguments
    ---------
    post - str
        A Stack Exchange post as recorded in the "Body" column of the Stack
        Exchange data dumps.
    lemmatizer - WordNetLemmatizer
        A lemmatizer for converting words to lemmas.
    stops - set(str)
        A set of stop words to exclude as tokens.

    Returns
    -------
    clean_tokens - list[str]
        A list of tokens extracted from the post.
    '''
    # Get text from post..
    soup = bs(post, features='lxml')
    text = soup.get_text()

    # Remove displayed math equations from the text.
    math_eqs = sepp.find_math(post)
    for eq in math_eqs:
        text = text.replace(eq, ' ')

    # Get words from title and convert to lowercase.
    words = [token.lower() for token in text.split()]

    # Loop through words and tokenize.
    tokens = []
    for word in words:
        # Ignore words which contain characters whcih are not English letters.
        if not re.match('[a-z]+$', word):
            continue

        # Ignore stop words.
        if word in stops:
            continue

        # Convert to lemma.
        lemma = lemmatizer.lemmatize(word)

        # Ignore null lemmas.
        if len(lemma) == 0:
            continue

        # Add prefix to indicate that the word came from the title.
        token = 'title_' + lemma
        tokens.append(token)

    return tokens
import system.command
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import nltk
from pymorphy2 import MorphAnalyzer
from pprint import pprint
import re
from collections import namedtuple
from string import punctuation
from collections import Counter
sw = nltk.corpus.stopwords.words('russian')
morph = MorphAnalyzer()


class StartCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = 'bochok potik :/'

    def process(self, text):
        return wikipedia_search(text)


def wikipedia_link_fetcher(user_input):
    user_input = user_input.split()
    user_input.append('wikipedia')
    query = '+'.join(user_input)
    google_address = 'https://www.google.ru/search?q=' + query

    ua = UserAgent(verify_ssl=False)
    headers = {'User-Agent': ua.random}
    response = requests.get(google_address, headers=headers)
    html = response.text
    with open('hah.html', 'w', encoding='utf-8') as f:
        f.write(html)

    if re.search(r'(https://..\.wikipedia\.org/.+?)"', html):
        print(re.search(r'(https://..\.wikipedia\.org/wiki.+?)"', html).group(1))
        return re.search(r'(https://..\.wikipedia\.org/wiki.+?)"', html).group(1)
    else:
        return 'hack'


def morph_parser(text):
    text = text.replace('ё', 'е')
    text = text.replace('Ё', 'Е')
    lemmas = [x.strip(punctuation).lower() for x in nltk.word_tokenize(text) if x.isalpha()]
    lemmas = [x for x in lemmas if x not in sw]
    for i, lemma in enumerate(lemmas):
        lemmas[i] = morph.parse(lemma)[0].normal_form

    return lemmas


def user_input_parser(user_input):
    parsed_user_input = set(morph_parser(user_input))

    return parsed_user_input


def wikipedia_parser(link):
    ua = UserAgent(verify_ssl=False)

    headers = {'User-Agent': ua.random}
    response = requests.get(link, headers=headers)
    html = re.search(r'<p>(.|\s)+', response.text).group()

    soup = BeautifulSoup(html, 'html.parser')
    article = soup.get_text()
    article = re.sub(r'\[.+?\]', '', article)
    article = nltk.sent_tokenize(article)

    all_lemmas = []
    parsed_article = []
    sentence_properties = namedtuple('sentence_properties', 'full lemmatized')

    for sentence in article:
        parsed_sentence = morph_parser(sentence)

        all_lemmas.extend(parsed_sentence)

        parsed_sentence = set(parsed_sentence)
        parsed_article.append(sentence_properties(sentence, parsed_sentence))

    freq_dict = dict(Counter(all_lemmas))
    for word in freq_dict:
        freq_dict[word] = 1 / freq_dict[word]

    return parsed_article, freq_dict


def sentence_chooser(parsed_user_input, article_properties):
    parsed_article = article_properties[0]
    freq_dict = article_properties[1]

    max = 0
    max_index = 0

    for i, sentence in enumerate(parsed_article):
        count = 0
        for lemma in sentence.lemmatized:
            if lemma in parsed_user_input:
                count += freq_dict[lemma]
        if count > max:
            max = count
            max_index = i
        if max == len(parsed_user_input):
            return parsed_article[max_index].full

    return parsed_article[max_index].full


if __name__ == '__main__':
    import time
    start_time = time.time()
    user_input = input()
    article = wikipedia_parser(wikipedia_link_fetcher(user_input))
    user_input = user_input_parser(user_input)
    print(sentence_chooser(user_input, article))
    print("--- %s seconds ---" % (time.time() - start_time))
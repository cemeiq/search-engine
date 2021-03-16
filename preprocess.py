import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from pathlib import Path, PurePath
import requests
from requests.exceptions import HTTPError, ConnectionError
from rank_bm25 import BM25Okapi
import nltk
from nltk.corpus import stopwords
nltk.download("punkt")
nltk.download("stopwords")
import re
import os
import json
import glob
import sys
from tqdm import tqdm
from rank_bm25 import BM25Okapi


class preprocess_class:

    def __init__(self, text):
        self.stop_words = list(set(stopwords.words("english")))
        self.text = text

    def strip_characters(self, text):
        """
        This function will strip off characters from the text string
        :return: string
        """
        stripped_text = re.sub('\(|\)|:|,|;|\.|’|”|“|\?|%|>|<', '', text)
        stripped_text = re.sub('/', ' ', stripped_text)
        stripped_text = stripped_text.replace("'",'')
        return stripped_text

    def clean(self):
        """
        This function will convert the string to lowercase and strip characters 
        :return: processed string
        """
        cleaned_text = self.text.lower()
        cleaned_text = self.strip_characters(cleaned_text)
        return cleaned_text

    def tokenize(self, text_string):
        """
        This function will tokenize the string
        :return: list of tokens
        """
        tokens_list = nltk.word_tokenize(text_string)
        processed_tokens_list = []
        for token in tokens_list:
            print(token)
            if (len(token) > 1) and (token not in self.stop_words)  and not (token.isnumeric() and len(token) is not 4) \
            and (not token.isnumeric() or token.isalpha()) :
                
                processed_tokens_list.append(token)

        return list(set(processed_tokens_list))        

    def preprocess(self):
        """
        This function will get json files from all the subdirectories in a partciular directory
        :return: list of json files
        """
        cleaned_text = self.clean()
        tokens = self.tokenize(cleaned_text)
        return tokens        


obj = preprocess_class("My name is iqra 1234 dfdmfn[]")
print(obj.preprocess())
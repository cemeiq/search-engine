import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from pathlib import Path, PurePath
import requests
from requests.exceptions import HTTPError, ConnectionError
from rank_bm25 import BM25Okapi
import nltk
from nltk.corpus import stopwords
nltk.download("punkt")
import re
import os
import json
import glob
import sys
from tqdm import tqdm
from rank_bm25 import BM25Okapi
from paper import Paper

class SearchResults:

    def __init__(self, dataframe, columns = None):
        """
        This function will initilize the input data dataframe and columns
        :param dataframe: a dataframe for results, colums: columns of dataframe  
        :return: none
        """
        self.results = dataframe
        if columns:
            self.results = self.results[columns]
        

    def __len__(self):
        """
        This function will the calculate the length the dataframe
        :return: int
        """
        return len(self.results)

    def __getitem__(self, item):
        """
        This function return the paper instance for a particular paper
        :return: object
        """

         return Paper(self.results.loc[item])


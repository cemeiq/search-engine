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

sys.path.insert(0, "../")

DATA_PATH = '/home/iqra/Documents/python-projects/search-engine/dataset/'

class Json_Data:
    
    def __init__(self, dirname, num_docs):
            self.dirname = dirname
            self.num_docs = num_docs

    def get_jsons(self):
        """
        This function will get json files from all the subdirectories in a partciular directory
        :return: list of json files
        """
        listOfFiles = list()
        for (dirpath, dirnames , filenames) in os.walk(self.dirname):
                for file in filenames[0:self.num_docs+1]:
                    if file.endswith('.json') and len(file) == 45:
                        listOfFiles.append(os.path.join(dirpath,file)) 

        print(f'Number of files found {len(listOfFiles)}')
        # print(listOfFiles[0])
        json_filelst = []

        for file in tqdm(listOfFiles[0: 50]):
            with open(file) as json_file:
                json_filelst.append(json.load(json_file)) 

        return json_filelst


    def extract_json_data(self, json_list):
        """
        This function will extract the id, title, abstract and text of each document and create a dictionary
        :param json_list: a list containing json files for documents
        :return: A json dictionary containing id, title, abstract and text of each document 
        """    
        if (len(json_list['abstract']) > 0):
            json_dict = {
                'id': json_list['paper_id'],
                'title': json_list['metadata']['title'],
                'abstract': json_list['abstract'],
                'text': "".join([i['text'] for i in json_list['body_text']])

            }
        else:
            json_dict = {
                'id': json_list['paper_id'],
                'title': json_list['metadata']['title'],
                'text': "".join([i['text'] for i in json_list['body_text']])

            }

        return json_dict

    def get_dataset(self):
        """
        This function will combine get_jsons and extract_json_data to create a pandas dataframe for the documents dataset 
        :return: documents dataframe
        """    
        
        json_lst = self.get_jsons()
        datalst = []
        for file in tqdm(json_lst):
            data_item = self.extract_json_data(file)
            datalst.append(data_item)
        dataset_df = pd.DataFrame(datalst)
        return dataset_df    

# get_dataset(DATA_PATH)
# json_docs_obj = Json_Data(DATA_PATH, 10)
# dataset = json_docs_obj.get_dataset()
# print(dataset.head(1))

       
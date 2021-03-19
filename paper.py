class Paper:

    def __init__(self, item):
        """
        This function will initilize the paper properties like metadata
        :param dataframe: a dataframe item  
        :return: none
        """
        if isinstance(item, pd.DataFrame):
            self.item = item.T.iloc[:, 0] 
        
        self.metadata = self.item
        self.sha = item.sha
        self.pmcid = item.pmcid
        self.cord_uid = item.cord_uid
        self.pdf_json_files = item.pdf_json_files
        self.data_path = item.data_path

        

    def get_jsonpaper(self):
        """
        This function will return the pdf json of a document   
        :return: json file
        """
        if isinstance(self.metadata.pdf_json_files, string):
            return self.get_pdf_json()

    def get_pdf_json_path(self):
        """
        This function will return the path of the pdf json file  
        :return: string
        """
        if self.metadata.pdf_json_files:
            return self.data_path / self.pdf_json_files.partition(';')[0]
    

    def get_pdf_json(self):
        """
        This function will get the pdf json
        :return: json file
        """
        path = self.get_pdf_json_path()
        if path and path.exists():
            return load_json_paper(path)

    @property
    def url(self):
        """
        This function will return the url for the document source  
        :return: string
        """

        if not isinstance(self.metadata.url, str):
                return none
        for url in self.metadata.url.split(';'):
            if 'api.elsevier.com' in url:
                return url.strip()            

    @property
    def title(self):
        """
        This function will return the title string for each document  
        :return: string
        """
        return self.metadata.title  

    @property
    def abstract(self):
        """
        This function will return the abstract for each document  
        :return: string
        """
        return self.metadata.abstract

    @property
    def authors(self):
        """
        This function will initilize the input data dataframe and columns
        :param dataframe: a dataframe for results, colums: columns of dataframe  
        :return: none
        """

        pass        
            

import pandas as pd

class csvImport():
    def __init__(self):
        self.databasePath = "../data/netflix_titles.csv"
        
    def import_database(self):
        data = pd.read_csv(self.databasePath)
        
        return data
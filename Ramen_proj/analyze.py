import pandas as pd
import numpy as np

class RamenFinds:
    
    def __init__(self, df, column=None):
        if (isinstance(df, str)):
            df = pd.read_csv(df)
            
        self.df = df
        
        if (column != None):
            self.col = df[column]
            self.star = self.average_star(None)
        
    def average_star(self, variable=None):
        if (variable == None):
            cate_star = {}
            n = len(self.df)
            count = self.col.value_counts()
            m = len(count.index.tolist())
            for i in range(n):
                if (self.col.iloc[i] in cate_star):
                    cate_star[self.col.iloc[i]] += self.df["Stars"].iloc[i] / count[self.col.iloc[i]]
                else:
                    cate_star[self.col.iloc[i]] = self.df["Stars"].iloc[i] / count[self.col.iloc[i]]
                
            return cate_star
        
        n = len(self.df)
        star = 0
        count = 0
        for i in range(n):
            if (self.col[i] == variable):
                star += self.df["Stars"].iloc[i]
                count += 1
            
        return star / count
            
            
                
            
        
from math import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from datetime import datetime

class Preprocessing:
    def __init__(self):
        self.crimesDf= pd.read_csv('Crimes_-_2018.csv')
        self.missing_values = list(self.crimesDf.isna().sum())
        self.cols = list(self.crimesDf.columns)
        col_final = []

        for i in range(len(self.cols)):
            if (self.missing_values[i] == 0):
                self.cols[i]="Others"
        self.d = dict(zip(self.cols, self.missing_values)) 
        self.missing_vals = pd.DataFrame(self.d, index=["Missing Values"]) 
    
    def get_missing_values_plot(self):
        #cambiar tamaño de la letra de los ejes
        plt.rcParams['font.size'] = 10
        self.x = list(self.d.keys())
        self.y = list(self.d.values())
        plt.figure(figsize=(12, 4))
        sns.barplot(x=self.x, y=self.y, palette="Reds")
        # plt.xticks(rotation=90)
        plt.title("Valores faltantes en el conjunto de datos", fontdict = {'fontsize': 10})
        plt.ylabel("Recuento de valores perdidos", fontdict={'fontsize': 10})
        # plt.show()
        return plt

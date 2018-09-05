#!/usr/bin/env python3

'''
Entry example which takes any entered text and displays it when the user
presses the button.
'''

import tkinter
import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile
from scipy.interpolate import *
from numpy import *
from matplotlib.pyplot import *
from os import listdir
from os.path import isfile, join
import shutil
import preprocessing
import models
import feature_engineering

class Entry(tkinter.Tk):
    location="hello"
    order="1"
    regression_type="0"
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Crystall-ball")
        self.geometry("500x500")
        
        
        label = tkinter.Label(text="")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=300)
        label.pack(fill=tkinter.BOTH, expand= 1)

        label = tkinter.Label(text="please select dataset and ask your question")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=300)
        label.pack(fill=tkinter.BOTH, expand= 0)

        
        #for the datasets list
        onlyfiles = [f for f in listdir("./") if isfile(join(f))]
        print(onlyfiles)
        optionList = []
        if (len(onlyfiles)== 0):
            optionList = ["please add datasets"]
        else:
            optionList=onlyfiles
            
        variable = tkinter.StringVar(self)
        variable.set("datasets")
        optionmenu = tkinter.OptionMenu(self, variable, *optionList,command=self.optionselect)
        optionmenu.pack()
        
        self.dataset = "not selected yet"
        
        
        
        
        label = tkinter.Label(text="question")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=100)
        label.pack(fill=tkinter.BOTH, expand= 0)
        
        self.entry = tkinter.Entry()
        self.entry.pack(fill=tkinter.BOTH, expand=0)
        
        button = tkinter.Button(text="go", command=self.on_button_click)
        button.pack(fill=tkinter.BOTH, expand=0)
        
        self.label = tkinter.Label(text= "results")
        self.label.pack() 

        label = tkinter.Label(text="")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=300)
        label.pack(fill=tkinter.BOTH, expand= 0)

        
        label = tkinter.Label(text="")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=300)
        label.pack(fill=tkinter.BOTH, expand= 0)
        
        label = tkinter.Label(text="add new dataset")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=300)
        label.pack(fill=tkinter.BOTH, expand= 0)

        label = tkinter.Label(text="enter location of new dataset ")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=400)
        label.pack(fill=tkinter.BOTH, expand= 0)
        self.entry1 = tkinter.Entry()
        self.entry1.pack(fill=tkinter.BOTH, expand=0)

        button1 = tkinter.Button(text="add new dataset", command=self.on_button_click1)
        button1.pack(fill=tkinter.BOTH, expand=0)

        self.entry2 = tkinter.Entry()
        self.entry2.pack(fill=tkinter.BOTH, expand=0)

        button2 = tkinter.Button(text="complaints", command=self.on_button_click2)
        button2.pack(fill=tkinter.BOTH, expand=0)
    
    def optionselect(self,option):
        self.dataset = option
        print (self.dataset)
    
    
    def on_button_click(self):
        question=self.entry.get()
        wordslist = question.split(" ")
        stop_words = ["a","the","I","you","want","what","will","how","would","it","be","if","know","to","going","on"]
        filtered_wordslist = [w for w in wordslist if not w in stop_words]
        
        features_list = self.get_features(self.dataset)
        query_feature_overlap= []
        for word in filtered_wordslist:
            if word in features_list:
                query_feature_overlap.append(word)
        
        print(query_feature_overlap)
        #print your results in string as shown below
        self.label['text'] = "let me work  on it"

    def get_features(self,dataset):
        #get the features in the input dataset and return them as a list
        a = dataset.split(".")
        features = []
        if a[1]=="csv":
            df = pd.read_csv(dataset)
            b = list(df.columns.values)
            for word in b:
                 features.append(word.lower())

        elif a[1]=="xlsx":
            df = pd.read_excel(dataset)
            b = list(df.columns.values)
            for word in b:
                 features.append(word.lower())
            
        return features
    
    def on_button_click1(self,df):
        dataset_location=self.entry1.get()
        loc = dataset_location.split("/")
        filename= loc[-1]
        dest_loc = "./"+filename
        shutil.copyfile(dataset_location,dest_loc)
        preprocessing.missing_value_filling(filename)
        df = feature_engineering.feature_engineering(df)
        todo = 'classfication' #nlp module will be sending this
        models.model(df, todo)


if __name__ == "__main__":
    application = Entry()
    application.mainloop()



#Make the necessary imports
import streamlit as st
import numpy as np
import pandas as pd

import os
import textract
import spacy
import pandas as pd
from fuzzywuzzy import fuzz
# import nltk
# from nltk.corpus import stopwords
# import nltk
# nltk.download()
# nltk.download('stopwords')
stop_words = set()
stop_words.add(".")
stop_words.add(",")
stop_words.add("!")
stop_words.add("(")
stop_words.add(")")
pdf = [] 
final = [] 
corpus1=[]
jjj2=[] 
jjjj2=[]
#Taking inputs and calling the above created functuon to output the prediciton.
def fileget(text1):
    

    path=text1
    for f in os.listdir(path):
        if f.endswith('.pdf') or f.endswith('.xlsx') or f.endswith('.docx') or f.endswith('.pptx') or f.endswith('.png') or f.endswith('.jpg')  :

            pdf.append(f)
            path1 = path+f
            text=textract.process(path1)
            text=b''.join([text])
            inter=text.decode("utf-8")
            if 
            final.append(inter)    
    
    nlp = spacy.load('en_core_web_sm')
     
    for i in final:
        jjjj2.append(i.split('\n'))
     
    
    return jjjj2


from spacy.tokenizer import Tokenizer
from spacy.lang.en import English


def findfeatures1(features ,documents, match=80):
    result=[]
    
    for feature in features:
      count=-1
      
      for d in documents:
        count=count+1
        
        for document in d:
            
            lenfeature = len(feature.split(" "))
            
            word_tokens = nltk.word_tokenize(document)
            filtered_word_tokens = [w for w in word_tokens if not w in stop_words]
            for i in range (len(word_tokens)-lenfeature+1):
                wordtocompare = ""
                j=0
                for j in range(i, i+lenfeature):
                    # if re.search(r'[,!?{}\[\]\"\"\'\']',word_tokens[j]):
                    #     break
                    wordtocompare = wordtocompare+" "+word_tokens[j].lower()
                wordtocompare.strip()
                
                if wordtocompare=="": continue
                else:
                  if (fuzz.ratio(wordtocompare,feature.lower())>= match  or fuzz.partial_ratio(wordtocompare,feature.lower())>= match or fuzz.token_sort_ratio(wordtocompare,feature.lower())>= match or fuzz.token_set_ratio(wordtocompare,feature.lower())>= match):
                      result.append([document,feature,pdf[count]])
                 
                  if fuzz.ratio(wordtocompare,feature.lower())>= match:
                      result.append([document,feature,pdf[count]])

    return result

def main():
    st.title("Enter Path")
    text = st.text_input("Path")
    
    if st.button("Get file"):
     output1=fileget(text)
      #st.success("The Given output is {}".format(output))
    
    context = st.text_input("Context")
    flex = [context]
    if st.button("Find para"):       
      output1=fileget(text)
      output=findfeatures1(flex,output1)
      st.success("The Given output is {}".format(output))

if __name__=="__main__":
    main()

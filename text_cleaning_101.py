import pandas as pd 
import numpy as np 
import nltk
from nltk.corpus import stopwords
import re
import string
import seaborn as sns 
import matplotlib.pyplot as plt
%matplotlib inline

#---------------------------------------------------------------------------------------------------
text=   
      """
      The New York Times (sometimes abbreviated as the NYT and NYTimes) 
      is an American newspaper based in New York City with worldwide influence 
      and readership.[6][7][8] Founded in 1851, the paper has won 127 Pulitzer Prizes, 
      more than any other newspaper.[9][10] The Times is ranked 18th in the world by 
      circulation and 3rd in the U.S.[11] Nicknamed "The Gray Lady,"[12] the Times has 
      long been regarded within the industry as a national "newspaper of record."[13] The paper's motto, 
      "All the News That's Fit to Print," appears in the upper left-hand corner of the front page.
      """
len(text)
#---------------------------------------------------------------------------------------------------
#REMOVE_PUNCTUATION
exclude = set(string.punctuation)
text = ''.join(ch for ch in text if ch not in exclude)
len(text)
#---------------------------------------------------------------------------------------------------
#REMOVE_STOPWORDS
STOPWORDS = set(stopwords.words('english'))
text =  ' '.join([word for word in text.split() if word not in STOPWORDS])
len(text)
#---------------------------------------------------------------------------------------------------

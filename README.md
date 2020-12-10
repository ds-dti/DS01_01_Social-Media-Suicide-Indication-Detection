# Suicide-Prevention-DTI

Is an application that aims to detect a person's twitter post whether they have suicidal tendencies or not. The words from the post will be processed and classified, which will be the percentage label.

Dataset used:
- https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv
- https://raw.githubusercontent.com/reetika-goel/Predict-Suicidal-Ideation-Based-on-Tweets/master/PredictSuicidalIdeationBasedonTweets/Train_suicide1.csv


## Pre-Processing
At this stage there are several functions that help the process including:
- Case Folding
  Converts the entire text in the data into a standard form, which is converts the text to lowercase, remove the link and the word  RT, remove numbers, remove punctuation mark, remove whitespace.
  
- Tokenization
  The stage of truncating the input string based on each word that composes it.
  
- Stemming
  The process of removing suffixes. Reduces the number of variations in the representation of a word.

- Lemmetizer
  A process of finding the basic form of a word.


## API
```
import requests
import json

Base = "http://127.0.0.1:5000/"

my_list = [['kill', 'feel', 'depress'], 
            ['love', 'big', 'family']]

for i in my_list:
    response = requests.post(Base + "Posts", {"tweet": json.dumps(i)})
    print(response.json())
```
Line diatas merupakan script code API yang digunakan dalam projek ini.

## Requirement API
```
requests
```
Kebutuhan yang diperlukan adalah Client melakukan request untuk memanggil API

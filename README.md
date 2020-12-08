# Suicide-Prevention-DTI

Merupakan suatu aplikasi yang dimana mendeteksi suatu post twitter seseorang  yang adanya kecenderungan memiliki kondisi ingin bunuh diri. yang mana dari post tersebut kita dapat melakukan deteksi apakah post itu terindikasi bunuh diri atau tidak.

Dataset yang digunakan 
- https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv
- https://raw.githubusercontent.com/reetika-goel/Predict-Suicidal-Ideation-Based-on-Tweets/master/PredictSuicidalIdeationBasedonTweets/Train_suicide1.csv


## Penjelasan Pre-Processing
```
import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv', sep=',')
df1 = df1.drop(['url', 'num_comments', 'author', 'title', 'selftext', 'selftext_clean', 'title_clean', 'author_clean', 'selftext_length', 'title_length'], axis=1)
df1 = df1.dropna()
df1.head()
```

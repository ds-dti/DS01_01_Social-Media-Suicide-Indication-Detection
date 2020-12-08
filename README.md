# Suicide-Prevention-DTI

Merupakan suatu aplikasi yang dimana mendeteksi suatu post twitter seseorang  yang adanya kecenderungan memiliki kondisi ingin bunuh diri. yang mana dari post tersebut kita dapat melakukan deteksi apakah post itu terindikasi bunuh diri atau tidak.

Dataset yang digunakan 
- https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv
- https://raw.githubusercontent.com/reetika-goel/Predict-Suicidal-Ideation-Based-on-Tweets/master/PredictSuicidalIdeationBasedonTweets/Train_suicide1.csv


## Penjelasan Pre-Processing
import pandas as pd
df1 = pd.read_csv('https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv', sep=',')
df1 = df1.drop(['url', 'num_comments', 'author', 'title', 'selftext', 'selftext_clean', 'title_clean', 'author_clean', 'selftext_length', 'title_length'], axis=1)
df1 = df1.dropna()
df1.head()
Line diatas membaca isi dataset pertama dan dijabarkan dengan tabel

df2 = pd.read_csv('https://raw.githubusercontent.com/reetika-goel/Predict-Suicidal-Ideation-Based-on-Tweets/master/PredictSuicidalIdeationBasedonTweets/Train_suicide1.csv', sep=',')
df2.loc[df2['Suicide'] == "Potential Suicide post ", "Suicide"] = 1
df2.loc[df2['Suicide'] == "Not Suicide post", "Suicide"] = 2
df2 = df2.rename(columns = {'Tweet': 'megatext_clean', 'Suicide': 'is_suicide'}, inplace = False)
df2.is_suicide.astype('int')
df2.head()
Line diatas membaca isi dataset kedua dan dijabarkan dengan tabel

df = pd.concat([df1, df2], ignore_index=True, sort=False)
df.loc[df['is_suicide'] == 1, "is_suicide"] = "suicide"
df.loc[df['is_suicide'] == 0, "is_suicide"] = "depression"
df.loc[df['is_suicide'] == 2, "is_suicide"] = "normal"
df.shape
Menggabungkan dataset pertama dengan dataset kedua, dan dibuat label berdasarkan indeks diawali dengan 0.

df = df.dropna()
df.isnull().sum()

import matplotlib.pyplot as plt

labels = ['Normal', 'Depression','Suicide']
size = df['is_suicide'].value_counts()
colors = ['green', 'yellow','red']
explode = [0, 0.05, 0.1]

plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(size, colors = colors, explode = explode, labels = labels, shadow = True, autopct = '%.2f%%')
plt.title('Labels', fontsize = 20)
plt.axis('off')
plt.legend()
plt.show()
Line diatas menampilkan banyaknya persentase dari masing-masing label yang dipakai.

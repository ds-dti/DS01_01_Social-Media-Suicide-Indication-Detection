# Suicide-Prevention-DTI

Merupakan suatu aplikasi yang dimana mendeteksi suatu post twitter seseorang  yang adanya kecenderungan memiliki kondisi ingin bunuh diri. yang mana dari post tersebut kita dapat melakukan deteksi apakah post itu terindikasi bunuh diri atau tidak.

Dataset yang digunakan 
- https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv
- https://raw.githubusercontent.com/reetika-goel/Predict-Suicidal-Ideation-Based-on-Tweets/master/PredictSuicidalIdeationBasedonTweets/Train_suicide1.csv


## Penjelasan Pre-Processing
```
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 

# Case Folding
# Convert text to lowercase
df['megatext_clean'] = df['megatext_clean'].str.lower()

# Remove Twitter megatext_clean Link and RT word
df['megatext_clean'] = df['megatext_clean'].replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True).replace(r'rt', '', regex=True)

# Remove number
df['megatext_clean'] = df['megatext_clean'].str.replace('\d+', '')

# Remove Punctuation
df['megatext_clean'] = df['megatext_clean'].str.replace('[^\w\s]','')

# Remove Whitespaces
df["megatext_clean"] = df['megatext_clean'].str.strip()

# Tokenization
df["megatext_clean"] = df["megatext_clean"].apply(nltk.word_tokenize)

# StopWords Removal
stop_words = set(stopwords.words('english'))
df["megatext_clean"] = df["megatext_clean"].apply(lambda x: [item for item in x if item not in stop_words])

# Stemming
ps = PorterStemmer()
df['megatext_clean'] = df['megatext_clean'].apply(lambda x: [ps.stem(item) for item in x])

# Lemmetizer
lemmatizer = WordNetLemmatizer()
df['megatext_clean'] = df['megatext_clean'].apply(lambda x: [lemmatizer.lemmatize(item) for item in x])

df.shape
```
Pada linecode pre-processing terdapat fungsi-fungsi diantaranya:
1. Mengubah teksnya menjadi huruf kecil
2. Menghapus link dan kata RT
3. Menghapus angka
4. Menghapus tanda baca
5. Menghapus spasi
6. Tokenisasi
7. Menghapus StopWords
8. Melakukan Stemming dan Lemmetizer

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

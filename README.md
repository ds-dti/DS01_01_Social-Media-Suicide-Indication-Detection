# Suicide-Prevention-DTI

Is an application that aims to detect a person's twitter post whether they have suicidal tendencies or not. The words from the post will be processed and classified, which will be the percentage label.

Dataset used:
- https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv
- https://raw.githubusercontent.com/reetika-goel/Predict-Suicidal-Ideation-Based-on-Tweets/master/PredictSuicidalIdeationBasedonTweets/Train_suicide1.csv


## Pre-Processing

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

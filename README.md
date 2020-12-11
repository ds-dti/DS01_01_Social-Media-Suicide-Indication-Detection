# Suicide-Prevention-DTI

Is an application that aims to detect a person's twitter post whether they have suicidal tendencies or not. The words from the post will be processed and classified, which will be the percentage label.

Label are used in between :
- Suicide
- Normal

Dataset used:
- https://raw.githubusercontent.com/hesamuel/goodbye_world/master/data/data_for_model_2.csv
- https://raw.githubusercontent.com/reetika-goel/Predict-Suicidal-Ideation-Based-on-Tweets/master/PredictSuicidalIdeationBasedonTweets/Train_suicide1.csv


## Pre-Processing
At this stage there are several functions that help the process including:
- Case Folding converts the entire text in the data into a standard form.
   - Converts the text to lowercase
   - Remove the link and the word  RT 
   - Remove numbers 
   - Remove punctuation mark
   - Remove whitespace.
  
- Tokenization the stage of truncating the input string based on each word that composes it.
  
- Stemming the process of removing suffixes. Reduces the number of variations in the representation of a word.

- Lemmetizer a process of finding the basic form of a word.

- Text Vectorization is the process of converting text into numerical representation.

## Model
On this project, we used neural network to classified the data.
![Model Layer](Image/model_layer.png)

On the neural network layer, we used ReLU (Rectified Linear Unit) function, and Dropout Regularization to reduce overfitting.

![Accuracy](Image/accuracy.PNG)
The accuracy we get after being classified is 95%

## API Explanation
The Suicide Prevention API provides access to Neural Network that can predict suicidial from text. this api build from flask framework and deploy on heroku
by using POST and /Posts method to communicate with api.

API End point
```
POST   https://suicideprevention.herokuapp.com/Posts
```

Parameter
```
tweet string text to be predicted it's meaning suicide or normal
```

## How to use API
Make file api.py, write this code, and run it !
```
import requests
import json

Base = "https://suicideprevention.herokuapp.com/"

my_list = [['understand people reply immediately op invitation talk privately mean help type response usually lead either disappointment disaster usually work quite differently say pm anytime casual social context huge admiration appreciation goodwill good citizenship many support others flag inappropriate content even know many struggling hard work behind scene information resource make easier give get quality help small start new wiki page explains detail much better respond public comment least gotten know someone maintained r depression wiki private_contact full text current version summary anyone acting helper invite accepts private contact e pm chat kind offsite communication early conversion showing either bad intention bad judgement either way unwise trust pm anytime seems like kind generous offer might perfectly well meaning unless solid rapport ha established wise idea point consider offer accept invitation communicate privately posting supportive reply publicly help people op response good quality educate inspire helper 1 9 90 rule http en wikipedia org wiki 1 25_rule_ internet_culture applies much doe anywhere else internet people struggling serious mental health issue often justifiably low tolerance disappointment high level ever changing emotional need unless helper able make 100 commitment every way long necessary offering personal inbox resource likely harm good mental health crisis line responder usually give name caller allowed request specific responder much healthier safer caller develop relationship agency whole analogously much safer healthier ops develop relationship community whole even trained responder generally allowed work high intensity situation alone partly availability mostly wider perspective preventing compassion fatigue helper get head someone whose mental health issue including suicidality often comorbid depression escalate pm conversation much harder others including r depression r suicidewatch moderator help contrary common assumption moderator see police pm observation many year people say pm consistently one least understanding mental health issue mental health support gap knowledge ability communicate effectively community input mitigates limitation reason someone truly help would want hide response community scrutiny helper concerned privacy keep mind self disclosure used supportively feeling detail problem use alt throwaway account restriction account age karma know internet used people exploit abuse others people want hide deceptive manipulative response everyone except victim many specifically target vulnerable mental health issue helper invite op talk privately give good supportive experience primed person vulnerable abuser sort cognitive priming tends particularly effective someone state mental health crisis people rely heuristic critical reasoning ops want talk privately posting wide open anonymous forum like reddit might best option although recommend allow ops request private contact asking support want please keep expectation realistic careful look history anyone offer pm opening broken least understood rule helper may invite private contact first resort made new wiki explain'], 
            ['God damn vending machines are so depressing -standing at them waiting for your sad little snack like some Pavlovian bitch! Happy Tuesday!']]

for i in my_list:
    response = requests.post(Base + "Posts", {"tweet": i})
    print(response.json())
```

The Result will be json file like this :
```
{
'probability': 0.6786270141601562
}
```
The code above is API testing used in this application.



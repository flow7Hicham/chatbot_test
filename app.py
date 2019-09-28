# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_most_frequent_response
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from traduction import *
app = Flask(__name__)
#userText = ""
bot = ChatBot(
    "MOURCHID_BOT",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    #tie_breaking_method="random_response",
    #database_uri="mysql://root:hajji1996@localhost:3306/databasename",
    response_selection_method=get_most_frequent_response ,
    statement_comparison_function=levenshtein_distance,
    logic_adapters=[
                #'chatterbot.logic.MathematicalEvaluation',
                #'chatterbot.logic.TimeLogicAdapter',
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'maximum_similarity_threshold': 0.65,
                    'default_response': 'I am sorry, but I do not understand.',
                    #'response_selection_method':'chatterbot.comparisons.get_random_response',
                    'statement_comparison_function':'levenshtein_distance',


                }
            ]
)
trainer = ChatterBotCorpusTrainer(bot)
for _file in os.listdir('french'):
    #chats = open('chats/'+_file , 'r',encoding="utf-8").readlines()
    trainer.train('french/'+_file )





@app.route("/")
def home():
    return render_template("index_test2.html")

@app.route("/get")
def get_bot_response():
    userText = str(request.args.get('msg'))
    test = str(request.args.get('test'))
    userLanguage = detected_langue(userText)
    print("\n \n \n \n"+ userLanguage +"\n \n \n \n")
    userText = correct(userText,userLanguage)
    print("\n \n \n \n"+ userText +"\n \n \n \n")
    userText = traduction(userText,'fr')
    print("\n \n \n \n"+ userText +"\n \n \n \n")
    if test =='false':    
        response = str(bot.get_response(userText)).split('/')
        if 'multiple' in response[0]:
            categore = response[0].split("-")
            Langeur = len(categore)
            multiple=""
            for i in range(1,Langeur):
                multiple +=str(i)+"==" + str(categore[i]) + " "
            rest = traduction(response[1],userLanguage)
            return str(rest + ":true:"+ multiple)
        else:
            if response[0] == 'I am sorry, but I do not understand.':
                return ":false:" + 'I am sorry, but I do not understand.'
            else :
                return str(":false:" + traduction(str(response[0]),userLanguage))
    else:
        old_responce = str(request.args.get('response')).split("-")
        index = int(userText) 
        
        return  str(":false:"+old_responce[index-1])
        

@app.route("/new_question")
def new_question():
    userText = str(request.args.get('no_response'))
    email = str(request.args.get('email'))
    file = open("text.txt",'a')
    file.write(userText + ":"+ email +"\n")
    return 'merci'
    


if __name__ == "__main__":
    app.run(port=8000)

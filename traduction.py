# -*- coding: utf-8 -*-
from googletrans import Translator
from textblob import TextBlob 
from textblob import Blobber

from textblob_fr import PatternTagger, PatternAnalyzer

def correct(responce , srclangue):
    if srclangue == 'fr':
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        responce =str(TextBlob(responce).correct())
    if srclangue == 'en' :
        responce = str(TextBlob(responce).correct())
    return responce 
    
def traduction(responce,langue):
    translator = Translator(service_urls=['translate.google.com']) 
    #tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    #responce =str(TextBlob(responce).correct())
    print("\n \n \n \n"+ responce +"\n \n \n \n")
    translatedList = translator.translate([responce], dest=langue)
   
    for translated in translatedList:
          return translated.text 
           
#print(type(traduction("have a good day","ar")))
def detected_langue(response):
    translator = Translator(service_urls=['translate.google.com']) 
#translated = translator.translate('matbakhe')
    detected = translator.detect(response)
    if detected.lang == 'cafr':
        return 'fr'
    return detected.lang

#print(detected_langue("salut"))

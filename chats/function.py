import pyttsx3


class Voix():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)    # Speed percent (can go over 100)
        self.engine.setProperty('volume', 0.9)
        
    def Parler(self,phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()
        
    
def new_question(qst):
    file = open('new_question/new_chat.txt','a')
    file.write(qst+'\n')
    file.close() 


def erru():
    print("Sur quel categore a yu la question ")
    categore = input(" 1-Murabaha \n 2-Idjar \n 3-Musharaka \n" )
    if categore == 1:
        cate = "Mourabaha"
    elif categore == 2 :
        cate = "Ijar"
    else :
        cate = "Moucharaka"
        
    file=open('video/liste_video.txt' ,'r').readlines()
    
    print("vous pouvez voir ce video ")
    
    
    for i in file :
        if i.split(":")[0]==cate:
            print(i.split(":")[1])


def link_image(categorie):
    file = open("liste_image.txt",'r').readlines()
    for _link in file:
        if _link.split(":")[0] == categorie:
            return _link.split(":")[2]

def link_text(categorie):
  file = open("liste_image.txt",'r').readlines()
  for _link in file:
    if _link.split(":")[0] == categorie:
                  return _link.split(":")
       
 

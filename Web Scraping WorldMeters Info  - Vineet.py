import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import pyaudio
import threading
import time

api_key = "tovjT6M2qoOH"
project_token = "tLJhBs-2zyEG"
run_token = "txM5MJLCH52J"

response = requests.get(f"https://parsehub.com/api/v2/projects/{project_token}/last_ready_run/data", params={"api_key": api_key})
data = json.loads(response.text)
class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {"api_key": self.api_key}
        self.data = self.get_data()

    def get_data(self):
        response = requests.get(f"https://parsehub.com/api/v2/projects/{project_token}/last_ready_run/data", params={"api_key": api_key})
        data = json.loads(response.text)
        return data

    def get_current_world_population(self, information):
        data = self.data["Information"]

        for content in data:
            if content["name"] == information:
                return content["value"]
    def update_data(self):
        response = requests.post(f"https://parsehub.com/api/v2/projects/{project_token}/run", params={"api_key": api_key})

        def poll():
            time.sleep(0.1)
            old_data = self.data
            while True:
                new_data = self.get_data()
                if new_data != old_data:
                    self.data = new_data
                    speak("Data updated")
                    break
                time.sleep(5)
                
        t = threading.Thread(target = poll)
        t.start()

                        #list of possible information
l1 = ['Current World Population', 'Births this year', 'Births today',
'Deaths this year', 'Deaths today', 'Net population growth this year',
'Net population growth today', 'Public Healthcare expenditure today',
'Public Education expenditure today', 'Public Military expenditure today',
'Cars produced this year', 'Bicycles produced this year',
'Computers produced this year', 'New book titles published this year',
'Newspapers circulated today', 'TV sets sold worldwide today',
'Cellular phones sold today', 'Money spent on videogames today',
'Internet users in the world today', 'Emails sent today',
'Blog posts written today', 'Tweets sent today', 'Google searches today',
'Undernourished people in the world', 'Overweight people in the world',
'Obese people in the world', 'People who died of hunger today',
'Money spent for obesity related\ndiseases in the USA today',
'Money spent on weight loss\nprograms in the USA today',
'Deaths caused by water related\ndiseases this year',
'People with no access to\na safe drinking water source',
'Days to the end of natural gas', 
'Days to the end of coal', 'Communicable disease deaths this year',
'Seasonal flu deaths this year', 'Deaths of children under 5 this year',
'Abortions this year', 'Deaths of mothers during birth this year',
'HIV/AIDS infected people', 'Deaths caused by HIV/AIDS this year',
'Deaths caused by cancer this year', 'Deaths caused by malaria this year',
'Cigarettes smoked today', 'Deaths caused by smoking this year',
'Deaths caused by alcohol this year', 'Suicides this year',
'Money spent on illegal drugs this year',
'Road traffic accident fatalities this year']


def speak(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception", str(e))
        return said.lower()

def main():
    print("Started Program")
    text = ""
    data = Data(api_key, project_token) 
    while "stop" not in text:
        print("Listening...")
        text = get_audio()
        print(text)
        if text == "update":
            data.update_data()
            speak("Data is being updated. This may take a moment!")

        for phrase in l1:
            length = (phrase.split())
            d = 0
            
            allwords = True
            while d < len(length):
                if length[d].lower() not in text:
                    allwords = False
                d += 1
            if allwords == True:
                output = (phrase + ": " + data.get_current_world_population(phrase))
                speak(output)
    speak("Program Ended")
main()


        

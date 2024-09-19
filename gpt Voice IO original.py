# GPT-3 with Voice Input and Output
#--------------------------------------
# Download and install the following Libraries: 
#   pip3 install SpeechRecognition pydub
#   pip3 install pyaudio
#   pip install playsound

import pyttsx3 ### Text to speech library
import winsound ### for beep sound
import speech_recognition as sr ### for Google's speech recognition
import openai #333 GPT 3 library
import json
import zzzkeys
import time

openai.api_key = "your openAI API key goes here!" #This code won't work without your own API key from OpenAI
r = sr.Recognizer()

print("\r\r")

myInput = "Starting"

while myInput != ("goodbye"):
  """ Record User's Voice and Return Text """
  with sr.Microphone() as source:
    winsound.Beep(400, 20)
    print("Waiting for user input... (\'goodbye\' ends the conversation)")
    audio_data = r.record(source, duration=3)
    text = r.recognize_google(audio_data)  # convert speech to text
    print("")
    print("  -->>> Text heard: ", text)
    print("")
    winsound.Beep(400, 20)

  """ Send Input to GPT """
  myInput = text
  response = openai.Completion.create(
    model="davinci-text-2",
    prompt=f"AI: What have you been up to?\n Human: Not much. You? \n AI:Not much. \n Human: {myInput}\n",
    #truncate=5, #cuts off GPT's reply when it sees the first period. 
    temperature=0.9, #randomness of replies. 0=not at all random. 1= very random.
    max_tokens=25, #maximum number of tolkens (groups of 4 characters) returned from GPT
    top_p=.9, # higher = more random selection of next word
    frequency_penalty=0.9, # reduces repitition of words
    presence_penalty=0.9, # lowers the probability of a word if it already appeared in the predicted text. 
    stop=["Human:"] #used to make the model stop at a desired point
  )

  GPT_Reply=response["choices"][0]["text"] # parse out just the reply from GPT

  GPT_Reply = GPT_Reply[:GPT_Reply.find(".") or GPT_Reply.find("?")]
  print(GPT_Reply)

  """ Speak GPT's Reply """
  engine = pyttsx3.init() # object creation
  engine.setProperty('rate', 100)     # setting up new voice rate
  voices = engine.getProperty('voices')       #getting list of current voices
  engine.setProperty('voice', voices[0].id)   #changing voices index to change voice
  engine.setProperty('rate', 150)             #talking speed
  GPT_Reply=GPT_Reply.replace("AI:","")       #remove the text "AI"
  engine.say(GPT_Reply)                       # finally SAY the reply that came from GPT
  print("")
  print("  -->>> Reply from GPT: ", GPT_Reply)
  print("")
  engine.runAndWait()
  engine.stop()

print('(Conversation is over)')



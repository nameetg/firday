import speech_recognition as sr
import webbrowser
import pyttsx3
import youtubeMusic


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(c):
  if 'open google' in c.lower():
    webbrowser.open('https://google.com')
  elif 'open facebook' in c.lower():
    webbrowser.open('https://facebook.com')
  elif 'open linkedin' in c.lower():
    webbrowser.open('https://linkedin.com')
  elif 'open instagram' in c.lower():
    webbrowser.open('https://instagram.com')
  elif 'open youtube' in c.lower():
    webbrowser.open('https://youtube.com')
  elif c.lower().startswith('play'):
    song = c.lower().split(' ')[1]
    link = youtubeMusic.music[song]
    webbrowser.open(link)
  
if __name__ == '__main__':
  speak('Initializing friday')

  while True:
    r = sr.Recognizer()
    

    try:
      with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source, timeout=2, phrase_time_limit=1)
      command = r.recognize_google(audio)
      if(command.lower() == 'friday'):
        speak('Yes')
        with sr.Microphone() as source:
          print('friday active...')
          audio = r.listen(source)
          command = r.recognize_google(audio)

          processCommand(command)
          
    except Exception as e:
      print('sphinx error; {e}')

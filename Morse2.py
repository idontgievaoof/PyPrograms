import string
import random
import time

def randomCharSelector():
  pool = string.ascii_lowercase + string.digits
  return random.choice(pool)


from pydub import AudioSegment
from pydub.playback import play
import os

AUDIO_DIR=r"morseAudioFiles"

def playAudio(question):
  filename=f"{question.lower()}.wav"
  filepath=os.path.join(AUDIO_DIR,filename)

  if not os.path.exists(filepath):
    print(f"Error: Audio file not found for '{question}' at {filepath}")
    return

  try:
    print(filepath)
    audio = AudioSegment.from_file(filepath)
    play(audio)
    
    time.sleep(0.5)
    print("i played the audio")
    print(f"{question} is the answer")
    
  except Exception as e:
    print(f"An error occurred while playing audio for '{question}': {e}")

  return question


def checkAnswer(question, answer):
  if question.lower() == answer.lower():
    return 1
  else:
    return 0

def main():
  print("Type any letter when ready")
  ready=None
  ready=input()

  if ready == "stop and exit":
    return
  elif ready is not None:
    while True:
      flag=0
      lives=3
      answer=None

      while flag == 0 and lives>0:

        print("Playing audio...")

        #call fnc to play audio for morse code of some random letter/ no.
        #this fnc also returns the correct answer
        question = randomCharSelector()
        playAudio(question)
        print("returned to main")

        print("Audio finished playing")
        print("Enter your answer")
        answer=input()

        if answer == "stop and exit":
          return

        #send correct ans and user's answer to a func to check
        #the fnc returns variable called flag a 1 for correct and 0 for wrong
        flag=checkAnswer(question, answer)

        if flag == 1:
          print("Correct")
          break
        else:
          print("Wrong")
          lives=lives-1
          print(f"You have {lives} lives left")

      if answer == "stop and exit":
        return

      if lives == 0:
        print("You have no more lives left")
        print(f"Correct answer was {question}")



if __name__ == "__main__":
  main()

import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

print("Text-to-Speech Program (type 'stop' to quit)\n")

while True:
    text =input("Enter the text: ")
    
    if text.lower() == "stop":
        print("Program stopped by user.")
        break

    engine.say(text)
    engine.runAndWait()

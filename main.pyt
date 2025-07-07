
# Jarvis AI - A Personal Assistant using Python
# This script uses speech recognition, text-to-speech, and OpenAI's ChatGPT API
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import openai

# --- SETUP ---
openai.api_key = "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"  # 🔐 Never share your real key in public code

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

def speak(text):
    print("Jarvis:", text)
    speaker.say(text)
    speaker.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = listener.listen(source, timeout=5, phrase_time_limit=7)
            command = listener.recognize_google(audio).lower().strip()
            print(f"[DEBUG] You said: {command}")
            return command
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, there was a problem with the speech recognition service.")
        return ""

def match_command(command, keywords):
    return any(keyword in command for keyword in keywords)

# --- CHATGPT API LOGIC ---
def ask_chatgpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=150,
            temperature=0.7
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        print(e)
        return "Sorry, I couldn't connect to ChatGPT."

# --- MAIN FUNCTION ---
def run_jarvis():
    speak("Hello Sir! I'm ready to assist you.")

    while True:
        command = take_command()

        if match_command(command, ["notepad", "open notepad"]):
            speak("Opening Notepad")
            os.startfile("notepad")

        elif match_command(command, ["file explorer", "open file explorer"]):
            speak("Opening File Explorer")
            os.system("explorer")

        elif match_command(command, ["chrome", "open chrome", "google chrome"]):
            speak("Opening Google Chrome")
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif match_command(command, ["youtube", "open youtube"]):
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif match_command(command, ["microsoft edge", "open edge"]):
            speak("Opening Microsoft Edge")
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edge_path)

        elif match_command(command, ["calculator", "open calculator"]):
            speak("Opening Calculator")
            os.system("calc")

        elif match_command(command, ["create folder", "make folder", "new folder"]):
            speak("What should I name the folder?")
            folder_name = take_command()

            if folder_name:
                base_path = "C:\\Users\\kumar\\Desktop"
                folder_path = os.path.join(base_path, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    speak(f"Folder named {folder_name} has been created.")
                else:
                    speak("A folder with that name already exists.")
            else:
                speak("I didn't get the folder name.")

        elif match_command(command, ["ask chatgpt", "question", "chat gpt"]):
            speak("What do you want to ask ChatGPT?")
            user_question = take_command()

            if user_question:
                speak("Thinking...")
                answer = ask_chatgpt(user_question)
                speak(answer)

        elif match_command(command, ["exit", "stop", "quit", "shutdown"]):
            speak("Goodbye Sir! Shutting down.")
            break

        elif command != "":
            speak("Sorry, I don't know that command yet.")

# --- START JARVIS ---
run_jarvis()
import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import subprocess
import os
import datetime
import random


# ============================================================
# JARVIS VOICE ENGINE
# ============================================================

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# ============================================================
# SPEECH RECOGNITION
# ============================================================

recognizer = sr.Recognizer()


def listen():

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        command = command.lower()

        print("You:", command)

        return command

    except sr.WaitTimeoutError:

        print("No speech detected.")
        return ""

    except sr.UnknownValueError:

        speak("Sorry, I could not understand that.")
        return ""

    except sr.RequestError:

        speak("Speech recognition service is unavailable.")
        return ""

    except Exception as e:

        print("Error:", e)
        return ""


# ============================================================
# OPEN SPOTIFY
# ============================================================

def open_spotify():

    speak("Opening Spotify")

    webbrowser.open(
        "https://open.spotify.com/"
    )


# ============================================================
# PLAY MUSIC
# ============================================================

def play_music():

    speak("What music do you want to play?")

    music = listen()

    if music:

        speak("Searching for " + music)

        pywhatkit.playonyt(music)


# ============================================================
# OPEN GOOGLE
# ============================================================

def open_google():

    speak("Opening Google")

    webbrowser.open(
        "https://www.google.com"
    )


# ============================================================
# GOOGLE SEARCH
# ============================================================

def google_search(command):

    search_text = command.replace(
        "search google",
        ""
    ).strip()

    if search_text == "":

        speak("What should I search on Google?")

        search_text = listen()

    if search_text:

        speak(
            "Searching Google for "
            + search_text
        )

        url = (
            "https://www.google.com/search?q="
            + search_text.replace(" ", "+")
        )

        webbrowser.open(url)


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(command):

    search_text = command.replace(
        "search youtube",
        ""
    ).strip()

    if search_text == "":

        speak("What should I search on YouTube?")

        search_text = listen()

    if search_text:

        speak(
            "Searching YouTube for "
            + search_text
        )

        pywhatkit.search(search_text)


# ============================================================
# PLAY YOUTUBE
# ============================================================

def play_youtube():

    speak("What do you want me to play?")

    song = listen()

    if song:

        speak("Playing " + song)

        pywhatkit.playonyt(song)


# ============================================================
# OPEN CHROME
# ============================================================

def open_chrome():

    speak("Opening Google Chrome")

    chrome_paths = [

        r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",

        os.path.expanduser(
            r"~\AppData\Local\Google\Chrome\Application\chrome.exe"
        )
    ]

    chrome_found = False

    for path in chrome_paths:

        if os.path.exists(path):

            subprocess.Popen(path)

            chrome_found = True

            break

    if not chrome_found:

        speak(
            "Chrome was not found. Opening Google instead."
        )

        webbrowser.open(
            "https://www.google.com"
        )


# ============================================================
# OPEN NOTEPAD
# ============================================================

def open_notepad():

    speak("Opening Notepad")

    subprocess.Popen(
        "notepad.exe"
    )


# ============================================================
# OPEN CALCULATOR
# ============================================================

def open_calculator():

    speak("Opening Calculator")

    subprocess.Popen(
        "calc.exe"
    )


# ============================================================
# OPEN FILE EXPLORER
# ============================================================

def open_file_explorer():

    speak("Opening File Explorer")

    subprocess.Popen(
        "explorer.exe"
    )


# ============================================================
# OPEN COMMAND PROMPT
# ============================================================

def open_command_prompt():

    speak("Opening Command Prompt")

    subprocess.Popen(
        "cmd.exe"
    )


# ============================================================
# OPEN POWERSHELL
# ============================================================

def open_powershell():

    speak("Opening PowerShell")

    subprocess.Popen(
        "powershell.exe"
    )


# ============================================================
# OPEN VS CODE
# ============================================================

def open_vscode():

    speak("Opening Visual Studio Code")

    try:

        subprocess.Popen("code")

    except:

        speak(
            "Visual Studio Code command was not found."
        )


# ============================================================
# OPEN DOWNLOADS
# ============================================================

def open_downloads():

    speak("Opening Downloads folder")

    downloads = os.path.join(
        os.path.expanduser("~"),
        "Downloads"
    )

    if os.path.exists(downloads):

        os.startfile(downloads)

    else:

        speak(
            "Downloads folder was not found."
        )


# ============================================================
# OPEN DOCUMENTS
# ============================================================

def open_documents():

    speak("Opening Documents folder")

    documents = os.path.join(
        os.path.expanduser("~"),
        "Documents"
    )

    if os.path.exists(documents):

        os.startfile(documents)

    else:

        speak(
            "Documents folder was not found."
        )


# ============================================================
# OPEN DESKTOP
# ============================================================

def open_desktop():

    speak("Opening Desktop")

    desktop = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    if os.path.exists(desktop):

        os.startfile(desktop)

    else:

        speak(
            "Desktop folder was not found."
        )


# ============================================================
# OPEN PICTURES
# ============================================================

def open_pictures():

    speak("Opening Pictures folder")

    pictures = os.path.join(
        os.path.expanduser("~"),
        "Pictures"
    )

    if os.path.exists(pictures):

        os.startfile(pictures)

    else:

        speak(
            "Pictures folder was not found."
        )


# ============================================================
# OPEN VIDEOS
# ============================================================

def open_videos():

    speak("Opening Videos folder")

    videos = os.path.join(
        os.path.expanduser("~"),
        "Videos"
    )

    if os.path.exists(videos):

        os.startfile(videos)

    else:

        speak(
            "Videos folder was not found."
        )


# ============================================================
# OPEN MUSIC FOLDER
# ============================================================

def open_music_folder():

    speak("Opening Music folder")

    music = os.path.join(
        os.path.expanduser("~"),
        "Music"
    )

    if os.path.exists(music):

        os.startfile(music)

    else:

        speak(
            "Music folder was not found."
        )


# ============================================================
# OPEN WINDOWS SETTINGS
# ============================================================

def open_settings():

    speak("Opening Windows Settings")

    subprocess.Popen(
        "start ms-settings:",
        shell=True
    )


# ============================================================
# OPEN CONTROL PANEL
# ============================================================

def open_control_panel():

    speak("Opening Control Panel")

    subprocess.Popen(
        "control.exe"
    )


# ============================================================
# OPEN TASK MANAGER
# ============================================================

def open_task_manager():

    speak("Opening Task Manager")

    subprocess.Popen(
        "taskmgr.exe"
    )


# ============================================================
# OPEN YOUR APPLICATION
# ============================================================

def open_my_application():

    speak("Opening your application")

    # CHANGE THIS PATH TO YOUR APPLICATION

    application_path = (
        r"C:\Users\HP\Desktop\JARVIS 2.O"
    )

    if os.path.exists(application_path):

        subprocess.Popen(
            application_path
        )

    else:

        speak(
            "Your application path has not been configured."
        )


# ============================================================
# OPEN CUSTOM FOLDER
# ============================================================

def open_custom_folder():

    speak(
        "Enter the folder path in the terminal."
    )

    path = input(
        "Folder path: "
    ).strip()

    if os.path.exists(path):

        os.startfile(path)

        speak(
            "Opening the folder."
        )

    else:

        speak(
            "That folder does not exist."
        )


# ============================================================
# TIME
# ============================================================

def tell_time():

    current_time = datetime.datetime.now().strftime(
        "%I:%M %p"
    )

    speak(
        "The current time is "
        + current_time
    )


# ============================================================
# DATE
# ============================================================

def tell_date():

    current_date = datetime.datetime.now().strftime(
        "%d %B %Y"
    )

    speak(
        "Today's date is "
        + current_date
    )


# ============================================================
# DAY
# ============================================================

def tell_day():

    today = datetime.datetime.now().strftime(
        "%A"
    )

    speak(
        "Today is "
        + today
    )


# ============================================================
# GREETINGS
# ============================================================

def greetings():

    hour = datetime.datetime.now().hour

    if hour < 12:

        speak(
            "Good morning!"
        )

    elif hour < 18:

        speak(
            "Good afternoon!"
        )

    else:

        speak(
            "Good evening!"
        )

    speak(
        "How can I help you?"
    )


# ============================================================
# JOKE
# ============================================================

def tell_joke():

    jokes = [

        "Why did the programmer quit his job? Because he didn't get arrays.",

        "Why do programmers prefer dark mode? Because light attracts bugs.",

        "There are only 10 types of people in the world. Those who understand binary and those who don't.",

        "Why was the computer cold? Because it left its Windows open."
    ]

    speak(
        random.choice(jokes)
    )


# ============================================================
# LOCK COMPUTER
# ============================================================

def lock_computer():

    speak(
        "Locking the computer."
    )

    os.system(
        "rundll32.exe user32.dll,LockWorkStation"
    )


# ============================================================
# SHUTDOWN COMPUTER
# ============================================================

def shutdown_computer():

    speak(
        "Are you sure you want to shut down the computer?"
    )

    confirmation = listen()

    if (
        "yes" in confirmation
        or "confirm" in confirmation
    ):

        speak(
            "The computer will shut down in five seconds."
        )

        os.system(
            "shutdown /s /t 5"
        )

    else:

        speak(
            "Shutdown cancelled."
        )


# ============================================================
# RESTART COMPUTER
# ============================================================

def restart_computer():

    speak(
        "Are you sure you want to restart the computer?"
    )

    confirmation = listen()

    if (
        "yes" in confirmation
        or "confirm" in confirmation
    ):

        speak(
            "The computer will restart in five seconds."
        )

        os.system(
            "shutdown /r /t 5"
        )

    else:

        speak(
            "Restart cancelled."
        )


# ============================================================
# CANCEL SHUTDOWN
# ============================================================

def cancel_shutdown():

    os.system(
        "shutdown /a"
    )

    speak(
        "Shutdown or restart has been cancelled."
    )


# ============================================================
# COMMAND PROCESSOR
# ============================================================

def process_command(command):

    command = command.lower().strip()


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if (
        command == "exit"
        or command == "quit"
        or command == "stop jarvis"
        or command == "goodbye"
    ):

        speak(
            "Goodbye! Have a great day."
        )

        return False


    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    elif (
        "hello" in command
        or "hi jarvis" in command
        or "hey jarvis" in command
    ):

        greetings()


    elif "good morning" in command:

        speak(
            "Good morning! Have a great day."
        )


    elif "good afternoon" in command:

        speak(
            "Good afternoon! How can I help you?"
        )


    elif "good evening" in command:

        speak(
            "Good evening! What can I do for you?"
        )


    # --------------------------------------------------------
    # CONDITIONAL RESPONSES
    # --------------------------------------------------------

    elif "how are you" in command:

        speak(
            "I am doing great. Thank you for asking!"
        )


    elif "who are you" in command:

        speak(
            "I am Jarvis, your personal AI assistant."
        )


    elif "what can you do" in command:

        speak(
            "I can search Google, search YouTube, "
            "play music, open applications, open folders, "
            "control Windows and answer your questions."
        )


    elif "are you there" in command:

        speak(
            "Yes, I am here and ready to help."
        )


    elif "wake up" in command:

        speak(
            "I am awake and ready."
        )


    elif (
        "thank you" in command
        or "thanks" in command
    ):

        speak(
            "You're welcome!"
        )


    # --------------------------------------------------------
    # GOOGLE
    # --------------------------------------------------------

    elif command == "open google":

        open_google()


    elif (
        "search google" in command
        or "google search" in command
    ):

        google_search(command)


    # --------------------------------------------------------
    # YOUTUBE
    # --------------------------------------------------------

    elif (
        "search youtube" in command
        or "youtube search" in command
    ):

        youtube_search(command)


    elif (
        "play youtube" in command
        or "play a video" in command
    ):

        play_youtube()


    # --------------------------------------------------------
    # SPOTIFY
    # --------------------------------------------------------

    elif command == "open spotify":

        open_spotify()


    elif (
        "play music" in command
        or "play some music" in command
    ):

        play_music()


    # --------------------------------------------------------
    # CHROME
    # --------------------------------------------------------

    elif (
        "open chrome" in command
        or "start chrome" in command
    ):

        open_chrome()


    # --------------------------------------------------------
    # WINDOWS APPLICATIONS
    # --------------------------------------------------------

    elif "open notepad" in command:

        open_notepad()


    elif (
        "open calculator" in command
        or "open calc" in command
    ):

        open_calculator()


    elif (
        "open file explorer" in command
        or "open explorer" in command
    ):

        open_file_explorer()


    elif (
        "open command prompt" in command
        or "open cmd" in command
    ):

        open_command_prompt()


    elif "open powershell" in command:

        open_powershell()


    elif (
        "open vscode" in command
        or "open visual studio code" in command
    ):

        open_vscode()


    elif "open settings" in command:

        open_settings()


    elif "open control panel" in command:

        open_control_panel()


    elif "open task manager" in command:

        open_task_manager()


    # --------------------------------------------------------
    # FOLDERS
    # --------------------------------------------------------

    elif (
        "open downloads" in command
        or "open download folder" in command
    ):

        open_downloads()


    elif (
        "open documents" in command
        or "open document folder" in command
    ):

        open_documents()


    elif "open desktop" in command:

        open_desktop()


    elif (
        "open pictures" in command
        or "open photos" in command
    ):

        open_pictures()


    elif "open videos" in command:

        open_videos()


    elif "open music folder" in command:

        open_music_folder()


    elif (
        "open my folder" in command
        or "open custom folder" in command
    ):

        open_custom_folder()


    # --------------------------------------------------------
    # YOUR APPLICATION
    # --------------------------------------------------------

    elif (
        "open my application" in command
        or "open my app" in command
    ):

        open_my_application()


    # --------------------------------------------------------
    # TIME / DATE
    # --------------------------------------------------------

    elif (
        "what time is it" in command
        or "tell me the time" in command
        or "current time" in command
    ):

        tell_time()


    elif (
        "what is today's date" in command
        or "tell me the date" in command
        or "current date" in command
    ):

        tell_date()


    elif (
        "what day is it" in command
        or "today's day" in command
    ):

        tell_day()


    # --------------------------------------------------------
    # JOKE
    # --------------------------------------------------------

    elif (
        "tell me a joke" in command
        or "tell joke" in command
    ):

        tell_joke()


    # --------------------------------------------------------
    # COMPUTER CONTROL
    # --------------------------------------------------------

    elif (
        "lock computer" in command
        or "lock my computer" in command
    ):

        lock_computer()


    elif (
        "shutdown computer" in command
        or "shut down computer" in command
    ):

        shutdown_computer()


    elif (
        "restart computer" in command
        or "restart my computer" in command
    ):

        restart_computer()


    elif (
        "cancel shutdown" in command
        or "cancel restart" in command
    ):

        cancel_shutdown()


    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    else:

        speak(
            "I don't know that command yet."
        )

    return True


# ============================================================
# SPEECH MODE
# ============================================================

def speech_mode():

    print()
    print("========================================")
    print("          JARVIS - SPEECH MODE")
    print("========================================")
    print()
    print("Speak your commands.")
    print("Say 'quit' to return to the main menu.")
    print()

    speak(
        "Speech mode activated. "
        "I am listening."
    )

    while True:

        command = listen()

        if command == "":
            continue

        result = process_command(
            command
        )

        if result is False:

            break

    return


# ============================================================
# TERMINAL MODE
# ============================================================

def terminal_mode():

    print()
    print("========================================")
    print("         JARVIS - TERMINAL MODE")
    print("========================================")
    print()
    print("Type your commands.")
    print("Type 'back' to return to the main menu.")
    print()

    while True:

        command = input(
            "You: "
        ).lower().strip()

        if command == "back":

            print(
                "\nReturning to main menu..."
            )

            break

        if command == "":
            continue

        result = process_command(
            command
        )

        if result is False:

            return False

    return True


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    while True:

        print()
        print("========================================")
        print("          JARVIS AI ASSISTANT")
        print("========================================")
        print()
        print("1. Speech")
        print("2. Terminal")
        print("3. Quit")
        print()

        choice = input(
            "Enter your choice: "
        ).strip()


        # ----------------------------------------------------
        # SPEECH
        # ----------------------------------------------------

        if choice == "1":

            speech_mode()


        # ----------------------------------------------------
        # TERMINAL
        # ----------------------------------------------------

        elif choice == "2":

            result = terminal_mode()

            if result is False:

                break


        # ----------------------------------------------------
        # QUIT
        # ----------------------------------------------------

        elif choice == "3":

            speak(
                "Goodbye! Have a great day."
            )

            break


        # ----------------------------------------------------
        # INVALID OPTION
        # ----------------------------------------------------

        else:

            print()
            print(
                "Invalid choice."
            )

            print(
                "Please select 1, 2 or 3."
            )


# ============================================================
# START JARVIS
# ============================================================

if __name__ == "__main__":

    main_menu()
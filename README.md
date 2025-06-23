This is a simple voice-based calculator project written in Python. It allows users to perform basic mathematical operations using natural language commands like "add 5 and 6", "what is the product of 3 and 9", or "divide 100 by 4".

✨ Features
✅ Voice command interpretation using NLP
✅ Basic arithmetic operations: add, subtract, multiply, divide
✅ Friendly interaction with fallback support
✅ Easily extendable with more operations
🔧 Requirements
Python 3.7+
speech_recognition
pyttsx3
re (Regular expressions, built-in)
Install dependencies using:

pip install speechrecognition pyttsx3
🚀 How to Use
Clone the repo or download the smartcalculator.py file.
Run the script:
python smartcalculator.py
Speak your command like:
"Add 8 and 5"
"What is 9 times 4"
"Divide 20 by 2"
"Exit" to stop
The calculator will respond with the answer in audio.

📌 How It Works
Takes microphone input using speech_recognition
Uses re (regex) to find numbers and operation keywords
Matches command with pre-defined operation map
Uses pyttsx3 to speak the result
🤖 Future Ideas
Add support for advanced math (power, square root, etc.)
Include GUI interface
Add error handling for invalid speech or inputs

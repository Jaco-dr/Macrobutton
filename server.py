from flask import Flask, request
import pyautogui

app = Flask(__name__)

@app.route('/execute', methods=['GET'])
def execute_command():
    command = request.args.get('command')

    # Verwerk de ontvangen commando's
    if command == 'Ctrl+N':
        pyautogui.hotkey('ctrl', 'n')
    elif command == 'Ctrl+S':
        pyautogui.hotkey('ctrl', 's')
    elif command == 'Ctrl+Z':
        pyautogui.hotkey('ctrl', 'z')
    elif command == 'Ctrl+Y':
        pyautogui.hotkey('ctrl', 'y')

    return "Command Executed", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

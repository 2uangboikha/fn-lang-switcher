import os
from pynput import keyboard

# Fix weird bug LC path needing to be sourced
new_path = "/usr/local/lib"
os.environ["DYLD_LIBRARY_PATH"] = new_path

# Initialize the language list and the current index
lang_list = [
    'com.apple.keylayout.RussianWin', 
    'com.apple.inputmethod.VietnameseIM.VietnameseTelex',
    'com.apple.keylayout.ABC'
]
current_index = 0

def on_press(key):
    global current_index
    
    # Check if the pressed key is the key with code 179
    key_str = '{0}'.format(key)
    if key_str == '<179>':
        # Read the current input source
        stream = os.popen('/usr/local/bin/issw')
        output = stream.read().strip()
        
        # Find the current index in the language list
        if output in lang_list:
            current_index = lang_list.index(output)
        
        # Determine the next index
        next_index = (current_index + 1) % len(lang_list)
        next_lang = lang_list[next_index]
        
        # Switch to the next input source
        os.system(f'/usr/local/bin/issw {next_lang}')
        
        # Update the current index
        current_index = next_index

# Set up and start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=None) as listener:
    listener.join()

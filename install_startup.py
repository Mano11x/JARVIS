import os
import sys

def main():
    # Define paths
    project_dir = os.path.dirname(os.path.abspath(__file__))
    python_exe = os.path.join(project_dir, ".venv", "Scripts", "python.exe")
    if not os.path.exists(python_exe):
        python_exe = os.path.join(project_dir, "venv", "Scripts", "python.exe")
    wakeup_script = os.path.join(project_dir, "wakeup.py")

    # Windows Startup folder path for the current user
    appdata = os.environ.get("APPDATA")
    if not appdata:
        print("Error: Could not locate APPDATA directory.")
        return
        
    startup_dir = os.path.join(appdata, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    vbs_path = os.path.join(startup_dir, "JarvisWakeup.vbs")

    # VBScript content to run Python in hidden mode (no command prompt window)
    vbs_content = f'''Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c \\"{python_exe}\\" \\"{wakeup_script}\\"", 0, False
'''

    try:
        with open(vbs_path, "w") as f:
            f.write(vbs_content)
        print(f"Success! Created startup script at: {vbs_path}")
        print("JARVIS will now automatically run and start listening in the background whenever your computer turns on.")
        
        # Also run it right now so the user doesn't have to restart
        os.startfile(vbs_path)
        print("Successfully started JARVIS in the background! You can speak 'JARVIS WAKEUP' now.")
    except Exception as e:
        print(f"Error installing startup script: {e}")

if __name__ == "__main__":
    main()

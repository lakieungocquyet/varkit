import subprocess

def translate_path(path):
    RESULT = subprocess.run(["wslpath", "-u", path], capture_output=True, text=True, check=True)
    WSL_PATH = RESULT.stdout.strip()
    return WSL_PATH
import platform

def detect_os():
    os_name = platform.system().lower()
    print(f"[DEBUG] platform.system() = {os_name}")
    if os_name == "linux":
        return "linux"
    elif os_name == "windows":
        return "windows"
    else:
        raise RuntimeError(f"Unsupported platform: {os_name}")


import os
import sys
import time
import threading
import webbrowser
import streamlit.web.cli as stcli

def resolve_path(path):
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

def open_browser():
    """Wait a few seconds for server to start, then open browser."""
    time.sleep(4)
    webbrowser.open("http://localhost:8501")

def main():
    # Setup sys.path so the python_master module can be imported properly
    if getattr(sys, "frozen", False):
        src_path = os.path.join(sys._MEIPASS, "src")
        sys.path.insert(0, src_path)
        python_master_path = os.path.join(src_path, "python_master")
        sys.path.insert(0, python_master_path)
        app_path = os.path.join(python_master_path, "app.py")
    else:
        src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
        sys.path.insert(0, src_path)
        app_path = os.path.join(src_path, "python_master", "app.py")

    # Launch browser in a background thread after delay
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()

    # Reconstruct sys.argv to run: streamlit run <path_to_app.py>
    sys.argv = [
        "streamlit", "run", app_path,
        "--server.headless=true",
        "--global.developmentMode=false",
        "--server.port=8501",
    ]

    # Start Streamlit CLI
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()

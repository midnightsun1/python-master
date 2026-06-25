import os
import sys
import streamlit.web.cli as stcli

def main():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(current_dir, "app.py")
    
    # Reconstruct sys.argv to run: streamlit run <path_to_app.py>
    sys.argv = ["streamlit", "run", app_path] + sys.argv[1:]
    
    # Run Streamlit CLI main function
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()

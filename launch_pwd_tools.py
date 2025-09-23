import subprocess
import sys
import os

def main():
    # Change to the PWD-Tools directory
    os.chdir("PWD-Tools")
    
    # Try to run the Streamlit app
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
    except FileNotFoundError:
        print("Streamlit not found. Please install it with: pip install streamlit")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
import os
import sys
import threading
import time
import webbrowser


def open_browser_when_ready(url: str, delay_seconds: float = 1.5) -> None:
    def _worker() -> None:
        time.sleep(delay_seconds)
        try:
            webbrowser.open(url)
        except Exception:
            pass

    threading.Thread(target=_worker, daemon=True).start()


def get_app_dir() -> str:
    # When packaged with PyInstaller (onedir), the data is copied to a subfolder named 'app'
    if getattr(sys, "frozen", False):  # PyInstaller runtime
        exe_dir = os.path.dirname(sys.executable)
        return os.path.join(exe_dir, "app")

    # Running from source: use the repository folder layout
    this_dir = os.path.dirname(os.path.abspath(__file__))
    # This file lives inside PWD-Tools/, which is the app root
    return this_dir


def main() -> int:
    try:
        from streamlit.web import cli as stcli
    except Exception as exc:
        print("Streamlit is required to run this app. Please install dependencies.")
        print(f"Error: {exc}")
        return 1

    app_dir = get_app_dir()
    app_entry = os.path.join(app_dir, "app.py")

    if not os.path.exists(app_entry):
        print(f"App entry file not found: {app_entry}")
        return 2

    os.chdir(app_dir)

    # Provide a minimal, known-good Streamlit config to avoid parsing errors
    safe_config_path = os.path.join(app_dir, "streamlit.safe.toml")
    if not os.path.exists(safe_config_path):
        try:
            with open(safe_config_path, "w", encoding="utf-8") as f:
                f.write(
                    """
[server]
headless = true
address = "127.0.0.1"
port = 8501
enableCORS = false
enableXsrfProtection = false
fileWatcherType = "none"
""".strip()
                )
        except Exception:
            pass

    os.environ["STREAMLIT_CONFIG_FILE"] = safe_config_path

    # Start browser shortly after server starts
    open_browser_when_ready("http://127.0.0.1:8501")

    # Build arguments for Streamlit
    sys.argv = [
        "streamlit",
        "run",
        app_entry,
        "--server.address=127.0.0.1",
        "--server.port=8501",
        "--browser.gatherUsageStats=false",
        "--server.headless=true",
    ]

    try:
        return stcli.main()
    except SystemExit as e:
        # Streamlit may raise SystemExit
        return int(getattr(e, "code", 0) or 0)


if __name__ == "__main__":
    sys.exit(main())



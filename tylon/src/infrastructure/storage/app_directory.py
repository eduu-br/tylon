import os


def ensure_app_directory():
    app_dir: str = os.getenv("LOCALAPPDATA") + "\\.tylon"  # type: ignore
    if not os.path.exists(app_dir):
        os.mkdir(app_dir)

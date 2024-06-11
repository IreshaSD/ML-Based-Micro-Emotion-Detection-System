import tkinter
from ui.windows.app import App
import sys


if __name__ == "__main__":
    csv_path = sys.argv[1]
    base_path = sys.argv[2]
    App(tkinter.Tk(), "Video", csv_path, base_path)

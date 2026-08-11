import webview
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

if __name__ == '__main__':
    window = webview.create_window(
        'Zenith Music', 
        'https://efeprivatemix.vercel.app/',
        width=1280,
        height=720,
        background_color='#121212',
        min_size=(800, 600)
    )
    webview.start()

import webview
import ctypes
import time

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

try:
    from pypresence import Presence
    has_rpc = True
except ImportError:
    has_rpc = False

class Api:
    def __init__(self):
        self.rpc = None
        self.connected = False
        self.start_time = time.time()
        
        if has_rpc:
            try:
                # User's Discord Client ID
                self.rpc = Presence('1536830417682825246')
                self.rpc.connect()
                self.connected = True
                
                # Default presence when app opens
                self.rpc.update(
                    state="Uygulama Açık",
                    details="Ana Sayfada Geziniyor",
                    large_image="zenith_logo",
                    large_text="Zenith Music",
                    start=self.start_time
                )
            except Exception as e:
                print("Discord RPC bağlanılamadı:", e)
                
    def update_rpc(self, title, artist):
        if self.connected and self.rpc:
            try:
                self.rpc.update(
                    state=artist,
                    details=f"Dinliyor: {title}",
                    large_image="zenith_logo",
                    large_text="Zenith Music",
                    start=self.start_time
                )
            except Exception as e:
                print("RPC güncellenemedi:", e)

if __name__ == '__main__':
    api = Api()
    window = webview.create_window(
        'Zenith Music', 
        'https://efeprivatemix.vercel.app/',
        width=1280,
        height=720,
        background_color='#121212',
        min_size=(800, 600),
        js_api=api
    )
    webview.start()

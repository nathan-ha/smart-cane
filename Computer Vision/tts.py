import time
from gtts import gTTS
import os

class TTS:
    
    def __init__(self):
        self.last_announcement = {}
        self.dedup_timeout = 2.0
        self.language = 'en'
    
    def alert_object(self, object_name):
        alert = object_name
        audio = gTTS(text=alert, lang=self.language, slow=False)
        audio.save("tmp.mp3")
        
        # Check duplicates
        current_time = time.time()
        if alert in self.last_announcement:
            if current_time - self.last_announcement[alert] < self.dedup_timeout:
                print(f"[SKIPPED] {alert}")
                return
            
        os.system("tmp.mp3")
        self.last_announcement[alert] = current_time
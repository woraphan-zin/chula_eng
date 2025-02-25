import tkinter as tk
import random

# Thai consonants and their names
THAI_CONSONANTS = {
    "ก": "กอ ไก่",
    "ข": "ขอ ไข่",
    "ค": "คอ ควาย",
    "ง": "งอ งู",
    "จ": "จอ จาน",
    "ฉ": "ฉอ ฉิ่ง",
    "ช": "ชอ ช้าง",
    "ซ": "ซอ โซ่",
    "ญ": "ญอ หญิง",
    "ฎ": "ฎอ ชฎา",
    "ฏ": "ฏอ ปฏัก",
    "ฐ": "ฐอ ฐาน",
    "ฑ": "ฑอ มณโฑ",
    "ณ": "ณอ เณร",
    "ด": "ดอ เด็ก",
    "ต": "ตอ เต่า",
    "ถ": "ถอ ถุง",
    "ท": "ทอ ทหาร",
    "น": "นอ หนู",
    "บ": "บอ ใบไม้",
    "ป": "ปอ ปลา",
    "ผ": "ผอ ผึ้ง",
    "ฝ": "ฝอ ฝา",
    "พ": "พอ พาน",
    "ฟ": "ฟอ ฟัน",
    "ม": "มอ ม้า",
    "ย": "ยอ ยักษ์",
    "ร": "รอ เรือ",
    "ล": "ลอ ลิง",
    "ว": "วอ แหวน",
    "ศ": "ศอ ศาลา",
    "ส": "สอ เสือ",
    "ห": "หอ หีบ"
}

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        
        self.current_card = None
        self.flipped = False
        
        self.card_label = tk.Label(root, text="", font=("Arial", 50), width=5, height=2, relief="ridge", bd=3)
        self.card_label.pack(pady=40)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack(pady=5)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack(pady=5)
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(list(THAI_CONSONANTS.keys()))
        self.flipped = False
        self.update_display()
    
    def flip_card(self):
        self.flipped = not self.flipped
        self.update_display()
    
    def update_display(self):
        if self.flipped:
            self.card_label.config(text=THAI_CONSONANTS[self.current_card], font=("Arial", 24))
        else:
            self.card_label.config(text=self.current_card, font=("Arial", 50))

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()
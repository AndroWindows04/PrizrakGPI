import customtkinter as ctk
import threading
import time
import ctypes
import random
import os
import winsound
import sys

u32 = ctypes.windll.user32
g32 = ctypes.windll.gdi32

def no_exit(): pass

def run_simulation():
    if not v.get(): return
    root.withdraw()
    
    h = u32.GetDC(0)
    sw, sh = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
    t_msg = "HAHA.YOUR BIN TROLL"
    s_t = time.time()
    l_i = s_t
    
    while time.time() - s_t < 105:
        c_t = time.time()
        g32.BitBlt(h, random.randint(-10, 10), random.randint(-10, 10), sw, sh, h, 0, 0, 0x440032)
        
        if c_t - l_i > 10:
            g32.BitBlt(h, 0, 0, sw, sh, h, 0, 0, 0x5A0049)
            l_i = c_t
            
        g32.SetTextColor(h, random.randint(0, 0xFFFFFF))
        g32.SetBkMode(h, 1)
        g32.TextOutW(h, random.randint(0, sw), random.randint(0, sh), t_msg, len(t_msg))
        u32.DrawIcon(h, random.randint(0, sw), random.randint(0, sh), u32.LoadIconW(0, 32513))
        u32.SetCursorPos(random.randint(0, sw), random.randint(0, sh))
        
        if random.random() > 0.8:
            winsound.Beep(random.randint(400, 1200), 70)
            g32.StretchBlt(h, 20, 20, sw-40, sh-40, h, 0, 0, sw, sh, 0xCC0020)
        time.sleep(0.04)
    
    u32.InvalidateRect(0, None, True)
    os._exit(0)

def set_ru():
    lbl.configure(text="БЕЗОПАСНАЯ СИМУЛЯЦИЯ\n\nПрограмма покажет визуальные эффекты,\nно не нанесет вреда системе.")
    chk.configure(text="Я подтверждаю просмотр")
    btn_y.configure(text="Запуск")
    btn_n.configure(text="Выход")

def set_en():
    lbl.configure(text="SAFE SIMULATION\n\nThe program will show visual effects\nwithout harming your system.")
    chk.configure(text="I confirm the simulation")
    btn_y.configure(text="Run")
    btn_n.configure(text="Exit")

root = ctk.CTk()
root.overrideredirect(True)
ww, wh = 450, 300
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{ww}x{wh}+{int(sw/2-ww/2)}+{int(sh/2-wh/2)}")
root.attributes("-topmost", True)

v = ctk.BooleanVar()
lbl = ctk.CTkLabel(root, text="", font=("Arial", 14, "bold"))
lbl.pack(pady=30)
chk = ctk.CTkCheckBox(root, text="", variable=v)
chk.pack()

f_btns = ctk.CTkFrame(root, fg_color="transparent")
f_btns.pack(pady=20)
btn_y = ctk.CTkButton(f_btns, text="", fg_color="#2ecc71", hover_color="#27ae60", width=120, command=lambda: threading.Thread(target=run_simulation).start())
btn_y.pack(side="left", padx=10)
btn_n = ctk.CTkButton(f_btns, text="", width=120, command=root.destroy)
btn_n.pack(side="left", padx=10)

f_lang = ctk.CTkFrame(root, fg_color="transparent")
f_lang.pack(side="bottom", pady=10)
ctk.CTkButton(f_lang, text="RU", width=40, command=set_ru).pack(side="left", padx=5)
ctk.CTkButton(f_lang, text="EN", width=40, command=set_en).pack(side="left", padx=5)

set_ru()
root.mainloop()



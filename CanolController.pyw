# Under LICENSE: Radioxians SA LICENSE (Source Available, for more info, view the file LICENSE)

import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import datetime

# --- LOGICA ---
def azione(tipo, valore=None):
    if tipo == "web":
        webbrowser.open(valore)
    elif tipo == "cmd":
        os.system(valore)
    elif tipo == "ora":
        messagebox.showinfo("AI Time", f"Capo, sono le: {datetime.datetime.now().strftime('%H:%M:%S')}")

def cerca_google(event=None): # Funziona anche premendo INVIO sulla tastiera
    query = entry.get()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")

# --- FINESTRA ---
root = tk.Tk()
root.title("CanolController")
root.geometry("450x650")
root.configure(bg="#1a1a1a") # Sfondo dark

# Titolo App
tk.Label(root, text="💻 CanolController 1.0", font=("Arial Black", 20), fg="#00ff00", bg="#1a1a1a").pack(pady=10)

# Barra di ricerca
frame_search = tk.Frame(root, bg="#1a1a1a")
frame_search.pack(pady=10)

entry = tk.Entry(frame_search, font=("Arial", 12), width=25, bg="#333", fg="white", borderwidth=0)
entry.pack(side="left", padx=5)
entry.bind("<Return>", cerca_google) # Se premi invio cerca subito

btn_cerca = tk.Button(frame_search, text="SEARCH ON GOOGLE", command=cerca_google, bg="#00ff00", font=("Arial", 9, "bold"))
btn_cerca.pack(side="left")

# --- GRIGLIA BOTTONI ---
grid_frame = tk.Frame(root, bg="#1a1a1a")
grid_frame.pack(pady=10)

def btn(testo, colore, r, c, cmd):
    b = tk.Button(grid_frame, text=testo, bg=colore, fg="white", width=18, height=2, 
                  font=("Arial", 9, "bold"), borderwidth=0, cursor="hand2", command=cmd)
    b.grid(row=r, column=c, padx=5, pady=5)

# --- MAPPA DEI BOTTONI (14 FUNZIONI) ---
# Fila 1
btn("📺 YOUTUBE", "#FF0000", 0, 0, lambda: azione("web", "https://youtube.com"))
btn("🎮 ROBLOX", "#444444", 0, 1, lambda: azione("web", "https://roblox.com"))
# Fila 2
btn("🤖 GEMINI AI", "#4285F4", 1, 0, lambda: azione("web", "https://gemini.google.com"))
btn("💬 DISCORD", "#5865F2", 1, 1, lambda: azione("web", "https://discord.com"))
# Fila 3
btn("📝 WIKIPEDIA", "#000000", 2, 0, lambda: azione("web", "https://it.wikipedia.org"))
btn("🌐 TRADUTTORE", "#4285F4", 2, 1, lambda: azione("web", "https://translate.google.it"))
# Fila 4
btn("🎵 SPOTIFY", "#1DB954", 3, 0, lambda: azione("web", "https://open.spotify.com"))
btn("💜 TWITCH", "#9146FF", 3, 1, lambda: azione("web", "https://twitch.tv"))
# Fila 5
btn("🧮 CALCOLATRICE", "#f39c12", 4, 0, lambda: azione("cmd", "calc"))
btn("⏰ ORA ESATTA", "#9b59b6", 4, 1, lambda: azione("ora"))
# Fila 6
btn("📊 TASK MANAGER", "#34495e", 5, 0, lambda: azione("cmd", "taskmgr"))
btn("☁️ METEO", "#3498db", 5, 1, lambda: azione("web", "https://www.ilmeteo.it"))
# Fila 7
btn("📧 GMAIL", "#d44638", 6, 0, lambda: azione("web", "https://mail.google.com"))
btn("🛒 AMAZON", "#ff9900", 6, 1, lambda: azione("web", "https://amazon.it"))
# Fila 7
btn(" CANVA", "#ff5970", 7, 0, lambda: azione("web", "https://www.canva.com/"))
btn(" OUTLOOK", "#ff6902", 7, 1, lambda: azione("web", "https://outlook.live.com/"))


# Tasto speciale Hacker in fondo
tk.Button(root, text="☣️ HACKER MODE (FAKE,NOT OPEN IMMEDI.) ☣️", bg="#003300", fg="#00ff00", width=40, height=2,
          font=("Courier", 10, "bold"), command=lambda: azione("cmd", "start cmd /k color 0a")).pack(pady=20)

root.mainloop()

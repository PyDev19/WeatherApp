import tkinter as tk
import App
import GetWeather

# Get weather button
button = tk.Button(App.frame, text="Get Weather", font=('Courier', 14), command=lambda: GetWeather.get_weather(App.entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# Main Loop
App.root.mainloop()

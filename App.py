import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.resizable(False, False)
root.title('Weather App')

icon = tk.PhotoImage(file='weather-app.png')

root.iconphoto(False, icon)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 15), justify='left')
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, justify='left', anchor='w', font=('Courier', 15))
label.place(relwidth=1, relheight=1)

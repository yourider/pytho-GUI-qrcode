from tkinter import*
from PIL import ImageTk, Image
window = Tk(className="ev qrcode")
window.title('ev chat')
window.geometry("600x400")
img =Image.open('ev.jpg')
bg = ImageTk.PhotoImage(img)
window.attributes('-alpha', 0.5)
la = Label(window, image=bg)
la.place(x=0,y=0)
window.config(bg="#221222")

h = Label(window, text="Enter the data you want to give in your qrcode", font="Times 20 italic bold", bg="#221222", fg="red")
k = Entry(window,bg="#221222")
h7 = Label(window, text="Enter the name to your qrcode add .jpg also", font="Times 20 italic bold", bg="#221222", fg="red")
k6 = Entry(window,bg="#221222")
def p():
    import qrcode
    # generating a QR code using the make() function
    h4 = k.get()
    kg = k6.get()
    import os

    print('your QRcode is stored in ')
    os.system('pwd')
    qr_img = qrcode.make(h4)
    # saving the image file
    qr_img.save(kg)
    import notification
    notification.notify("your QR code is generated")
    h9 = Label(window, text="check the location were you saved the app",bg="#221222",fg="red")
    h9.pack()


b = Button(window, text="click me", command=p, borderwidth=9)


h.pack()
k.pack()
h7.pack()
k6.pack()
b.pack()


window.mainloop()

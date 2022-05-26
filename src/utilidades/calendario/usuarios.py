from tkinter import *
import cv2 #de libreria opencv-python
#Tipo  estructura usuario
class login():

    def __init__(self):
        self.msg = ""
        self.cont = 0
        self.window()
        self.titulos()
        self.entrada_datos()
        self.botones()
        self.ventana.mainloop()
        self.creacion_icono()


    def window(self):
        self.ventana= Tk()
        self.ventana.configure(bg="silver")
        self.ventana.title("Identificacion")
        self.ventana.resizable(False,False)

        self.ventana.geometry("560x330")


    def titulos(self):
        t1=Label(self.ventana,fg="black",font=("Arial",18),bg="silver",text="Nombre").place(x=230,y=30)
        t2=Label(self.ventana,bg="silver",fg="black",font=("Arial",18),text="Apellido").place(x=230,y=120)
        self.t3 = Label(self.ventana,fg="black",font=("Arial",14),bg="silver",text =self.msg)
        self.t3.place(x=200,y=220)

    def entrada_datos(self):
        self.username=StringVar()
        self.last_name=StringVar()
        self.nombre = Entry(self.ventana,font=("Arial",18),fg="blue",textvariable=self.username).place(x=150, y=80)

        self.apellido = Entry(self.ventana, font=("Arial", 18), fg="blue",textvariable=self.last_name)
        self.apellido.place(x=150, y=180)


    def botones(self):

        self.aceptar = Button(self.ventana, relief="raised", text="Aceptar", bg="blue", fg="white", font=("Arial", 13),
                              cursor="hand2", command=self.ventana.destroy).place(x=150, y=260, width=110, height=30)
        self.cancelar = Button(self.ventana, relief="raised", text="Cancelar", bg="blue", fg="white",
                               font=("Arial", 13),
                               cursor="hand2", command=self.ventana.destroy).place(x=310, y=260, width=110, height=30)

    def creacion_icono(self):
        self.username_data = self.username.get()

        self.last_name_data = self.last_name.get()

        img = cv2.imread('imagen.jpg')
        img_resized = cv2.resize(img, (120, 120))
        if(self.username_data!="" and self.last_name_data!=""):
            texto = self.username_data[:1] + "." + self.last_name_data[:1]
            posicion = (30, 80)
            font = cv2.FONT_HERSHEY_DUPLEX
            tamanoletra = 1
            colorletra = (241, 78, 214)
            grosorletra = 4
            extension = self.last_name_data + ".jpg"
            cv2.putText(img_resized, texto, posicion, font, tamanoletra, colorletra, grosorletra)
            cv2.imwrite(extension, img_resized)

a=login()

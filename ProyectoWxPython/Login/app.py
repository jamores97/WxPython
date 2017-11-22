# -*- coding:utf8 -*-
import wx


# Clase donde irán todos los elementos widgets del registro
class LoginDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Registrate Luismi!", size=(400, 450)) # Creamos el dialogo de titulo de la ventana

        # Creamos las fuentes que utilizaremos posteriormente en el formulario
        tituloFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Arial')
        usuarioFont = wx.Font(8, wx.SWISS, wx.NORMAL, wx.LIGHT, False, 'Arial')

        titulo_login = wx.StaticText(self, label="SIGNUP CAMPAIGNAPP", pos=(110, 20)) #Título del Login
        titulo_login.SetFont(tituloFont) #Insertamos su fuente correspondiente

        email = wx.StaticText(self, label="Email", pos=(95, 58)) # Label email del input
        email.SetFont(usuarioFont) # Insertamos su fuente correspondiente

        self.email = wx.TextCtrl(self, pos=(95, 76), size=(200, 26)) # Input email
        self.email.SetFont(usuarioFont) # Insertamos su fuente correspondiente

        usuario = wx.StaticText(self, label="Nombre usuario", pos=(95, 122))  # Label nombre de usuario del input
        usuario.SetFont(usuarioFont)  # Insertamos su fuente correspondiente

        self.user = wx.TextCtrl(self, pos=(95, 140), size=(200, 26))  # Input email
        self.user.SetFont(usuarioFont)  # Insertamos su fuente correspondiente

        password = wx.StaticText(self, label="Contraseña:", pos=(95, 186)) # Label password del input
        password.SetFont(usuarioFont) #Insertamos su fuente correspondiente

        self.password = wx.TextCtrl(self, pos=(95, 204), size=(200, 26), style=wx.TE_PASSWORD) # Input password

        password2 = wx.StaticText(self, label="Repetir contraseña:", pos=(95, 250))  # Label password del input
        password2.SetFont(usuarioFont)  # Insertamos su fuente correspondiente

        self.password2 = wx.TextCtrl(self, pos=(95, 268), size=(200, 26),  style=wx.TE_PASSWORD)  # Input password 2
        # self.password.Bind(wx.EVT_TEXT_ENTER, self.Loguearse)

        # Iniciar sesión
        registrar = wx.Button(self, label="Regístrate", pos=(120, 320), size=(150, 65)) # Creamos el botón de registro
        registrar.SetFont(usuarioFont) # Insertamos su fuente correspondiente
        registrar.Bind(wx.EVT_BUTTON, self.registrarse) # Método que se realizara una vez se pulse el botón

    # Método para comprobar el registro
    def registrarse(self, event):

        # Extraemos los valores que ha introducido el usuario
        user = self.user.GetValue()
        password = self.password.GetValue()
        password2 = self.password2.GetValue()
        email = self.password.GetValue()

        # Comprobamos que los datos son correctos, que haya escrito algo en cada campo y que ambas contraseñas sean iguales
        if user == "" or password == "" or password2 == "" or email == "":
            print "Faltan datos por introducir"
        elif  password != password2:
            print "Las contraseñas no coinciden"
        else:
            print "Registo completado!"



# Creamos la clase frame que será la ventana sobre donde se construirá nuestro formulario
class MainFrame(wx.Frame):
    def __init__(self):

        dlg = LoginDialog()
        dlg.ShowModal()


# Esta condición sirve para comprobar si este módulo ha sido importado por otra clase o no
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
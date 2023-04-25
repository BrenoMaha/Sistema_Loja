from customtkinter import *
from models.cadastro import abrir_tela_cadastro



class LoginWindow:
    def __init__(self):
        self.janela = CTk()
        self.janela.resizable(False, False)
        self.janela.title('Login')
        self.janela.geometry('430x270+700+350')

        self.login_frame = CTkFrame(master=self.janela,width=600)
        self.login_frame.place(x=0,y=0)
        self.login_frame.place_configure(width=430,height=270)

        self.painel = CTkLabel(
        master = self.login_frame,
        text='Tela de Login',
        font=('sitka banner', 20))
        self.painel.grid(
        row=1,
        columnspan=2,
        padx=(10, 0),
        pady=(10, 0))

        CTkLabel(
        self.login_frame, 
        text='Login:').grid(
        row=2, 
        column=0, 
        padx=(10, 5), 
        pady=(10, 0))

        self.entrada_login = CTkEntry(self.login_frame)

        self.entrada_login.grid(
        row=2, 
        column=1, 
        padx=(0, 10), 
        pady=(10, 0))

        CTkLabel(
        self.login_frame, 
        text='Senha:').grid(
        row=3,
        column=0, 
        padx=(10, 5), 
        pady=(10, 0))

        self.senha_var = StringVar()

        self.entrada_senha = CTkEntry(
        self.login_frame,
        show='*', 
        textvariable=self.senha_var)
        self.entrada_senha.grid(
        row=3, 
        column=1, 
        padx=(0, 10), 
        pady=(10, 0))

        self.botao_mostrar_senha = IntVar(value=0)

        CTkCheckBox(
        self.login_frame, 
        text='Mostrar senha', 
        variable=self.botao_mostrar_senha, 
        onvalue=1,
        offvalue=0, 
        command=self.mostrar_ou_ocultar_senha).grid(
        row=4,
        column=1, 
        pady=(10, 0))

        CTkButton(
        self.login_frame, 
        text='Login').grid(
        row=5, 
        columnspan=2, 
        padx=10, 
        pady=(20, 10), 
        sticky='we')

        CTkLabel(
        self.login_frame, 
        text='Não possui cadastro ainda?').grid(
        row=6, 
        column=0, 
        padx=10, 
        pady=(20, 10))
        self.botao_cadastro = CTkButton(
        self.login_frame, 
        text='Cadastre-se', 
        command=lambda:abrir_tela_cadastro(self)).grid(
        row=6,
        column=1, 
        padx=10, 
        pady=(20, 10))

        self.janela.mainloop()

    def mostrar_ou_ocultar_senha(self):
        if self.botao_mostrar_senha.get() == 1:
            self.senha_var.set(self.entrada_senha.get())
            self.entrada_senha.configure(show='')
        else:
            self.entrada_senha.delete(0, 'end')
            self.entrada_senha.insert(0, self.senha_var.get())
            self.entrada_senha.configure(show='*')

    
        




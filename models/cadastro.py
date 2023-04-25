from customtkinter import *
from database.cliente_repository import cadastrar_funcionario
from tkinter import messagebox




def abrir_tela_cadastro(login_window):
    login_window.login_frame.pack_forget()
    cadastro = CTkFrame(login_window.janela, width=300, height=300)
    cadastro.place(x=0, y=10)
    cadastro.place_configure(width=430,height=270)
    def mostrar_ou_ocultar_senha():
        if mostrar_senha.get() == 1:
            senha_var.set(entrada_senha.get())
            entrada_senha.configure(show='')
        else:
            entrada_senha.delete(0, 'end')
            entrada_senha.insert(0, senha_var.get())
            entrada_senha.configure(show='*')

    painel = CTkLabel(
        cadastro, text='Tela de Cadastro', font=('sitka banner', 20))
    painel.grid(row=1, columnspan=3, padx=(
        10, 10), pady=(10, 10), sticky='WE')

    CTkLabel(cadastro, text='Usuario: ').grid(
        row=2, column=0, padx=(10, 10), pady=(10, 10)
    )
    email_login = CTkEntry(cadastro)
    email_login.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

    CTkLabel(cadastro, text='Senha:').grid(
        row=3, column=0, padx=(10, 10), pady=(10, 10)
    )
    senha_var = StringVar()
    entrada_senha = CTkEntry(
        cadastro, show='*', textvariable=senha_var)
    entrada_senha.grid(
        row=3, column=1, padx=(10, 10), pady=(10, 10)
    )

    mostrar_senha = IntVar(value=0)

    CTkCheckBox(cadastro, text='Mostrar senha', variable=mostrar_senha, onvalue=1,
                offvalue=0, command=mostrar_ou_ocultar_senha).grid(row=3, column=2, padx=(10, 10), pady=(10, 10))
    
    CTkButton(
        master=cadastro,
        text='Confirmar cadastro',
        command=lambda: cadastrar_funcionario(email_login.get(),senha_var.get())
    ).grid(row=5,columnspan=4)


    def confirmacao_cadastro():
        pass
    

    

    
    


    
        
        


    



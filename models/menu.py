
from customtkinter import * 

class menu:
    def __init__(self) -> None:
        self.menu = CTk()
        self.menu.resizable(False,False)
        self.menu.title('Menu')
        self.menu.geometry('500x280+700+350')

        self.frame_cima = CTkFrame(master=self.menu,
            width=480)
        self.frame_cima.place(x=0,y=0)

        self.painel = CTkLabel(
            master= self.frame_cima,
            text='Menu de opções',
            font=('comic sans', 20),
            width=480)
        self.painel.grid(
            row=0,
            columnspan=2,
            padx=(10,10),
            pady=(10,10)
        )
        self.frame_menu = CTkScrollableFrame(
            master=self.menu,
            width=480)
        self.frame_menu.place(x=0,y=50)

        self.primeira_opcao = CTkButton(
            master=self.frame_menu,
            text='Listar todos os clientes',
            font=('comic sans',17),
            width=479
        )
        self.primeira_opcao.grid(
            row=0,column=0,sticky='we',pady=(0,1)
        )
        self.segunda_opcao = CTkButton(
            master=self.frame_menu,
            text='Detalhes de um cliente',
            font=('comic sans',17),
            width=475
        ).grid(
            row=1,column=0,sticky='we',pady=(0,1)
        )
        self.terceira_opcao = CTkButton(
            master=self.frame_menu,
            text='Cadastrar um cliente',
            font=('comic sans',17),
            width=475
        ).grid(
            row=2,column=0,sticky='we',pady=(0,1)
        )
        self.quarta_opcao = CTkButton(
            master=self.frame_menu,
            text='Alterar dados de cliente',
            font=('comic sans',17),
            width=475
        ).grid(
            row=3,column=0,sticky='we',pady=(0,1)
        )
        self.quinta_opcao = CTkButton(
            master=self.frame_menu,
            text='Excluir um cliente',
            font=('comic sans',17),
            width=475
        ).grid(
            row=4,column=0,sticky='we',pady=(0,1)
        )
        self.sexta_opcao = CTkButton(
            master=self.frame_menu,
            text='Cadastrar Produto',
            font=('comic sans',17),
            width=475
        ).grid(
            row=4,column=0,sticky='we',pady=(0,1)
        )
        self.setima_opcao = CTkButton(
            master=self.frame_menu,
            text='Cadastrar venda',font=('comic sans',17),
            width=475
        ).grid(
            row=5,column=0,sticky='we',pady=(0,1)
        )
        self.oitava_opcao = CTkButton(
            master=self.frame_menu,
            text='Consultar estoque',
            font=('comic sans',17),
            width=475
        ).grid(
            row=6,column=0,sticky='we',pady=(0,1)
        )


        


        self.menu.mainloop()




menu=menu()
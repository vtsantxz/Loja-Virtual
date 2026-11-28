import tkinter as tk

lista_produtos = [{
    "nome" : "Notebook" ,
    "preco": 3500.00 , 
    "quantidade" : 10

},
{
    "nome" : "Mouse" , 
    "preco" : 80.00 ,
    "quantidade" : 25

},
{
    "nome" : "Teclado" ,
    "preco" : 150.00 ,
    "quantidade" : 21
}]

janela = tk.Tk()

janela.title("LOJA VIRTUAL")
janela.geometry("900x600")
janela.resizable(False, False)

cabecalho = tk.Frame(janela, bg="#1E293B", height=80)
cabecalho.pack(fill="x")

titulo = tk.Label(cabecalho, text="LOJA VIRTUAL", font=("Arial", 22 , "bold"), bg="#1E293B", fg="white")
titulo.pack(pady="20")

conteudo = tk.Frame(janela)
conteudo.pack(fill="both", expand=True)

menu = tk.Frame(conteudo, bg="#334155", width="200")
menu.pack(side="left", fill="y")
menu.pack_propagate(False)

produtos = tk.Frame(conteudo, bg="#F1F5F9")
produtos.pack(side="right" , fill="both", expand=True)

titulo_produtos = tk.Label(produtos, text="Nossos produtos:", font=("Arial", 22 , "bold"))
titulo_produtos.pack(pady=20)

for produto in lista_produtos:

    card = tk.Frame(produtos, bg="white", padx="15", pady="10")
    card.pack(fill="x" , padx="20", pady="8")

    nome = tk.Label(card, text=produto["nome"], font=("Arial", 14 , "bold"), bg="white")
    nome.pack(anchor="w")

    preco = tk.Label(card, text=f"Preço: R$ {produto["preco"]:.2f}", font=("Arial", 11), bg="white")
    preco.pack(anchor="w")

    quantidade = tk.Label(card, text=f"Disponível: {produto["quantidade"]} unidades.", font=("Arial", 10) )
    quantidade.pack(anchor="w")


inicio = tk.Button(menu, text="Início")
inicio.pack(fill="x", padx="10", pady="5")

botao_produtos = tk.Button(menu, text="Produtos")
botao_produtos.pack(fill="x", padx="10", pady="5")


botao_carrinho = tk.Button(menu, text="Carrinho")
botao_carrinho.pack(fill="x", padx="10", pady="5")




janela.mainloop()


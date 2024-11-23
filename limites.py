import sympy as sp
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu

def ajustar_sintaxe(funcao):
    """
    Ajusta a sintaxe da entrada para o SymPy.
    - Substitui 'abs' por 'sp.Abs'.
    - Adiciona multiplicação implícita onde necessário.
    """
    funcao = funcao.replace("abs", "sp.Abs")  # Substitui abs por sp.Abs
    funcao = funcao.replace(")(", ")*(")  # Ex.: (x+3)(x+2) -> (x+3)*(x+2)
    return funcao

def calcular_limite():
    # Obtendo a função do usuário
    funcao = funcao_entry.get()
    ponto = ponto_entry.get()
    tendencia = tendencia_var.get()

    # Definindo a variável simbólica
    x = sp.symbols('x')

    # Ajustando a sintaxe da função
    funcao = ajustar_sintaxe(funcao)

    # Convertendo a string da função para uma expressão simbólica
    try:
        funcao_simb = sp.sympify(funcao)
    except (sp.SympifyError, SyntaxError) as e:
        resultado_label.config(text=f"Erro na função: {e}")
        return

    # Calculando o limite com a tendência especificada
    try:
        if tendencia == 'Direita':
            limite = sp.limit(funcao_simb, x, float(ponto), dir='+')
        elif tendencia == 'Esquerda':
            limite = sp.limit(funcao_simb, x, float(ponto), dir='-')
        else:
            limite = sp.limit(funcao_simb, x, float(ponto))

        # Exibindo o resultado
        resultado_label.config(text=f"Limite de {funcao} quando x tende a {ponto} ({tendencia}): {limite.evalf()}")

    except Exception as e:
        resultado_label.config(text=f"Erro ao calcular o limite: {e}")

# Configurando a interface gráfica
root = Tk()
root.title("Calculadora de Limites")

# Labels e entradas para a função e o ponto
Label(root, text="Função:").grid(row=0, column=0)
funcao_entry = Entry(root)
funcao_entry.grid(row=0, column=1)

Label(root, text="Ponto (x ->):").grid(row=1, column=0)
ponto_entry = Entry(root)
ponto_entry.grid(row=1, column=1)

# Opções de tendência (direita, esquerda, ou ambos)
tendencia_var = StringVar(root)
tendencia_var.set("Ambos")  # Valor padrão

tendencia_menu = OptionMenu(root, tendencia_var, "Direita", "Esquerda", "Ambos")
tendencia_menu.grid(row=2, column=1)

Label(root, text="Tendência:").grid(row=2, column=0)

# Botão para calcular o limite
calcular_button = Button(root, text="Calcular Limite", command=calcular_limite)
calcular_button.grid(row=3, column=1)

# Label para exibir o resultado
resultado_label = Label(root, text="")
resultado_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

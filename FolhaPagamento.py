import tkinter as tk
from tkinter import messagebox


def calculo_INSS(salario):
    if salario <= 1399.12:
        return salario * 0.08
    elif salario <= 2331.88:
        return salario * 0.09
    elif salario <= 4663.75:
        return salario * 0.11
    else:
        return 513.01


def calculo_IRRF(salario, dependentes):
    base_calculo = salario - calculo_INSS(salario) - (dependentes * 189.59)
    if base_calculo <= 1903.98:
        return 0
    elif base_calculo <= 2826.65:
        return (base_calculo * 0.075) - 142.80
    elif base_calculo <= 3751.05:
        return (base_calculo * 0.15) - 354.80
    elif base_calculo <= 4664.68:
        return (base_calculo * 0.225) - 636.13
    else:
        return (base_calculo * 0.275) - 869.36


def vale_transporte(salario):
    desconto_vt = salario * 0.06
    return desconto_vt if desconto_vt < 308 else 0


def vale_refeicao(salario):
    if salario <= 2047.30:
        return 22 * 2.4
    elif salario <= 4094.55:
        return 22 * 3.46
    elif salario <= 9819.15:
        return 22 * 5.56
    else:
        return 22 * 7.14


def vale_alimentacao(salario):
    if salario <= 2047.30:
        return 10.23
    elif salario <= 4094.55:
        return 20.47
    elif salario <= 9819.15:
        return 29.46
    else:
        return 45.54


def seguro_vida(salario):
    return salario * (0.55 / 100)


def assistencia_medica(salario, plano):
    planos = {
        "Básico": [32, 35, 37, 40],
        "Bronze": [37, 40, 43, 46],
        "Prata": [55, 60, 65, 70],
        "Ouro": [70, 76, 83, 91],
    }
    if salario <= 2200:
        return planos[plano][0]
    elif salario <= 3600:
        return planos[plano][1]
    elif salario <= 5900:
        return planos[plano][2]
    else:
        return planos[plano][3]


def calculo_liquido():
    try:
        qnt_dependentes = int(dependentes.get())
        salario_base = float(salario.get())
        plano_saude = assist_medica.get()
        nome_funcionario = nome.get()

        desconto_inss = calculo_INSS(salario_base)
        desconto_irrf = calculo_IRRF(salario_base, qnt_dependentes)
        desconto_vt = vale_transporte(salario_base)
        desconto_vr = vale_refeicao(salario_base)
        desconto_va = vale_alimentacao(salario_base)
        desconto_sv = seguro_vida(salario_base)
        desconto_am = assistencia_medica(salario_base, plano_saude)

        salario_liquido = (
            salario_base
            - desconto_inss
            - desconto_irrf
            - desconto_vt
            - desconto_vr
            - desconto_va
            - desconto_sv
            - desconto_am
        )

        for widget in janela.winfo_children():
            widget.destroy()

        resultado = tk.Label(
            janela,
            text=f"Sobre funcionário {nome_funcionario}:\n\n\n"
                 f"Salário Líquido: R$ {salario_liquido:.2f}\n"
                 f"Desconto INSS: R$ {desconto_inss:.2f}\n"
                 f"Desconto IRRF: R$ {desconto_irrf:.2f}\n"
                 f"Vale Transporte: R$ {desconto_vt:.2f}\n"
                 f"Vale Refeição: R$ {desconto_vr:.2f}\n"
                 f"Vale Alimentação: R$ {desconto_va:.2f}\n"
                 f"Seguro de Vida: R$ {desconto_sv:.2f}\n"
                 f"Assistência Médica ({plano_saude}): R$ {desconto_am:.2f}",
            font=("Arial", 14),
            justify="left",
        )
        resultado.pack(pady=20)
        
        voltar = tk.Button(janela, text="Novo Cálculo", command=widgets_primarios)
        voltar.pack(pady=10)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


def widgets_primarios():
    for widget in janela.winfo_children():
        widget.destroy()

    tk.Label(janela, text="Folha de Pagamento", font=("Arial", 16)).pack(pady=10)

    tk.Label(janela, text="Digite o nome do funcionário").pack()
    global nome
    nome = tk.Entry(janela)
    nome.pack(pady = 5)

    tk.Label(janela, text="Salário Bruto").pack()
    global salario
    salario = tk.Entry(janela)
    salario.pack(pady=5)

    tk.Label(janela, text="Número de Dependentes").pack()
    global dependentes
    dependentes = tk.Entry(janela)
    dependentes.pack(pady=5)

    tk.Label(janela, text="Plano de Saúde (Básico, Bronze, Prata, Ouro)").pack()
    global assist_medica
    assist_medica = tk.Entry(janela)
    assist_medica.pack(pady=5)

    tk.Button(janela, text="Calcular", command=calculo_liquido).pack(pady=10)
    tk.Button(janela, text="Sair", command=janela.quit).pack(pady=10)
    
janela = tk.Tk()
janela.title("Folha de Pagamento")
janela.geometry("400x500")

widgets_primarios()

janela.mainloop()

import random
import customtkinter as ctk


#Gera primeiros digitos aleatorios
def gerar_digitos_aleatorios():
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0 , 9))
    return cpf


#Gera os dois ultimos digitos
def gera_digitos(cpf,num):
    soma = sum(int(digito) * (num - i) for i, digito in enumerate(cpf))
    digito_gerado = (soma * 10) % 11
    digito_gerado = digito_gerado if digito_gerado <= 9 else 0
    return str(digito_gerado)

def gerar_cpf():
    nove_digitos = gerar_digitos_aleatorios()
    dez_digitos = nove_digitos + gera_digitos(nove_digitos, 10)
    cpf_gerado = dez_digitos + gera_digitos(dez_digitos, 11)
    return cpf_gerado

def validar_cpf():
    #Variavel 'retorno' para armazernar a mensagem que sera apresentada na Leabel
    retorno = ''
    cpf = resultado_entry.get()
    # Verificar se o CPF tem 11 dígitos
    if len(cpf)!= 11:
        retorno = 'CPF deve ter 11 dígitos\n'
        return resultado_label.configure(text=retorno)

    # Verificar se o CPF tem apenas dígitos
    if not cpf.isdigit():
        retorno = 'CPF deve conter apenas dígitos\n'
        return resultado_label.configure(text=retorno)

    # Calcular o primeiro dígito verificador
    soma = sum(int(digito) * (10 - i) for i, digito in enumerate(cpf[:-2]))
    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Calcular o segundo dígito verificador
    soma = sum(int(digito) * (11 - i) for i, digito in enumerate(cpf[:-1]))
    digito_2 = (soma * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    #Retorno Boolean a verificação
    if  cpf[-2:] == str(digito_1) + str(digito_2):
        retorno = 'O CPF é válido.\n'

    else:
        retorno = 'O CPF é inválido.\n'

    resultado_label.configure(text=retorno)
        

    # Verificar se os dígitos verificadores estão corretos
    return cpf[-2:] == str(digito_1) + str(digito_2)

def gerar_cpf_callback():
    resultado_entry.delete(0,ctk.END)
    cpf_gerado = gerar_cpf()
    resultado_entry.insert(0, cpf_gerado)

janela = ctk.CTk()
janela.title("Gerador de CPF")
janela.geometry('400X300')

gerar_cpf_button = ctk.CTkButton(master=janela, text="Gerar CPF", command=gerar_cpf_callback)
gerar_cpf_button.pack(ipadx=10, ipady=10, padx=15, pady=15)

resultado_entry = ctk.CTkEntry(janela, placeholder_text='CPF', width=180)
resultado_entry.pack(anchor="center",padx=15, pady=15)

resultado_label = ctk.CTkLabel(janela, text='')
resultado_label.pack()

validar_cpf_button = ctk.CTkButton(master=janela, text="Validar CPF", command=validar_cpf)
validar_cpf_button.pack(ipadx=10, ipady=10, padx=15, pady=15)

janela.mainloop()

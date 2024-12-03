import pyautogui
import time
import threading
import tkinter as tk

# Flag para controlar se o programa está executando
executando = False

# Função para digitar o texto com acentos
def digitar_com_acento(texto):
    global executando
    for caractere in texto:
        if not executando:
            break  # Se a execução for interrompida, sair da função

        if caractere == 'á':
            pyautogui.press('´')
            pyautogui.press('a')
        elif caractere == 'à':
            pyautogui.press('`')
            pyautogui.press('a')
        elif caractere == 'é':
            pyautogui.press('´')
            pyautogui.press('e')
        elif caractere == 'í':
            pyautogui.press('´')
            pyautogui.press('i')
        elif caractere == 'ó':
            pyautogui.press('´')
            pyautogui.press('o')
        elif caractere == 'ú':
            pyautogui.press('´')
            pyautogui.press('u')
        elif caractere == 'ã':
            pyautogui.press('~')
            pyautogui.press('a')
        elif caractere == 'õ':
            pyautogui.press('~')
            pyautogui.press('o')
        elif caractere == 'â':
            pyautogui.press('^')
            pyautogui.press('a')
        elif caractere == 'ê':
            pyautogui.press('^')
            pyautogui.press('e')
        elif caractere == 'ô':
            pyautogui.press('^')
            pyautogui.press('o')
        elif caractere == 'ç':
            pyautogui.keyDown('´')
            pyautogui.press('c')
            time.sleep(0.1)
            pyautogui.keyUp('´')
        else:
            pyautogui.write(caractere, interval=0.1)  # Digita os outros caracteres normalmente

    print("Texto digitado com sucesso!")

# Função para iniciar a digitação
def iniciar_digitacao():
    global executando
    executando = True
    texto = campo_texto.get("1.0", tk.END)  # Obtém o texto do widget Text
    threading.Thread(target=digitar_com_acento, args=(texto,)).start()

# Função para parar a digitação
def parar_digitacao():
    global executando
    executando = False
    print("Digitação interrompida.")

# Criação da interface gráfica
janela = tk.Tk()
janela.title("Auto-Typer Controlável")

# Campo de texto para entrada do usuário
campo_texto = tk.Text(janela, height=10, width=50)
campo_texto.pack(pady=10)

# Botões de controle
botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_digitacao, width=20)
botao_iniciar.pack(pady=5)

botao_parar = tk.Button(janela, text="Parar", command=parar_digitacao, width=20)
botao_parar.pack(pady=5)

# Executa a interface
janela.mainloop()

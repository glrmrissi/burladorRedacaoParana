
import pyautogui
import time

# Aguarda para você posicionar o cursor no local desejado
print("Posicione o cursor no local desejado. Você tem 5 segundos...")
time.sleep(5)

# Texto que precisa ser digitado
texto = "Seu texto vai aqui"

# Função para digitar o texto com acentos
def digitar_com_acento(texto):
    for caractere in texto:
        if caractere == 'á':
            pyautogui.press('´')  # Pressiona o acento agudo
            pyautogui.press('a')   # Pressiona a letra 'a'
        elif caractere == 'é':
            pyautogui.press('´')  # Pressiona o acento agudo
            pyautogui.press('e')   # Pressiona a letra 'e'
        elif caractere == 'í':
            pyautogui.press('´')  # Pressiona o acento agudo
            pyautogui.press('i')   # Pressiona a letra 'i'
        elif caractere == 'ó':
            pyautogui.press('´')  # Pressiona o acento agudo
            pyautogui.press('o')   # Pressiona a letra 'o'
        elif caractere == 'ú':
            pyautogui.press('´')  # Pressiona o acento agudo
            pyautogui.press('u')   # Pressiona a letra 'u'
        elif caractere == 'ã':
            pyautogui.press('~')  # Pressiona o til
            pyautogui.press('a')   # Pressiona a letra 'a'
        elif caractere == 'õ':
            pyautogui.press('~')  # Pressiona o til
            pyautogui.press('o')   # Pressiona a letra 'o'
        elif caractere == 'â':
            pyautogui.press('^')  # Pressiona o acento circunflexo
            pyautogui.press('a')   # Pressiona a letra 'a'
        elif caractere == 'ê':
            pyautogui.press('^')  # Pressiona o acento circunflexo
            pyautogui.press('e')   # Pressiona a letra 'e'
        elif caractere == 'ô':
            pyautogui.press('^')  # Pressiona o acento circunflexo
            pyautogui.press('o')   # Pressiona a letra 'o'
        elif caractere == 'ç':
            pyautogui.keyDown('´') # Era pra funcionar no teclado americano, porém não está funciando | Ver depois | 
            pyautogui.press('c')   # Pressiona diretamente o 'c'
            time.sleep(0.1)
            pyautogui.keyUp('´')
        else:
            pyautogui.write(caractere, interval=0.1)  # Digita os outros caracteres normalmente

# Chama a função para digitar o texto com acentos
digitar_com_acento(texto)

print("Texto digitado com sucesso! Paraná é um lixo")

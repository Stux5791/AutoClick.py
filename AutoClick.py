import pyautogui
import time

while True:

    tempoparainiciar = float(input("\nInforme o tempo para iniciar em segundos! "))
        # Puxa o valor da resposta do usuário (Float), e retorna em tempo para o autoclick iniciar


    totalclicks = int(input("\nInforme o total de clicks! "))
    if totalclicks <= 0: # Se o total de clicks informado pelo usuário for menor ou igual a 0, totalclicks = 1
        totalclicks = 1


    delayclicks = float(input("\nInforme o tempo de cada click em segundos! "))
        # Puxa o valor da resposta do usuário (Float), e retorna em delay para cada click


    time.sleep(tempoparainiciar)
    for clicks in range(totalclicks):
        time.sleep(delayclicks)
        pyautogui.leftClick()

import pyautogui as py
import time as t

#Parar o Código
py.FAILSAFE = True

# Interação com o usuário
print('--- CONFIGURANDO A LIMPEZA AUTOMÁTICA ---')
origem = input('De qual pasta você quer retirar os arquivos? (Ex.: downloads): ')
extensao = input('Qual é a extensão dos arquivos: (Ex.: pdf ou png): ')
destino = input('Para qual pasta você quer mover? (Ex.: imagens): ')

print(f'\nPerfeito. Irei mover arquivos {extensao} de {origem} para {destino}.')
print('\nIniciando em 5 segundos...')
t.sleep(5)

# 1° Passo: abre o explorador de arquivos
py.hotkey('win', 'e')
t.sleep(1)

# 2° Passo: abre a pasta que o usuário digitou
py.hotkey('alt', 'd')
t.sleep(0.5)
py.write(origem, interval=0.05)
t.sleep(0.5)
py.press('enter')
t.sleep(0.5)

# 3° Passo: seleciona e recorta os arquivos com a extensão do usuário
py.hotkey('ctrl', 'f')
t.sleep(0.5)
py.write(f'ext: {extensao}', interval=0.05)
t.sleep(0.5)
py.press('enter')
t.sleep(0.5)
py.press('tab')
t.sleep(0.5)
py.hotkey('ctrl', 'a')
t.sleep(0.5)
py.hotkey('ctrl', 'x')
t.sleep(0.5)

# 4° Passo: vai para a pasta de destino
py.hotkey('alt', 'd')
t.sleep(0.5)
py.write(destino, interval=0.05)
t.sleep(0.5)
py.press('enter')
t.sleep(0.5)

# 5° Passo: cola os arquivos
for i in range(12):
    py.press('tab')
py.hotkey('ctrl', 'v')
t.sleep(2)
py.hotkey('alt', 'f4')

# Informando a finalização
print('Arquivos organizados com sucesso!')
t.sleep(3)
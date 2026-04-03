# 📂 Python File Organizer (RPA)

Este é um projeto de automação robótica de processos (RPA) desenvolvido em **Python**. O script utiliza a biblioteca **PyAutoGUI** para interagir com a interface gráfica do Windows, automatizando a organização de arquivos entre diferentes diretórios de forma dinâmica.

---

## 🚀 Funcionalidades

Diferente de automações estáticas, este script permite que o usuário interaja via terminal para definir os parâmetros de execução:

* **Origem:** A pasta de onde os arquivos serão retirados.
* **Extensão:** Qual tipo de arquivo deve ser filtrado (ex: `pdf`, `png`, `docx`).
* **Destino:** A pasta para onde os arquivos serão movidos.

O robô utiliza comandos de teclado e atalhos do sistema para filtrar, selecionar, recortar e colar os arquivos, simulando o comportamento humano com precisão.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.14.3**
* **PyAutoGUI:** Para automação da interface gráfica (GUI Automation).
* **Time:** Para controle de fluxo e sincronização com o Sistema Operacional.

---

## 📋 Pré-requisitos

Antes de rodar o script, você precisará instalar a biblioteca PyAutoGUI via terminal:

```bash
pip install pyautogui

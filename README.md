### DESAFIO

## CRIANDO UM RANSOMARE
# CRIPTOGRAFANDO ARQUIVOS

Começamos pela preparação do ambiente simulando, em uma pasta, a existência de 2 (dois) arquivos importantes cujo teor deve ser resguardado.
Na sequência, redigimos o arquivo Python que executará a criptografia/descriptografia dos arquivos atacados.

Executado o script acima, a pasta alvo teve todos seus arquivos criptografados. Sua vida foi desgraçada!

# DESCRIPTOGRAFANDO OS ARQUIVOS ATACADOS
A seguir o script que permitirá a recuperação dos dados originais (sem a criptografia aplicada).


## CRIANDO UM KEYLLOGER

A função desse malware é o monitoramento e registro de todas as entradas de dados via teclado. Tudo que é digitado é capturado e enviado ao agente mal intencionado que poderá fazer diversos usos indevidos (criminosos e danosos) com tais dados.
Preparando o ambiente, criamos uma nova pasta com a instalação da biblioteca Pynput (pip install pynput) que tem a finalidade de “permite controlar e monitorar dispositivos de entrada” (mouse/teclado) de sua máquina.

Esquema de uso:
1 - Vai ficar em execução em segundo plano;
2 -  Toda vez que o usuário digitar uma tecla, o programa vai capturar essa tecla;
3 – O que for digitado, será gravado num arquivo “.txt”; e
4 -  O arquivo vai mostrar tudo o que foi digitado, de forma sequencial.

Rodando o script pudemos capturar os dados que foram digitados no teclado e registramos esses no respectivo arquivo de logs para posterior consulta e uso.

## TORNANDO UM KEYLLOGER “INVISÍVEL À VÍTIMA.

Nesta etapa iniciamos com um simples movimento: a mudança da extensão do nosso script de “.py” para “.pyw”. Esta ação ativa uma funcionalidade nativa do Python, atenção!!, no Windows. Essa mudança permite que o script rode em “background” no sistema Windows, sem ser notado.

## ENVIANDO OS DADOS CAPTURADOS REMOTAMENTE

Inicialmente é preciso de uma conta exclusiva para testes, por questões de segurança. Esta conta será utilizada no teste e deve ser ativada a verificação em 2 (duas) etapas.
O script a seguir realiza a automação do envio de mensagens periódicas ao atacante com os dados coletados de tempo em tempo.

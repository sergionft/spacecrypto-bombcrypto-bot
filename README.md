# SpaceCrypto And Bombcrypto Bot - MultiScreen
This is a open source project inspired on bombcrypto-bot that was a success auto click bot that helped me a lot.

So, I decided to create a new auto click bot for the new NFT game space crypto. (It is not soo easy) I hope you like

To maintain the improvments and this auto click bot free, please help me with any value, have fun :)

Metamask wallet (BNB/SPG/BUSD/BCOIN): 0xa5e1412B4dBf4bE9Fb3f52b12aBFF7A78272B9b3


CANAL DISCORD
https://discord.gg/ahwf3Nfd

## Funções extras adicionadas

- Suporte a multiplas contas no mesmo monitor

# Instalação:

1- Baixe e instale Python na versão maior que 3 no [site oficial](https://www.python.org/downloads/) ou através da [windows store](https://www.microsoft.com/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab).

2 - Após instalado python:

- Para `windows` _execute como administrador_ o arquivo `run.bat` na pasta principal.
- Para `linux` o arquivo `run.sh` na pasta principal.

# Configurações:

Você pode configurar algumas opções alterando o arquivo `config.yaml` na pasta principal do bot.

## `scale_image`

- Você agora tem suporte de colocar quantos % de zoom está usando em seu navegador.

  > Se atente também ao ZOOM da janela de notificação do _Metamask_, ela deve ser a mesma usada no navegador.

  - ### `enable`

    Quando `True`, ativa a funcionalidade de usar um scale diferente. Caso contrário, deixe o valor como `False`

    > O valor deve ser: `True` ou `False`

  - ### `percent`
    A porcentagem de zoom do seu navegador e da janela de notificação do metamask.
    > O Valor deve ser de: `50` a `100`. Quanto menor o valor, mais impreciso serão as detecções do bot.

## `is_retina_screen`

- Caso seu computador seja um dispositivo mac com tela retina, será necessário ativar essa opção para que o bot realize clicks com precisão. Se seu bot move o mouse para lugares aleatórios, talvez essa opção te ajude.
  > O valor deve ser: `True` para ativar, ou `False` para desativar

## `mouse_move_speed`

- Você pode configurar a velocidade com que o mouse se move na tela antes da realização do click.
  > O valor deve ser de: `0.1` a `1`

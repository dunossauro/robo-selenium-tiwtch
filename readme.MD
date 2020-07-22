# Twitch Selenium bot

Bot feito na livedepython para brincar com selenium.

## como instalar
```bash
pip install twitchio selenium
```

É necessario ter o docker instalado para rodar o browser remoto

## Subindo a iamgem no docker

```bash
docker run -p 4444:4444 -p 5900:5900 --shm-size 2g selenium/standalone-firefox-debug:3.141.59
```

## Rodar o bot

```bash
python bot.py
```


## Comandos do bot

comando | faz o que
--------| ---------
!numero | joguinho para tentar adivinhar o numero
!linguagem | Dá uma linguagem para @você
!abrir <url> | Abre uma url no browser
!enviar_texto <css_selector> <text> | Digita um texto no browser
!clicar <css_selector> | clica em um elemento no browser



## Exemplos usando comandos

#### Buscando batatinha no duckduckGo
```
!abrir http://ddg.gg
!enviar_texto #search_form_input_homepage batatinha
!clicar #search_button_homepage
```

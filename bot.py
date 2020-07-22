from twitchio.ext import commands
from os import environ
from random import randint, choice
from selenium.webdriver import Remote


numero = randint(1, 100000)

browser = Remote(
    desired_capabilities={'browserName': 'firefox'}
)

bot = commands.Bot(
    irc_token=environ['IRC_TOKEN'],
    client_id=environ['CLIENTE_ID'],
    nick='livedepython',
    prefix='!',
    initial_channels=['livedepython'],
)


langs = [
    'ASP',
    'ActionScript',
    'C',
    'C++',
    'C#',
    'Pascal',
    'Euphoria',
    'Java',
    'JavaScript',
    'Lua',
    'MATLAB',
    'PHP',
    'Python',
    'R',
    'Ruby',
    'Tcl',
    'Visual Basic',
]


@bot.event
async def event_ready():
    print('estamos de pé')


@bot.command(name='numero')
async def test(context):
    try:
        if str(numero) == context.content.split()[1]:
            await context.send(f'@{context.author.name} Acertou é {numero}')
        else:
            if numero > int(context.content.split()[1]):
                await context.send(
                    f'@{context.author.name} Errou, o número é maior!'
                )
            else:
                await context.send(
                    f'@{context.author.name} Errou, o número é menor!'
                )

    except:
        await context.send(f'Olar {context.author.name}!')


@bot.command(name='linguagem')
async def test(context):
    await context.send(f'@{context.author.name} programa em {choice(langs)}')



@bot.command(name='abrir')
async def test(context):
    cmd, url, *_ = context.content.split()
    try:
        browser.get(url)
    except:
        ...


@bot.command(name='enviar_texto')
async def test(context):
    cmd, css_selector, *texto = context.content.split()
    try:
        texto = ' '.join(texto)
        elemento = browser.find_element_by_css_selector(css_selector)
        elemento.send_keys(texto)
    except Exception as e:
        print(e)


@bot.command(name='clicar')
async def test(context):
    cmd, css_selector, *_ = context.content.split()
    try:
        elemento = browser.find_element_by_css_selector(css_selector)
        elemento.click()
    except Exception as e:
        print(e)


bot.run()

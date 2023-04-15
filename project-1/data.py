HELP_TEXT = '''
/start - запуск бота
/help - все команды
/description - описание бота
/keyboard - клавиатура комманд'''
from random import randint
agents = {'omen' : 'https://4kwallpapers.com/images/wallpapers/omen-valorant-pc-games-2020-games-1920x1200-2822.png',
          'raze' : 'http://mobimg.b-cdn.net/v3/fetch/ee/eedeb6d7328ea9469e9cd6dd84afd7d9.jpeg',
          'sage' : 'http://mobimg.b-cdn.net/v3/fetch/30/302986521ec1d1a44b477c7c63059033.jpeg',
          'geko' : 'https://triangle-news.ru/wp-content/uploads/2023/03/4xut7rxrrbh_7oa6in0o0unfxmigcg_xiycejdofayztl7e_imjtfshpephbnb1fqxoquu6phcdkd0flcoeq1plv.jpg'}
random_index = randint(1, len(agents))


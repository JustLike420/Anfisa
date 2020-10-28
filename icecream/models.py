from django.db import models
# как-бы база данных
# Create your models here.
icecream_db = [
    {
    'name': 'Золотое мороженое',
    'description': ('Шарики таитянского ванильного мороженого, шоколад '
                    '"Amedei Porcelana" и груда экзотических фруктов.'
                    'Всё это покрыто золотой фольгой, '
                    'её тоже полагается съесть.'),
    },
    {
    'name': 'Готическое мороженое',
    'description': ('Чёрное мороженое в чёрном вафельном рожке для '
                    'true black goths. Состав: сливочное мороженое, '
                    'миндаль, активированный уголь, чернота, мрак, '
                    'отрицание.'),
    },
    {
    'name': 'Мороженое паста карбонара',
    'description': ('Порция макарон под тёмным соусом. '
                    'Паста — из ванильного мороженого, '
                    'продавленного через пресс с дырочками, '
                    'соус — ликёр с орехами. Buon appetito!'),
    },
    {
    'name': 'Фруктово-ягодное мороженое ГОСТ 119-52',
    'description': ('Сырьё: сливки, пахта, фрукты и ягоды в свежем виде, '
                    'яичный порошок из куриных яиц, патока карамельная. '
                    'Общее количество микробов в 1 мл мороженого: '
                    'не более 250 тыс.'),
    },
    {
    'name': 'Люминесцентное мороженое',
    'description': ('Сливочное мороженое с белками, '
                    'активированными кальцием. '
                    'Светится, если облизнуть. '
                    'Можно подавать в тыкве на Хэллоуин '
                    'или кормить собаку Баскервилей.'),
    },
    {
    'name': 'Жареное мороженое',
    'description': ('Шарики мороженого обваливают в яйце и в панировке, '
                    'сильно замораживают и быстро обжаривают '
                    'в растительном масле. Едят быстро.'),
    },
    {
    'name': 'Мороженное от Just_like',
    'description': ('Чипсы, сухарики, пепси,'
                    'кока-кола. Если много'
                    'съесть, станет плохо'),
    }
]
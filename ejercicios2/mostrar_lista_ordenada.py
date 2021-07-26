tabla = [
    {
        'categoria':'accion',
        'juegos':['gta','call','pug']
    },
    {
        'categoria':'aventura',
        'juegos':['uno','dos','tres']
    },
    {
        'categoria':'deportes',
        'juegos':['beisbol','golf','futbol']
    }
]

for categ in tabla:
    print('----',categ['categoria'],'----')
    for jueguito in categ['juegos']:
        print(jueguito)
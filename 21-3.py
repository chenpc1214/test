import pygal.maps.world

mp = pygal.maps.world.World()
mp.title = "world languange"
mp.add("English",['us', 'au', 'ca', 'gb', 'nz'])
mp.add("Arabic",['ae', 'eg', 'ye', 'kw', 'sa'])
mp.add("German",['de', 'at', 'ch', 'lu', 'li'])

mp.render_to_file("world.svg")

import pygal.maps.world

mp = pygal.maps.world.World()

mp.title = "world population"

mp.add("Asian",{"cn":282162848,
                "jp":126870000,
                "th":63155029})

mp.add("North American",{"us":282162848,
                "ca":126870000,
                "mx":63155029})

mp.add("Africa",{"eg":282162848,
                "cd":126870000,
                "za":63155029})

mp.add("Europe",{"fr":282162848,
                "se":126870000,
                "ch":63155029})

mp.render_to_file("test.svg")

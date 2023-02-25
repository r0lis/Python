def operations_on_sets(balads, favourite):

    playlist_pondeli = balads.intersection(favourite)
    playlist_utery = balads.difference(favourite)
    print(playlist_pondeli, playlist_utery)


if __name__ == "__main__":
    balads = {("Led Zeppelin", "Stairway to Heaven"),
              ("Metallica", "Fade to Black"),
              ("Nirvana", "The Man Who Sold the World"),
              ("Guns N Roses", "Patience"),
              ("Nirvana", "Heart Shaped Box")}
    favourite = {("Nirvana", "The Man Who Sold the World"),
                 ("Metallica", "Fade to Black"),
                 ("Kiss", "Detroit Rock City")}

    operations_on_sets(balads, favourite)
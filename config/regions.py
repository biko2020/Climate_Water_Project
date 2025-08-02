moroccan_regions = {
    "Souss-Massa": (30.4, -9.5),
    "Marrakech-Safi": (31.6, -8.0),
    "Casablanca-Settat": (33.6, -7.6),
    "Oriental": (34.7, -2.9),
    "Fès-Meknès": (34.0, -4.9),
    "Rabat-Salé-Kénitra": (34.0, -6.8),
    "Béni Mellal-Khénifra": (32.5, -6.4),
    "Drâa-Tafilalet": (31.2, -5.5),
    "Tanger-Tétouan-Al Hoceïma": (35.0, -5.5),
    "Guelmim-Oued Noun": (28.9, -10.0),
    "Laâyoune-Sakia El Hamra": (27.2, -13.1),
    "Dakhla-Oued Ed-Dahab": (23.7, -15.9)
}

def clean_filename(region):
    return region.lower().replace(" ", "_").replace("â", "a").replace("é", "e")

from PySeoHtml import PySeoHtml

html_text = """
<p>By purchasing this exceptional villa at Apes Hill, you gain access to a world - class golf resort community where timeless elegance meets unparalleled beauty. Spanning 475 acres, Apes Hill offers an impressive collection of amenities, including the renowned 18 - hole championship golf course designed by Ron Kirby, health club, nature trails, padel courts, and tennis courts.</p>
<p>Additionally, the beautiful beaches, galleries, restaurants, and museums of Holetown are just a short drive away, providing endless opportunities for leisure and entertainment.</p>
<p>Don' t miss out on the chance to embrace refined luxury living in Barbados. us today to make this exceptional villa your own!</p>
"""

keywords = {
    "barb": "https://ok.com",
    # "roa": "https://road.com",
}

processor = PySeoHtml(html_text, keywords)
processed_text = processor.process_text()

print('before', html_text)
print('after', processed_text)

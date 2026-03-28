import pandas as pd

def load_data():
    carros = [
        {"nome": "Renault Kwid", "preco": 45000, "economia": 9, "conforto": 5, "espaco": 4, "categoria": "urbano"},
        {"nome": "Fiat Mobi", "preco": 47000, "economia": 8, "conforto": 5, "espaco": 4, "categoria": "urbano"},
        {"nome": "Hyundai HB20", "preco": 75000, "economia": 8, "conforto": 7, "espaco": 6, "categoria": "hatch"},
        {"nome": "Chevrolet Onix", "preco": 78000, "economia": 8, "conforto": 7, "espaco": 6, "categoria": "hatch"},
        {"nome": "Onix Plus", "preco": 85000, "economia": 9, "conforto": 8, "espaco": 8, "categoria": "sedan"},
        {"nome": "Toyota Yaris", "preco": 90000, "economia": 7, "conforto": 8, "espaco": 7, "categoria": "sedan"},
        {"nome": "Citroen C3", "preco": 65000, "economia": 7, "conforto": 6, "espaco": 6, "categoria": "hatch"},
    ]
    return pd.DataFrame(carros)

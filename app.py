from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Plik do przechowywania danych o książkach
PLIK_JSON = 'ksiazki.json'

# Wczytaj dane początkowe z pliku
try:
    with open(PLIK_JSON, 'r', encoding='utf-8') as plik:
        ksiazki = json.load(plik)
except FileNotFoundError:
    ksiazki = []
    # Przykładowe dane początkowe
    przykladowe_ksiazki = [
        {"id": 1, "tytul": "W pustyni i w puszczy", "autor": "Henryk Sienkiewicz", "rok": 1911, "kategoria": "Przygoda", "ocena": 8},
        {"id": 2, "tytul": "Pan Tadeusz", "autor": "Adam Mickiewicz", "rok": 1834, "kategoria": "Epos", "ocena": 7},
    ]
    ksiazki.extend(przykladowe_ksiazki)
    with open(PLIK_JSON, 'w', encoding='utf-8') as plik:
        json.dump(ksiazki, plik, ensure_ascii=False, indent=4)

# GET wszystkie książki
@app.route('/ksiazki', methods=['GET'])
@cross_origin()
def pobierz_ksiazki():
    return jsonify({"ksiazki": ksiazki})

# GET konkretną książkę po ID
@app.route('/ksiazki/<int:id_ksiazki>', methods=['GET'])
def pobierz_ksiazke(id_ksiazki):
    ksiazka = next((ksiazka for ksiazka in ksiazki if ksiazka['id'] == id_ksiazki), None)
    if ksiazka:
        return jsonify({"ksiazka": ksiazka})
    else:
        return jsonify({"komunikat": "Książka nie znaleziona"}), 404

# POST nową książkę
@app.route('/ksiazki', methods=['POST'])
def dodaj_ksiazke():
    nowa_ksiazka = request.get_json()
    nowa_ksiazka['id'] = len(ksiazki) + 1
    ksiazki.append(nowa_ksiazka)
    aktualizuj_plik_json()
    return jsonify({"komunikat": "Książka dodana pomyślnie", "ksiazka": nowa_ksiazka}), 201

# PUT zaktualizuj książkę po ID
@app.route('/ksiazki/<int:id_ksiazki>', methods=['PUT'])
def aktualizuj_ksiazke(id_ksiazki):
    ksiazka = next((ksiazka for ksiazka in ksiazki if ksiazka['id'] == id_ksiazki), None)
    if ksiazka:
        zaktualizowana_ksiazka = request.get_json()
        ksiazka.update(zaktualizowana_ksiazka)
        aktualizuj_plik_json()
        return jsonify({"komunikat": "Książka zaktualizowana pomyślnie", "ksiazka": ksiazka})
    else:
        return jsonify({"komunikat": "Książka nie znaleziona"}), 404

# DELETE książkę po ID
@app.route('/ksiazki/<int:id_ksiazki>', methods=['DELETE'])
def usun_ksiazke(id_ksiazki):
    global ksiazki
    ksiazki = [ksiazka for ksiazka in ksiazki if ksiazka['id'] != id_ksiazki]
    aktualizuj_plik_json()
    return jsonify({"komunikat": "Książka usunięta pomyślnie"})

def aktualizuj_plik_json():
    with open(PLIK_JSON, 'w', encoding='utf-8') as plik:
        json.dump(ksiazki, plik, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(debug=True)

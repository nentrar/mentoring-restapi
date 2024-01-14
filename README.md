# Proste REST API dla bazy książek

Projekt ten dostarcza prostą implementację REST API do zarządzania książkami w języku Python przy użyciu frameworku Flask. 
Repozytorium to zostało stworzone w celach edukacyjnych, aby umożliwić naukę podstawowych koncepcji związanych z REST API i zapytaniami HTTP.

## Instalacja

1. Sklonuj repozytorium do lokalnego środowiska:

    ```bash
    git clone https://github.com/nentrar/mentoring-restapi.git
    ```

2. Przejdź do folderu projektu:

    ```bash
    cd mentoring-restapi
    ```

3. Opcjonalnie, utwórz i aktywuj wirtualne środowisko:

    ```bash
    python -m venv venv
    source venv/bin/activate    # Dla systemów Unix/Linux
    # lub
    .\venv\Scripts\activate     # Dla systemu Windows
    ```

4. Zainstaluj zależności:

    ```bash
    pip install flask
    ```

## Uruchamianie

1. Upewnij się, że jesteś w głównym folderze projektu.

2. Uruchom aplikację Flask:

    ```bash
    flask run
    ```

3. Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000/` w przeglądarce.

## Korzystanie z API

- **GET - wszystkie książki:** [http://127.0.0.1:5000/ksiazki](http://127.0.0.1:5000/ksiazki)
- **GET - ale konkretna książka po ID:** [http://127.0.0.1:5000/ksiazki/1](http://127.0.0.1:5000/ksiazki/1)
- **POST - dodawanie nowej książki:** [http://127.0.0.1:5000/ksiazki](http://127.0.0.1:5000/ksiazki)
- **PUT - aktualizacja książki po ID:** [http://127.0.0.1:5000/ksiazki/1](http://127.0.0.1:5000/ksiazki/1)
- **DELETE - usuwanie książki po ID:** [http://127.0.0.1:5000/ksiazki/1](http://127.0.0.1:5000/ksiazki/1)

## Uwagi

To repozytorium zostało stworzone w celach edukacyjnych, aby ułatwić zrozumienie podstawowych koncepcji związanych z REST API i HTTP. 
Zachęcam do eksperymentowania z kodem oraz korzystania z narzędzi takich jak Postman do testowania i zrozumienia, jak działa to proste API do zarządzania książkami.

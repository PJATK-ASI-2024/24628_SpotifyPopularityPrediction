# Aplikacja API - Instrukcje uruchomienia i testowania

## Wymagania

1. **Docker** – musisz mieć zainstalowanego Dockera na swoim komputerze. Jeśli nie masz Dockera, zainstaluj go z [oficjalnej strony Docker](https://www.docker.com/get-started).
2. **Postman** – aplikacja do testowania API. Można pobrać z [oficjalnej strony Postman](https://www.postman.com/downloads/).

## Instrukcje uruchomienia aplikacji

1. **Zbudowanie obrazu Dockera**:

   Otwórz terminal w katalogu z projektem i wykonaj polecenie, aby zbudować obraz aplikacji:

   ```bash
   docker build -t asi/app .
   ```
   To polecenie utworzy obraz aplikacji o nazwie asi/app na podstawie pliku Dockerfile w katalogu.

2. **Uruchomienie kontenera z aplikacją**:
   Po zbudowaniu obrazu, uruchom kontener z aplikacją:
   ```bash
   docker run --rm -p 5000:5000 asi/app
   ```
  To polecenie uruchomi kontener i przypisze port 5000 kontenera do portu 5000 na twoim lokalnym komputerze. Aplikacja będzie dostępna pod adresem http://localhost:5000.
## Testowanie API za pomocą Postmana
<img width="900" alt="Zrzut ekranu 2024-12-4 o 14 26 31" src="https://github.com/user-attachments/assets/16fefb2f-c39e-4063-94e8-08d11cc484d6">

Metoda: GET
URL: http://127.0.0.1:5000/predict
Body: 
```
  {
  "id": "0xGQ6J6Wm65wy1GeORLIfV",
  "name": "French",
  "genre": "french",
  "artists": "Minus Manus, The Second Level, Oda Loves You",
  "album": "French",
  "duration_ms": 127747,
  "explicit": false
}
```
Powinna zostać zwrócona odpowiedź JSON, z predykcją regresji np.:
```
{
    "prediction": 0.31921148051303183
}
```

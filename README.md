# Analiza Czynników Wpływających na Wyniki Uczniów

## Opis projektu
Celem projektu jest zrozumienie czynników, które mogą mieć wpływ na wyniki uczniów. Analiza obejmuje zbadanie zmiennych, takich jak czas poświęcony na naukę, obecność na zajęciach oraz wsparcie rodziny.

## Źródło danych
- **Zbiór danych:** [Student Performance Factors](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)
- **Charakterystyka:** Dane dotyczące wyników uczniów wraz z czynnikami mogącymi mieć na nie wpływ.

## Dane
Ten zbiór danych dostarcza kompleksowego przeglądu różnych czynników wpływających na wyniki uczniów na egzaminach. Zawiera informacje dotyczące nawyków związanych z nauką, frekwencji, zaangażowania rodziców oraz innych aspektów wpływających na sukces akademicki.

## Opis Kolumn

| Atrybut                   | Opis                                                                                         |
|---------------------------|----------------------------------------------------------------------------------------------|
| **Hours_Studied**         | Liczba godzin poświęconych na naukę tygodniowo.                                              |
| **Attendance**            | Procent obecności na zajęciach.                                                              |
| **Parental_Involvement**  | Poziom zaangażowania rodziców w edukację ucznia (Niski, Średni, Wysoki).                     |
| **Access_to_Resources**   | Dostępność zasobów edukacyjnych (Niska, Średnia, Wysoka).                                    |
| **Extracurricular_Activities** | Udział w zajęciach pozalekcyjnych (Tak, Nie).                                          |
| **Sleep_Hours**           | Średnia liczba godzin snu na noc.                                                            |
| **Previous_Scores**       | Wyniki z poprzednich egzaminów.                                                              |
| **Motivation_Level**      | Poziom motywacji ucznia (Niski, Średni, Wysoki).                                             |
| **Internet_Access**       | Dostępność dostępu do Internetu (Tak, Nie).                                                  |
| **Tutoring_Sessions**     | Liczba sesji korepetycji w miesiącu.                                                         |
| **Family_Income**         | Poziom dochodu rodziny (Niski, Średni, Wysoki).                                              |
| **Teacher_Quality**       | Jakość nauczycieli (Niska, Średnia, Wysoka).                                                 |
| **School_Type**           | Typ szkoły, do której uczęszcza uczeń (Publiczna, Prywatna).                                 |
| **Peer_Influence**        | Wpływ rówieśników na wyniki akademickie (Pozytywny, Neutralny, Negatywny).                   |
| **Physical_Activity**     | Średnia liczba godzin aktywności fizycznej tygodniowo.                                       |
| **Learning_Disabilities** | Obecność trudności w uczeniu się (Tak, Nie).                                                 |
| **Parental_Education_Level** | Najwyższy poziom wykształcenia rodziców (Liceum, Studia, Studia podyplomowe).            |
| **Distance_from_Home**    | Odległość od domu do szkoły (Blisko, Średnia, Daleko).                                       |
| **Gender**                | Płeć ucznia (Mężczyzna, Kobieta).                                                            |
| **Exam_Score**            | Końcowy wynik na egzaminie.                                                                  |


## Cele projektu
1. Zidentyfikowanie kluczowych czynników wpływających na wyniki uczniów.
2. Budowa modelu predykcyjnego do przewidywania wyników uczniów.
3. Wyciągnięcie wniosków przydatnych dla instytucji edukacyjnych.

## Struktura projektu
- Przetwarzanie danych: pobieranie, obróbka i przygotowanie danych.
- Eksploracja i analiza danych: EDA, wykrywanie braków, wstępne przetwarzanie.
- Trenowanie modelu: dobór i dostosowanie modelu ML do wybranego problemu.
- Walidacja i testowanie: walidacja modelu na danych testowych, monitorowanie wyników.
- Dokształcanie modelu: dalsze trenowanie na nowych danych.
- Publikacja i wdrożenie: przygotowanie modelu do wdrożenia, konteneryzacja.
- Prezentacja i raport końcowy: przygotowanie do prezentacji wyników.

## Analiza Raportu Profilowania Danych

Dokument ten zawiera kluczowe wnioski z raportu profilowania danych oraz wskazuje obszary, które mogą wymagać poprawy lub głębszej analizy.

---

## Podsumowanie

Raport profilowania ocenia zbiór danych pod kątem jakości danych, w tym braków, wzorców rozkładu oraz potencjalnych anomalii. Analiza ma na celu zidentyfikowanie kluczowych obszarów wymagających uwagi w zbiorze danych.

---

## Podsumowanie Jakości Danych

| Metrika               | Wartość                |
|-----------------------|------------------------|
| Całkowita liczba rekordów | *Liczba rekordów*   |
| Liczba analizowanych cech  | *Liczba cech*     |
| Brakujące wartości    | *Ogólny procent braków*|
| Zduplikowane wiersze  | *Procent duplikatów*   |
| Skewness rozkładów    | *Liczba cech ze skewness*|

### Kluczowe Wnioski

1. **Brakujące Wartości**: W kilku cechach, takich jak *Cech X* i *Cech Y*, występuje znaczny procent brakujących wartości. Możliwe działania obejmują imputację brakujących danych lub dalszą analizę, aby sprawdzić, czy istnieje jakiś wzorzec.
2. **Zduplikowane Wiersze**: Około *X%* wierszy stanowią duplikaty, co może świadczyć o problemach z wprowadzaniem danych lub łączeniem różnych źródeł.
3. **Wartości odstające**: Wykryto znaczące wartości odstające w *Cech Z*. Mogą one wpływać na analizy – warto rozważyć dalsze badania lub skalowanie.

---

## Spostrzeżenia według Cech

### Cechy 1: *Nazwa Cechy*

- **Rozkład**: *Opis rozkładu (np. normalny, skośny)*.
- **Brakujące Wartości**: *X%* wartości jest brakujących.
- **Wartości odstające**: Wykryte na *wysokich/niskich zakresach*; mogą wymagać dalszego przetwarzania.
- **Korelacja z innymi Cechami**: *Opis, jeśli dotyczy*.

### Cechy 2: *Nazwa Cechy*

- **Rozkład**: *Opis rozkładu*.
- **Unikalne Wartości**: *Liczba unikalnych wartości*.
- **Brakujące Wartości**: *X% wartości brakujących*.
- **Kluczowe Spostrzeżenia**: 
  - *Wnioski dotyczące wzorców lub nieregularności*.

---

## Wnioski

Profilowanie danych ujawnia istotne informacje, które są kluczowe dla dalszych analiz. Sugerowane kroki obejmują:
- **Zarządzanie Brakującymi Wartościami**: Strategie wypełniania brakujących wartości w *Cech X* i *Cech Y*.
- **Zarządzanie Wartościami Odstającymi**: Podjęcie decyzji dotyczącej obsługi wartości odstających dla *Cech Z*.
- **Spójność Danych**: Rozważ przegląd procesów, aby ograniczyć występowanie duplikatów.

**Kolejne Kroki**: Przeprowadzenie czyszczenia danych na podstawie powyższych obserwacji oraz rozważenie inżynierii cech, gdzie korelacje mogą sugerować zmienne ukryte.

## Wybór najlepszego modelu przy użyciu narzędzia automl
Narzędzie **TPOT** wielokrotnie przy różnych parametrach wskazuje RandomForestRegressor jako najlepszy model
```
Best pipeline: RandomForestRegressor(StandardScaler(input_matrix), bootstrap=True, max_features=0.45, min_samples_leaf=16, min_samples_split=9, n_estimators=100)
Najlepszy model sugerowany przez TPOT:
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('randomforestregressor',
                 RandomForestRegressor(max_features=0.45, min_samples_leaf=16,
                                       min_samples_split=9, random_state=42))])
Dokładność na zbiorze testowym: -52.797815806700605
```

# Analiza Czynników Wpływających na Choroby Serca

## Opis projektu
Celem projektu jest zrozumienie czynników, które mogą mieć wpływ na wystąpienie choroby serca. Analiza obejmuje zbadanie zmiennych, takich jak wiek, płeć, ból w klatce piersiowej, ciśnienie krwi, poziom cholesterolu, czy cukrzyca, a także inne zmienne, które mogą mieć wpływ na zdrowie serca.

## Źródło danych
- **Zbiór danych:** [Heart Disease Dataset](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)
- **Charakterystyka:** Zbiór danych dotyczy pacjentów z ryzykiem chorób serca i zawiera różne czynniki zdrowotne, które mogą wskazywać na obecność lub brak choroby serca.

## Dane
Zbiór danych zawiera informacje o pacjentach, którzy byli badani w związku z chorobą serca. Celem jest wykrycie, które czynniki mają największy wpływ na wystąpienie choroby serca.

## Opis Kolumn

| Atrybut                         | Opis                                                                                             |
|----------------------------------|--------------------------------------------------------------------------------------------------|
| **age**                          | Wiek pacjenta (w latach).                                                                        |
| **sex**                          | Płeć pacjenta (1 = mężczyzna, 0 = kobieta).                                                      |
| **chest pain type**              | Rodzaj bólu w klatce piersiowej (0 = brak, 1 = ból typowy, 2 = ból nietypowy, 3 = brak bólu).      |
| **resting blood pressure**       | Ciśnienie krwi w spoczynku (mm Hg).                                                              |
| **serum cholestoral**            | Poziom cholesterolu w surowicy (mg/dl).                                                          |
| **fasting blood sugar**          | Poziom cukru na czczo (1 = większy niż 120 mg/dl, 0 = mniejszy lub równy 120 mg/dl).              |
| **resting electrocardiographic results** | Wyniki EKG w spoczynku (0 = brak, 1 = nieprawidłowe, 2 = prawidłowe).                            |
| **maximum heart rate achieved**  | Maksymalna osiągnięta częstość akcji serca (uderzenia na minutę).                                |
| **exercise induced angina**      | Angina wywołana wysiłkiem (1 = występuje, 0 = nie występuje).                                    |
| **oldpeak**                       | Depresja ST spowodowana wysiłkiem w porównaniu z odpoczynkiem.                                   |
| **slope of the peak exercise ST segment** | Nachylenie szczytowego segmentu ST podczas wysiłku (1 = łagodny, 2 = średni, 3 = ostry).         |
| **number of major vessels**      | Liczba głównych naczyń krwionośnych (0-3), które były widoczne w badaniach fluoroskopowych.        |
| **thal**                          | Defekt w badaniu serca (0 = normalny, 1 = stały defekt, 2 = odwracalny defekt).                   |
| **target**                        | Obecność choroby serca (1 = choroba, 0 = brak choroby).                                          |

## Cele projektu
1. Zidentyfikowanie kluczowych czynników wpływających na choroby serca.
2. Budowa modelu predykcyjnego do przewidywania ryzyka chorób serca.
3. Wyciągnięcie wniosków przydatnych dla instytucji zdrowia publicznego.

## Struktura projektu
- **Przetwarzanie danych**: Pobieranie, obróbka i przygotowanie danych.
- **Eksploracja i analiza danych**: EDA (analiza eksploracyjna danych), wykrywanie braków, wstępne przetwarzanie.
- **Trenowanie modelu**: Dobór i dostosowanie modelu ML do wybranego problemu.
- **Walidacja i testowanie**: Walidacja modelu na danych testowych, monitorowanie wyników.
- **Dokształcanie modelu**: Dalsze trenowanie na nowych danych.
- **Publikacja i wdrożenie**: Przygotowanie modelu do wdrożenia, konteneryzacja.
- **Prezentacja i raport końcowy**: Przygotowanie do prezentacji wyników.

## Analiza Raportu Profilowania Danych

Dokument ten zawiera kluczowe wnioski z raportu profilowania danych oraz wskazuje obszary, które mogą wymagać poprawy lub głębszej analizy.

---

## Wybór najlepszego modelu przy użyciu narzędzia automl

Narzędzie **TPOT** wielokrotnie przy różnych parametrach wskazuje **RandomForestClassifier** jako najlepszy model.


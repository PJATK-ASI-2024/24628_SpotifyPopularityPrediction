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

---

## Wybór najlepszego modelu przy użyciu narzędzia automl

Niniejszy dokument przedstawia analizę i porównanie trzech modeli uczenia maszynowego wygenerowanych podczas etapu wstępnej ewaluacji. Każdy model został oceniony na podstawie wyników walidacji krzyżowej, a jeden z nich został zarekomendowany do kolejnych etapów projektu.

## Rekomendowane Modele

### Model 1: LinearSVC
- **Konfiguracja**:
  - `C=20.0`
  - `dual=False`
  - `loss=squared_hinge`
  - `penalty=l2`
  - `tol=0.01`
- **Wynik Walidacji Krzyżowej**: 0.843
- **Opis**: Linear Support Vector Classification (LinearSVC) to model liniowy dobrze przystosowany do zadań klasyfikacji na dużą skalę. W tej konfiguracji wykorzystuje funkcję straty "squared hinge" i karę L2, co zapewnia odporność na przeuczenie przy wybranej wartości `C`. 
- **Uzasadnienie**: LinearSVC osiągnął najwyższy wynik walidacji krzyżowej spośród ocenianych modeli. Zapewnia równowagę między prostotą modelu a jego wydajnością klasyfikacyjną, co czyni go dobrym kandydatem do dalszych prac.

### Model 2: XGBClassifier (Konfiguracja A)
- **Konfiguracja**:
  - `learning_rate=0.1`
  - `max_depth=2`
  - `min_child_weight=4`
  - `n_estimators=100`
  - `subsample=0.70`
  - `verbosity=0`
- **Wynik Walidacji Krzyżowej**: 0.826
- **Opis**: XGBClassifier to implementacja algorytmu gradient boosting. Przy płytkiej głębokości drzew i niższej wartości `subsample` model ten jest zaprojektowany do lepszej generalizacji poprzez zmniejszenie ryzyka przeuczenia. XGBoost jest znany z dobrze radzenia sobie z bardziej złożonymi wzorcami, choć może wymagać większej ilości zasobów obliczeniowych.
- **Uzasadnienie**: Konfiguracja A modelu XGBClassifier oferuje wysoką wydajność, choć nieco niższą niż LinearSVC. Zastosowanie subsamplingu pozwala unikać przeuczenia.

### Model 3: XGBClassifier (Konfiguracja B)
- **Konfiguracja**:
  - `learning_rate=0.1`
  - `max_depth=2`
  - `min_child_weight=4`
  - `n_estimators=100`
  - `subsample=0.95`
  - `verbosity=0`
- **Wynik Walidacji Krzyżowej**: 0.826
- **Opis**: W tej konfiguracji model XGBClassifier stosuje wyższą wartość `subsample` (0.95), pozwalając na uczenie się na większej części danych w każdej iteracji. Podobnie jak w konfiguracji A, model jest zaprojektowany tak, aby ograniczać przeuczenie przy jednoczesnym uchwyceniu bardziej złożonych relacji w danych.
- **Uzasadnienie**: Wyniki walidacji krzyżowej są zbliżone do konfiguracji A, jednak różnica jest marginalna, co nie wskazuje na znaczącą przewagę.

## Wybrany Model

Model **LinearSVC** został wybrany do dalszych etapów projektu ze względu na najwyższy wynik walidacji krzyżowej i efektywność obliczeniową.




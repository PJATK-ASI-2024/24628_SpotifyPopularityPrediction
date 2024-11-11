# Analiza Czynników Wpływających na Udar

## Opis projektu
Celem projektu jest zbadanie, które czynniki zdrowotne oraz demograficzne mają wpływ na wystąpienie udaru. Analiza obejmuje zmienne takie jak wiek, płeć, poziom cukru we krwi, wskaźnik BMI, nadciśnienie, oraz inne zmienne, które mogą mieć wpływ na ryzyko wystąpienia udaru.

## Źródło danych
- **Zbiór danych:** [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Charakterystyka:** Zbiór danych zawiera informacje na temat pacjentów, uwzględniając czynniki zdrowotne i styl życia, które mogą wpływać na ryzyko udaru.

## Dane
Zbiór danych zawiera informacje o pacjentach, którzy byli badani w kontekście udaru. Celem analizy jest zidentyfikowanie czynników zwiększających ryzyko udaru oraz stworzenie modelu predykcyjnego.

## Opis Kolumn

| Atrybut             | Opis                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------|
| **id**              | Unikalny identyfikator pacjenta.                                                             |
| **gender**          | Płeć pacjenta (Male/Female).                                                                 |
| **age**             | Wiek pacjenta (w latach).                                                                    |
| **hypertension**    | Nadciśnienie (1 = obecne, 0 = brak).                                                         |
| **heart_disease**   | Obecność chorób serca (1 = obecne, 0 = brak).                                                |
| **ever_married**    | Czy pacjent był kiedykolwiek żonaty/zamężny (Yes/No).                                        |
| **work_type**       | Typ pracy pacjenta (Private, Self-employed, Govt job, Never worked, Children).               |
| **Residence_type**  | Typ miejsca zamieszkania (Urban/Rural).                                                      |
| **avg_glucose_level** | Średni poziom glukozy we krwi.                                                             |
| **bmi**             | Wskaźnik masy ciała pacjenta (BMI).                                                          |
| **smoking_status**  | Status palenia (formerly smoked, smokes, never smoked, Unknown).                             |
| **stroke**          | Wystąpienie udaru (1 = udar, 0 = brak udaru).                                                |

## Cele projektu
1. Zidentyfikowanie kluczowych czynników wpływających na wystąpienie udaru.
2. Budowa modelu predykcyjnego, który przewiduje ryzyko udaru na podstawie danych pacjentów.
3. Wyciągnięcie wniosków przydatnych dla instytucji zdrowia publicznego i praktyki medycznej.

## Struktura projektu
- **Przetwarzanie danych**: Pobieranie, obróbka i przygotowanie danych.
- **Eksploracja i analiza danych**: Analiza eksploracyjna (EDA), wykrywanie braków, przetwarzanie wstępne.
- **Trenowanie modelu**: Dobór i trenowanie modelu ML dopasowanego do problemu predykcji udaru.
- **Walidacja i testowanie**: Walidacja modelu na danych testowych, monitorowanie wyników oraz metryk.
- **Dokształcanie modelu**: Trenowanie na dodatkowych danych dla uzyskania lepszej dokładności.
- **Publikacja i wdrożenie**: Przygotowanie modelu do wdrożenia, konteneryzacja lub inne sposoby wdrożenia.
- **Prezentacja i raport końcowy**: Przygotowanie wyników i raportów końcowych.

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




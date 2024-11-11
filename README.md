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

# Wybór najlepszego modelu przy użyciu AutoML

Niniejszy dokument przedstawia analizę i porównanie trzech modeli uczenia maszynowego wygenerowanych podczas etapu wstępnej ewaluacji. Każdy model został oceniony na podstawie wyników walidacji krzyżowej, a jeden z nich został zarekomendowany do kolejnych etapów projektu.

## Rekomendowane Modele

### Model 1: KNeighborsClassifier
- **Konfiguracja**:
  - `n_neighbors=36`
  - `p=2` (odległość euklidesowa)
  - `weights=uniform`
- **Wynik Walidacji Krzyżowej**: 0.863
- **Opis**: KNeighborsClassifier jest modelem opartym na bliskości sąsiadów, co sprawia, że dobrze sprawdza się przy danych z wyraźnymi klastrami. Ten model uwzględnia 36 najbliższych sąsiadów podczas klasyfikacji nowego punktu.

### Model 2: XGBClassifier (Konfiguracja A)
- **Konfiguracja**:
  - `learning_rate=0.01`
  - `max_depth=7`
  - `min_child_weight=3`
  - `n_estimators=100`
  - `subsample=0.90`
  - `verbosity=0`
- **Wynik Walidacji Krzyżowej**: 0.863
- **Opis**: XGBClassifier stosuje gradient boosting, co pozwala mu wychwytywać złożone relacje między danymi. Przy niskim `learning_rate` model jest mniej narażony na przeuczenie i zapewnia stabilność przy wyższym `subsample`.

### Model 3: XGBClassifier (Konfiguracja B)
- **Konfiguracja**:
  - `VarianceThreshold__threshold=0.95` (filtracja niskiej wariancji)
  - `learning_rate=0.001`
  - `max_depth=10`
  - `min_child_weight=17`
  - `n_estimators=100`
  - `subsample=1.0`
  - `verbosity=0`
- **Wynik Walidacji Krzyżowej**: 0.863
- **Opis**: W tej konfiguracji model wykorzystuje selekcję cech o wysokiej wariancji, co zmniejsza ryzyko nadmiarowości i pozwala skupić się na najbardziej istotnych danych.

## Wybór Najlepszego Modelu

Po dokładnej analizie wyników walidacji krzyżowej oraz specyfiki działania każdego modelu, **Model KNeighborsClassifier** został wybrany jako najlepszy kandydat do dalszych etapów projektu. Model ten osiągnął identyczny wynik jak konfiguracje XGBClassifier, ale charakteryzuje się prostszą strukturą i mniejszym zapotrzebowaniem na zasoby obliczeniowe.

# **Analiza Popularności Utworów Muzycznych**

## **Opis Projektu**
Celem projektu jest zbadanie, które czynniki mają wpływ na popularność utworów muzycznych. Analiza obejmuje zmienne takie jak gatunek muzyczny, artyści, album, długość utworu, explicit (czy zawiera treści dla dorosłych) oraz inne zmienne, które mogą wpływać na popularność.

## **Źródło Danych**
- **Zbiór danych:** [Spotify Dataset]([https://www.kaggle.com/datasets](https://www.kaggle.com/datasets/ambaliyagati/spotify-dataset-for-playing-around-with-sql))
- **Charakterystyka:** Zbiór danych zawiera informacje o utworach muzycznych na platformie Spotify, w tym gatunki muzyczne, artyści, albumy, czas trwania utworów, oraz ich popularność.

## **Dane**
Zbiór danych zawiera informacje o utworach muzycznych, takie jak: nazwa utworu, gatunek, artyści, album, czas trwania, popularność oraz czy utwór zawiera treści explicit. Celem analizy jest stworzenie modelu predykcyjnego, który przewidzi popularność utworu na podstawie tych zmiennych.

## **Opis Kolumn**

| Atrybut             | Opis                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------|
| **id**              | Unikalny identyfikator utworu.                                                               |
| **name**            | Nazwa utworu.                                                                                 |
| **genre**           | Gatunek muzyczny (np. Acoustic, Pop, Rock).                                                  |
| **artists**         | Artyści wykonujący utwór (np. Billy Raffoul).                                                |
| **album**           | Nazwa albumu, z którego pochodzi utwór.                                                      |
| **popularity**      | Popularność utworu (na skali od 0 do 100, gdzie 100 to najwyższa popularność).                |
| **duration_ms**     | Czas trwania utworu w milisekundach.                                                          |
| **explicit**        | Informacja, czy utwór zawiera treści dla dorosłych (True/False).                             |

## **Cele Projektu**
1. Zidentyfikowanie czynników wpływających na popularność utworów muzycznych.
2. Stworzenie modelu predykcyjnego, który przewidzi popularność utworu na podstawie jego cech.
3. Analiza wpływu różnych czynników (takich jak gatunek, artyści, długość utworu) na popularność.

## **Struktura Projektu**
- **Przetwarzanie Danych**: Pobieranie, czyszczenie i przygotowanie danych do analizy (np. kodowanie zmiennych kategorycznych).
- **Eksploracja i Analiza Danych (EDA)**: Analiza wstępna danych, wykrywanie braków, analiza zależności pomiędzy zmiennymi.
- **Budowa Modelu**: Dobór i trenowanie odpowiedniego modelu ML (np. regresja, lasy losowe, XGBoost) do przewidywania popularności.
- **Walidacja Modelu**: Testowanie modelu na danych testowych, ocena skuteczności modelu przy użyciu odpowiednich metryk (np. RMSE, R^2).
- **Optymalizacja Modelu**: Dostosowanie parametrów modelu w celu poprawy wyników (np. Grid Search, Random Search).
- **Prezentacja Wyników**: Wizualizacja wyników analizy, zależności między zmiennymi oraz ocena jakości modelu.
- **Raport Końcowy**: Przygotowanie dokumentacji i raportu końcowego, w tym wniosków oraz rekomendacji.

---

# **Wybór Najlepszego Modelu przy Użyciu AutoML**

Niniejszy dokument przedstawia analizę i porównanie trzech modeli uczenia maszynowego wygenerowanych podczas etapu wstępnej ewaluacji. Każdy model został oceniony na podstawie wyników walidacji krzyżowej, a jeden z nich został zarekomendowany do kolejnych etapów projektu.

## **Rekomendowane Modele**

### **Model 1: RandomForestRegressor (Konfiguracja A)**
- **Konfiguracja**:
  - `bootstrap=True`
  - `max_features=0.7500000000000001`
  - `min_samples_leaf=3`
  - `min_samples_split=14`
  - `n_estimators=100`
- **Wynik Walidacji Krzyżowej**: -0.6617731797032844
- **Opis**: RandomForestRegressor jest modelem opartym na wielu drzewach decyzyjnych, który skutecznie radzi sobie z predykcją dla danych z dużą liczbą cech. Model ten uzyskał najlepszy wynik w analizie, jednak jego wynik walidacji wskazuje na potrzebę dalszej optymalizacji.

### **Model 2: RandomForestRegressor (Konfiguracja B)**
- **Konfiguracja**:
  - `bootstrap=False`
  - `max_features=0.4`
  - `min_samples_leaf=6`
  - `min_samples_split=18`
  - `n_estimators=100`
- **Wynik Walidacji Krzyżowej**: -0.6828323501950834
- **Opis**: Ta konfiguracja RandomForestRegressor zmienia parametry, takie jak `max_features` i `min_samples_leaf`, w celu dostosowania modelu do specyfiki danych. Wynik jest nieco gorszy od Modelu 1, ale nadal ma duży potencjał, aby uzyskać lepszą wydajność po dalszej optymalizacji.

### **Model 3: RandomForestRegressor (Konfiguracja C)**
- **Konfiguracja**:
  - `bootstrap=True`
  - `max_features=0.7500000000000001`
  - `min_samples_leaf=7`
  - `min_samples_split=9`
  - `n_estimators=100`
- **Wynik Walidacji Krzyżowej**: -0.6842742297828467
- **Opis**: Ta konfiguracja modelu RandomForestRegressor ma wyższe wartości dla `min_samples_leaf` i `min_samples_split`, co może prowadzić do prostszych drzew decyzyjnych. Jednak uzyskany wynik walidacji jest gorszy w porównaniu do Modelu 1, co sugeruje, że ta konfiguracja może wymagać dalszej optymalizacji.

## **Wybór Najlepszego Modelu**

Po dokładnej analizie wyników walidacji krzyżowej oraz specyfiki działania każdego modelu, **Model 1: RandomForestRegressor (Konfiguracja A)** został wybrany jako najlepszy kandydat do dalszych etapów projektu. Model ten osiągnął najlepszy wynik walidacji krzyżowej i zapewnia dobrą równowagę między złożonością a efektywnością.

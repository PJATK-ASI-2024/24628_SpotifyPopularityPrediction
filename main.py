import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

csv_file = 'StudentPerformanceFactors.csv'
df = pd.read_csv(csv_file)

print("Podstawowe informacje o danych:")
print(df.info())

print("\nPodgląd danych:")
print(df.head())

print("\nStatystyki opisowe:")
print(df.describe())

train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)

print("\nRozmiar zbioru treningowego:", train_data.shape)
print("Rozmiar zbioru testowego:", test_data.shape)

print("\nStatystyki opisowe dla zbioru treningowego:")
print(train_data.describe())

print("\nStatystyki opisowe dla zbioru testowego:")
print(test_data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(train_data['Exam_Score'], kde=True, color='blue', label='Zbiór treningowy')
sns.histplot(test_data['Exam_Score'], kde=True, color='green', label='Zbiór testowy')
plt.xlabel("Exam Score")
plt.legend()
plt.title("Rozkład wyników egzaminu w zbiorze treningowym i testowym")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', square=True)
plt.title("Macierz korelacji zmiennych numerycznych")
plt.show()

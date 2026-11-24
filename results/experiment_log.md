# Dziennik eksperymentów

## Wpis: HOG + SGD-SVM — baseline A

* **Data:** 24.11.2026
* **Zadanie:** 2 - baseline model
* **Poziom (A, B albo C):** A
* **Cel albo hipoteza:** Sprawdzenie skuteczności klasycznego modelu liniowego SVM opartego na cechach HOG w klasyfikacji 12 gatunków zwierząt na zdjęciach z fotopułapek.
* **Reprezentacja i preprocessing:** Obrazy przeskalowane do 256×256 z zachowaniem proporcji i paddingiem. Ekstrakcja cech HOG z obrazów w skali szarości 128×128.. Standaryzacja cech przez StandardScaler.
* **Model i hiperparametry:** SGDClassifier z funkcją straty ‘hinge’ (liniowy SVM), ‘alpha=0.0001’, ‘max_iter=3000’, ‘tol=0.001’, ‘random_state=21’.
* **Co jest zamrożone, a co trenowane:** Reprezentacja HOG bez uczenia parametrów. Trenowany jest StandardScaler oraz klasyfikator liniowy na zbiorze train.
* **Sposób wyboru hiperparametrów (na validation albo walidacją krzyżową w obrębie train):** Wybór konfiguracji na podstawie wyników na zbiorze validation. Zbiór final test pozostaje niewykorzystany.
* **Seed:** 21
* **Wynik na validation (metryka główna i pomocnicze):** Macro F1 = 0.1213; accuracy = 0.2407; macro precision = 0.2012; macro recall = 0.1220.
* **Koszt (czas, sprzęt, pamięć):** Trening 1474 s (24 min 34 s). Środowisko Google Colab:
CPU: x86_64; Logical CPU cores: 2; Total RAM (GB): 12.67; Available RAM (GB): 10.05. Szczytowe zużycie pamięci nie było mierzone.
* **Pliki z wynikami w 'results/':** 'validation/baseline_a_metrics.json', 'validation/baseline_a_predictions.csv'.
* **Commit:** '106ea7d'
* **Wnioski:** Model osiąga niską skuteczność klasyfikacji, szczególnie dla części gatunków. Predykcje koncentrują się na kilku klasach, m.in. gazelle_thomsons i wildebeest. Analiza błędów wskazuje na trudności związane z małymi lub częściowo zasłoniętymi zwierzętami, dominacją tła oraz ograniczeniami reprezentacji HOG.

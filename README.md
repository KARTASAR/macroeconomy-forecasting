# Прогнозирование макроэкономических и финансовых переменных
> Решение команды Chill Garage на хакатоне Цифрового Прорыва, Северо-Западный федеральный округ, [кейса](https://hacks-ai.ru/hackathons/757124) "Алгоритм на страже экономической стабильности". /
> Состав команды: [Дмитрий Куценко](https://github.com/kdimon15), [Никита Романов](https://github.com/KARTASAR), [Давид Джалаев](https://github.com/DavidRomanovizc).

<br>

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![sklearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

<br>

## Содержание
- [Таблица лидеров](#таблица-лидеров)
- [Описание задачи](#описание-задачи)
- [Наше решение](#описание-нашего-решения)

<br>

## Таблица лидеров
![image](https://user-images.githubusercontent.com/91266802/187231269-e566aca0-be90-4888-aeec-7920120fbf32.png)

<br>

## Описание задачи
В рамках данного хакатона участникам предстояло разработать модель, которая сможет быстро адаптироваться к задаче прогнозирования экономических переменных квартальной и месячной периодичности, которые модель не видела до этого.

Обучающая выборка состоит из 69 экономических переменных месячной и 39 переменных квартальной периодичности в период с января 2003 года по декабрь 2015 года.

Тестовая выборка состояла из 4446 файлов в каждом из которых отдельная задача прогнозирования не более чем 10ти временных рядов на не более чем 15 месяцев/5 кварталов.

<img width="865" alt="image" src="https://user-images.githubusercontent.com/91266802/187088928-690163a2-f023-44ba-89c7-8d7792b90634.png">

<br>

## Описание нашего решения

Наша команда разработала уникальный алгоритм, с помощью которого можно предсказать макроэкономические и финансовые переменные. В начале наша модель анализирует временные ряды и делит их на классы для улучшения качества предсказания. Для каждого класса обучена отдельная модель, которая предсказывает соответствующие временные ряды. Финальная модель предсказывает изменение цены, а не саму цену, что позволяет снизить переобучение на небольшом объеме данных.

<img width="708" alt="image" src="https://user-images.githubusercontent.com/91266802/187089122-ef06cb76-0619-4274-9473-c42cd97f3b8c.png">


Стек используемых технологий: библиотеки градиентного бустинга Catboost, XGBoost, библиотека для работы с временными рядам Sktime, а также библиотеки для анализа данных: pandas, matplotlib.

Уникальность нашего решения заключается в том, что мы обучили модель, которая способна определять тип временного ряда и подбирать модель, которая лучше всего подходит для предсказания будущей стоимости на данном временном ряду. Предсказываются изменения временного ряда, а не будущего состояния.

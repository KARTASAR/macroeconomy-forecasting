# Прогнозирование макроэкономических и финансовых переменных
> Решение команды Chill Garage на хакатоне Цифрового Прорыва, Северо-Западный федеральный округ,\
> [кейса](https://hacks-ai.ru/hackathons/757124) "Алгоритм на страже экономической стабильности".
> Разрабатывали: [Дмитрий Куценко](https://github.com/kdimon15), [Никита Романов](https://github.com/KARTASAR), [Давид Джалаев](https://github.com/DavidRomanovizc).

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
<svg width="8272" height="1549" viewBox="0 0 8272 1549" fill="none" xmlns="http://www.w3.org/2000/svg">
<g opacity="0.5" filter="url(#filter0_i_6_2238)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M8272 1032.67L7927.33 946.611C7582.67 860.556 6893.33 688.444 6204 631.074C5514.67 573.704 4825.33 631.074 4136 659.759C3446.67 688.444 2757.33 688.444 2068 573.704C1378.67 458.963 689.333 229.481 344.667 114.741L-0.00012207 0V1549H344.667C689.333 1549 1378.67 1549 2068 1549C2757.33 1549 3446.67 1549 4136 1549C4825.33 1549 5514.67 1549 6204 1549C6893.33 1549 7582.67 1549 7927.33 1549H8272V1032.67Z" fill="url(#paint0_linear_6_2238)"/>
</g>
<defs>
<filter id="filter0_i_6_2238" x="0" y="0" width="8272" height="1553" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feOffset dy="4"/>
<feGaussianBlur stdDeviation="2"/>
<feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
<feBlend mode="normal" in2="shape" result="effect1_innerShadow_6_2238"/>
</filter>
<linearGradient id="paint0_linear_6_2238" x1="10943.9" y1="532.198" x2="10655.3" y2="2775.46" gradientUnits="userSpaceOnUse">
<stop offset="0.390625" stop-color="#00FF29"/>
<stop offset="1" stop-color="#005321"/>
<stop offset="1" stop-color="#13ED6A"/>
</linearGradient>
</defs>
</svg>


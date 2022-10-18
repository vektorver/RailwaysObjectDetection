# RailwaysObjectDetection

Модель Object Detection для обнаружения рабочих, касок и жилеток на железной дороге. 

Предоставлена выборка размером 3221 фотографий. Число классов равно 3 (рабочий, жилет, каска)

Выборка не имеет критических дефектов и хорошо подходит для обучения.

1. Все объекты имеют полный набор данных (x, y координаты центра, высота и ширина)

2. Все объекты имеют размеченный класс

3. Нет разбалансировки объектов по классам. Все объекты появляются приемлемое число раз [7883, 6515, 7973]

4. Допустимое число изображений без искомых объектов. 157 против 22528

5. Координаты центров объектов располагаются с определенной закономерностью. Она обусловлена тем, что в выборке представлены фотографии исключительно с камер видео наблюдения, которые имеют эффект рыбьего глаза. Установлены на приблизительно одинаковой высоте и захватывают приблизительно одинаковый угол обзора

![image](https://user-images.githubusercontent.com/29977757/196367938-e4119bb0-b516-49ae-bb55-ee0cc7636cfc.png)


Модель обучалась на 80 процентах изображений от общей выборки. 20 процентов использовалось для валидации 

Достигнута точность: 

```
class_id = 0, name = 0, ap = 79.41%   	 (TP = 1458, FP = 2526) 
class_id = 1, name = 1, ap = 83.60%   	 (TP = 1185, FP = 1399) 
class_id = 2, name = 2, ap = 97.10%   	 (TP = 1550, FP = 1841) 
```

Модель обучалась несколько раз с разными параметрами в cfg файле. В репозитории приложен файл cfg, который привел модель к наилучшим результатам.

Модель YOLOV4. 

Конфигурационный файл модели был изменен. Указано число классов (3), разрешение изображений (800, 800), а так же число шагов обучения, размер max_batches, число фильтров на выходе сети и др. 

---------

# График обучения сети

![image](https://user-images.githubusercontent.com/29977757/196161975-1617a208-f295-45af-abf5-4e3b2005583b.png)

График обучения сильно колеблется. Стоит отметить, что имеется переобучение у сети. О таком свойстве модели указано в туториалах фреймворка. Модель все равно достигает высоких результатов на тестовой выборке. Алгоритм обучения построен таким образом, чтобы запомнить веса с наилучшим значением на тестовой выборке. 

---------
# Визуализация результатов
Взяты анкоры с вероятностью выше 90 процентов

![image](https://user-images.githubusercontent.com/29977757/196162072-1e838b10-80ed-493f-a861-b376eef4a627.png)
![image](https://user-images.githubusercontent.com/29977757/196368616-edde87fc-e085-4550-ad0f-bcedef07c0c4.png)


---------

В файле main.py создан класс Model, который получает при инициализации конфиг (состоящий из файлов: конфигурации модели, весов модели, информации об обучающих данных, названий классов). Метод predict на вход получает изображение и сохраняет в директорию проекта файл prediction.jpg

Пример запуска функции есть в файле main.py
```
config = {'obj.data': 'obj.data', 
       'cfg':'yolov4-obj.cfg',
       'weights': 'yolov4-obj_best.weights', 
       'thresh': 0.7}
       
model = ObDetModel(config)
model.predict('1657.jpg')
```

Веса можно скачать здесь:

https://drive.google.com/file/d/1-1WlEnwuXrAf3dlufw1Moyxhv3YRunz3/view?usp=sharing

Colab Notebook:

https://colab.research.google.com/drive/1dwRG6LpQ_Cy1XJvLiA3_4FNd9Bwx5PMt?usp=sharing

P.S. Обычно подобного рода проекты я оформляю как сервис и заворачиваю в Docker-контейнер. Решил не делать так в этот раз, потому что этого не требовалось в задании. Кроме того, фреймворк Darknet за счет исполнительного файла сводит необходимость предустановки библиотек к минимуму. Данный репозиторий работает на любой исполнительной машине, где имеется GPU Nvidia (не сильно слабой производительности. Пойдут карты от 1050) с доступными CUDA ядрами и установленными библиотеками видео-карты. 

# Лабораторная работа 1: Основы SQL
##### Выполнил: ***Дьяконов Олег***
---

### Практические задания

- Создать таблицы на основе рисунка 2. Создание должно производится через скрипты.
- Для каждой таблицы создайте не менее пяти записей, самостоятельно определив значения полей.
- Выполнить эксперимент по добавлению некорректных данных в таблицы.
- Описать поведение базы при вводе неправильных данных.
- Обновить описание таблиц, обеспечив контроль корректности вводимых данных.
- Для каждой таблицы разработайте SQL-запросы с условиями отбора данных. Результаты выполнения запросов оформить в виде скриншотов и сохранить итоговый файл лабораторной работы.
---

### Ход выполнения

Работа выполнялась в **sqliteonline.com**

---

## 1 Создание таблиц

- Создал таблицы на основе *рисунка 2*. Скрипт:
```
CREATE TABLE shop (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE NOT NULL,
balance FLOAT NOT NULL
);

CREATE TABLE product (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE NOT NULL,
price FLOAT NOT NULL
);

CREATE TABLE warehouse (
shop_id INTEGER REFERENCES shop(id),
product_id INTEGER REFERENCES product(id),
quantity INTEGER NOT NULL,
PRIMARY KEY (shop_id, product_id)
);
```

- *Скриншоты:*
<img width="1181" height="659" alt="image" src="https://github.com/user-attachments/assets/70d1d557-792f-4d13-bbb7-5d3c90666c16" />


---

# 2 Добавление данных в  таблицы

- ***Для shop:***
```
INSERT INTO shop VALUES (1, 'Пятерочка', 300);
INSERT INTO shop VALUES (2, 'Перекресток', 500);
INSERT INTO shop VALUES (3, 'Магнит', 450);
INSERT INTO shop VALUES (4, 'Лента', 700);
INSERT INTO shop VALUES (5, 'Дикси', 250);
```

- *Скриншот:*
<img width="1194" height="882" alt="image" src="https://github.com/user-attachments/assets/0d154980-e81b-4a9d-8e9f-4ee755d99744" />


- ***Для product:***
```
INSERT INTO product VALUES (1, 'молоко', 100);
INSERT INTO product VALUES (2, 'хлеб', 30);
INSERT INTO product VALUES (3, 'сыр', 200);
INSERT INTO product VALUES (4, 'яблоки', 90);
INSERT INTO product VALUES (5, 'курица', 250);
```

- *Скриншот:*
<img width="1188" height="894" alt="image" src="https://github.com/user-attachments/assets/7b85301c-6453-4898-9d7d-3423b9d1640e" />


- ***Для warehouse:***
```
INSERT INTO warehouse VALUES (1,1,20);
INSERT INTO warehouse VALUES (1,2,15);
INSERT INTO warehouse VALUES (2,3,10);
INSERT INTO warehouse VALUES (3,4,40);
INSERT INTO warehouse VALUES (4,5,12);
```

- *Скриншот:*
<img width="1190" height="1063" alt="image" src="https://github.com/user-attachments/assets/e30717f7-0897-4e90-8788-033ac9abb96f" />


---

## 3 Просмотр таблиц

- ***Для shop:***
```
SELECT * FROM shop;
```

- *Скриншот:*
<img width="1189" height="817" alt="image" src="https://github.com/user-attachments/assets/4dd80e7f-a8dc-4541-8968-ad1d034f47c6" />


- ***Для product:***
```
SELECT * FROM product;
```

- *Скриншот:*
<img width="1197" height="888" alt="image" src="https://github.com/user-attachments/assets/b68859e5-afd9-49c1-9f90-359f463a034f" />


- ***Для warehouse:***
```
SELECT * FROM warehouse;
```

- *Скриншот:*
<img width="1192" height="851" alt="image" src="https://github.com/user-attachments/assets/2f393158-4b2c-4da2-8375-0c8eaff1802e" />


--- 

## 4. Эксперимент с некорректными данными

В ход работы был проведен эксперимент по добавлению некорректных данных.

- ***Нарушение ограничения UNIQUE:***
```
INSERT INTO product VALUES (6, 'молоко', 120);
```

- *Скриншот:*
<img width="1197" height="952" alt="image" src="https://github.com/user-attachments/assets/f518701b-2d0f-4a22-a874-89d71e90ebeb" />


- ***Нарушение ограничения NOT NULL:***
```
INSERT INTO shop VALUES (6, NULL, 100);
```

- *Скриншот:*
<img width="1189" height="927" alt="image" src="https://github.com/user-attachments/assets/1f164847-dd3c-415e-b30d-6211bec31e7c" />


---

## 5. Контроль корректности вводимых данных

Для повышения надежности базы данных добавил проверку корректности данных через **CHECK**, где цена товара не может быть отрицательной

- ***Пример:***
```
CREATE TABLE product (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE NOT NULL,
price FLOAT NOT NULL CHECK (price > 0)
);
```

- *Скриншот:*
<img width="1196" height="900" alt="image" src="https://github.com/user-attachments/assets/9a68e6f9-fcde-40a0-972a-a226e73e2b3e" />
<img width="1195" height="927" alt="image" src="https://github.com/user-attachments/assets/3fb7d8ae-7586-4a36-ae1f-5f3a59b326c0" />



---

## 6. SQL запросы с условиями

В рамках работы были разработаны запросы с условиями отбора данных

- ***Магазины с балансом больше 400:***
```
SELECT * FROM shop
WHERE balance > 400;
```

- *Скриншот:*
<img width="1194" height="747" alt="image" src="https://github.com/user-attachments/assets/93e906cc-d8d5-4cdd-b68a-b4fe7caa2469" />


---

# Вывод

В ходе выполнения лабораторной работы были изучены основные операции работы с реляционными базами данных. Были созданы таблицы, добавлены данные и выполнены SQL-запросы для получения информации. Также был проведен эксперимент по добавлению некорректных данных и изучено поведение базы данных при нарушении ограничений.

В результате работы были получены практические навыки создания и управления базой данных с использованием языка SQL.

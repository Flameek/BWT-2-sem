# Лабораторная работа 2: Основы выборки SQL
##### Выполнил: ***Дьяконов Олег***
---

### Практические задания

- Создайте дополнительную таблицу “Сотрудник” выполнив следующую команду:
```
CREATE TABLE worker (
worker_id INTEGER PRIMARY KEY,
shop_id INTEGER REFERENCES product (id),
name VARCHAR(255),
salary INTEGER NOT NULL,
position VARCHAR(255));
```
- Внесите в таблицу данные.
- К лабораторной работе прилагается файл data.sql. Для импорта данных в среде Jade необходимо нажать на кнопку с тремя вертикальными точками в левом верхнем углу выбрать пункт Import SQL.
- К таблицам напишите запросы операциями группировки и сортировки. Также реализуйте запросы с использованием агрегатных функций для таблицы "Сотрудник".
- Сформируйте запрос, который выводи список сотрудников с указанием названия магазина, должности и зарплаты. Результат отсортировать по названию магазина, должности и зарплаты. Результат сортировать по названию магазина, затем по зарплате по убыванию.
- Составьте запрос, который выводит для каждого магазина: Название магазина, кол-во сотрудников, среднюю зарплату. Результат отсортировать по средней зарплате по убыванию.
- Найдите магазины, где средняя зарплата сотрудников выше 50000. Выведите название магазина и среднюю зарплату. 

---

### Ход выполнения

Работа выполнялась в **sqliteonline.com**

---

## 1. Создание таблиц

В **первой лабораторной работе** были созданы таблицы:
- **`shop`**
- **`product`**
- **`warehouse`**
Теперь мы добавляем таблицу **`worker`**:
-  ***Скрипт:***
```

```

- *Скриншот:*
<img width="1274" height="1130" alt="изображение" src="https://github.com/user-attachments/assets/ae9ca049-553e-4034-bd8d-317c92c3b446" />


---

# 2. Заполнение данными таблицы

- К нашей лабораторной работе прикреплялся файл с данными **`data.sql`**. Импорт осуществился через **sqliteonline.com**
- Была осуществлена **Проверка**:
<img width="1262" height="1280" alt="изображение" src="https://github.com/user-attachments/assets/2e31a898-c36f-4da2-a748-4161b3cdc571" />


---

# 3. Выполнение запросов

#### Запросы с группировкой, сортировкой и агрегатными функциями для таблицы **`worker`**

- ***Количество сотрудников по должностям:***
```
SELECT 
    position,                    
    COUNT(*) AS employee_count   
FROM worker
GROUP BY position                
ORDER BY employee_count DESC;
```

>>> *`GROUP BY` position объединяет всех сотрудников с одинаковой должностью в одну группу.*
>>> *`COUNT()` подсчитывает количество строк в каждой группе.*
>>> *`ORDER BY employee_count DESC` сортирует результат так, чтобы самая многочисленная должность была первой.*

- *Скриншот:*
<img width="1278" height="1085" alt="изображение" src="https://github.com/user-attachments/assets/4086d8d0-cc95-4754-a878-97a78d105782" />


- ***Средняя зарплата по должностям:***
```
SELECT 
    position,
    AVG(salary) AS avg_salary
FROM worker
GROUP BY position
ORDER BY avg_salary DESC;
```

>>> *`AVG(salary)` вычисляет среднее арифметическое зарплат в группе.*

- *Скриншот:*
<img width="1227" height="1280" alt="изображение" src="https://github.com/user-attachments/assets/c92b5120-4bc2-41f8-a613-a95c83745c6b" />


- ***Минимальная и максимальная зарплата в каждом магазине***
```
SELECT 
    shop_id,
    MIN(salary) AS min_salary,   -- минимальная зарплата в магазине
    MAX(salary) AS max_salary    -- максимальная зарплата в магазине
FROM worker
GROUP BY shop_id;
```

>>> *Группируем сотрудников по `shop_id`, чтобы для каждого магазина получить свои значения.*

- *Скриншот:*
<img width="1270" height="1280" alt="изображение" src="https://github.com/user-attachments/assets/63c89de5-827a-451e-9be8-91b73327bb2b" />


- ***Список сотрудников с названием магазина, должностью и зарплатой***
```
SELECT 
    shop.name AS shop_name,
    worker.name AS employee_name,
    worker.position,
    worker.salary
FROM worker
JOIN shop ON worker.shop_id = shop.id
ORDER BY shop_name, worker.salary DESC;
```

>>> *`JOIN` объединяет таблицы `worker` и `shop` по полю `shop_id`.*
>>> *`ORDER BY shop_name, worker.salary DESC` сортирует по названию магазина (алфавит), а внутри каждого магазина - по убыванию зарплаты.*

- *Скриншот:*
<img width="1275" height="1280" alt="изображение" src="https://github.com/user-attachments/assets/f8806c24-54e0-4a68-9e8e-87aae5d2442b" />


- ***Для каждого магазина - название, кол-во сотрудников и средняя зарплата***
```
SELECT 
    shop.name AS shop_name,
    COUNT(worker.worker_id) AS employee_count,
    AVG(worker.salary) AS avg_salary
FROM shop
LEFT JOIN worker ON shop.id = worker.shop_id
GROUP BY shop.id, shop.name
ORDER BY avg_salary DESC;
```

>>> *`LEFT JOIN` гарантирует, что в результат попадут все магазины, даже если в них нет сотрудников.*
>>> *`COUNT(worker.worker_id)` игнорирует `NULL`, поэтому магазины без сотрудников получат 0.*
>>> *`AVG(worker.salary)` вычисляет среднюю зарплату, пропуская `NULL`.
>>> *Сортировка по убыванию средней зарплаты показывает магазины с самой высокой оплатой труда.*

- *Скриншот:*
<img width="1224" height="1280" alt="изображение" src="https://github.com/user-attachments/assets/a20391dd-a3a6-445e-b4f0-13602927c049" />


- ***Магазины со средней зарплатой выше 50000**
```
SELECT 
    shop.name AS shop_name,
    AVG(worker.salary) AS avg_salary
FROM shop
JOIN worker ON shop.id = worker.shop_id
GROUP BY shop.id, shop.name
HAVING AVG(worker.salary) > 50000
ORDER BY avg_salary DESC;
```

>>> *`HAVING` применяется после группировки и позволяет фильтровать группы по агрегированному значению (здесь - средняя зарплата).*
>>> *`JOIN` используется, чтобы исключить магазины без сотрудников (в них `avg_salary` был бы `NULL` и не прошел бы условие).*
>>> *`AVG(worker.salary)` вычисляет среднюю зарплату, пропуская `NULL`.

- *Скриншот:*
<img width="1267" height="1280" alt="изображение" src="https://github.com/user-attachments/assets/b4d52906-75c8-4b53-aea7-9630d0a17341" />


---

# Вывод

В ходе лабораторной работы были освоены основные конструкции SQL для выборки данных.

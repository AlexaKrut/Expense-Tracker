# Трекер расходов
Идея проекта [Expense_Tracker](https://roadmap.sh/projects/expense-tracker) была взята с [roadmap.sh](https://roadmap.sh/)

## Описание
Трекер расходов - это простое приложение командной строки, которое помогает пользователям управлять своими финансами, позволяя добавлять, удалять и просматривать расходы. Приложение также предоставляет сводную информацию о расходах, включая возможность фильтрации по месяцам.

## Установка
Для установки и запуска приложения выполните следующие шаги:

1. Склонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd <папка_проекта>
   ```
2. Посмотрите справку проекта
   ```bash
   python3 expanse-tracker.py -h
   ```
3. Запустите программу
   ```bash
   python3 expanse-tracker.py <параметры>

## Использование
Приложение запускается из командной строки. Вот несколько примеров команд:

1) Добавление расхода:
```bash
expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)
```
2) Просмотр всех расходов:
```bash
expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
```
3) Получение сводной информации о расходах:
```bash
expense-tracker summary
# Total expenses: $30
```
4) Удаление расхода:
```bash
expense-tracker delete --id 1
# Expense deleted successfully
```
5) Сводная информация о расходах за конкретный месяц:
```bash
expense-tracker summary --month 8
# Total expenses for August: $20
```

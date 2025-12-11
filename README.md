Перед запуском должны быть установлены:
 - Docker
 - Docker Compose

Проверить: docker --version

Запуск через Docker Compose: docker-compose build

Запуск проекта: docker-compose up -d

Сервис доступен по адресу http://localhost:8880

Остановка проекта: docker-compose down

## Структура файла .env
RETAILCRM_API_KEY=YOUR_KEY

RETAILCRM_API_URL=https://{subdomain}.retailcrm.ru

LOG_LEVEL=INFO

## Основные моменты реализации

1. Асинхронная интеграция с RetailCRM через HTTPX
2. Единый интеграционный интерфейс ICRM, который является абстрактным слоем взаимодействия между приложением и внешними CRM-системами
2. Интерфейс обработчика
2. Валидация данных через Pydantic v2
3. Обработка ошибок RetailCRM
4. Логирование


## Моменты, которые вызвали трудности

1. Описывание Response pydantic моделей (отличающий стиль именований)
2. Невнимательность
3. Особенности формата запросов RetailCRM

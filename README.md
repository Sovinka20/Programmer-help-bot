# Telegram Bot Reference Guide

The project is aimed at quickly obtaining the necessary, periodically requested information. This bot provides reference information based on keywords and uses a PostgreSQL database to store the information.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Development](#development)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sovinka20/programmer_help_bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd programmer_help_bot
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Setup GitHub Actions Secrets

To run the bot, you need to set up the following secrets in GitHub Actions:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `DB_NAME`: The name of the PostgreSQL database.
- `DB_USER`: The username for the PostgreSQL database.
- `DB_PASSWORD`: The password for the PostgreSQL database user.
- `DB_HOST`: The host of the PostgreSQL database (e.g., `localhost`).

## Usage

Describe how to use your project. Examples of commands, scripts, or API.

```bash
python bot.py
```

## Testing

Describe how to run tests.

```bash
pytest
```

## Development

If you want to contribute to the project, follow these steps:

1. Fork the project.
2. Create a new branch for your feature:

   ```bash
   git checkout -b your-feature-branch
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Description of your changes"
   ```

4. Push your changes to your fork:

   ```bash
   git push origin your-feature-branch
   ```

5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

# Бот-помощник программиста

Проект направлен на быстрое получение необходимой, периодически запрашиваемой информации. Этот бот предоставляет справочную информацию по ключевым словам и использует базу данных PostgreSQL для хранения информации.

## Оглавление

- [Установка](#установка)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Разработка](#разработка)
- [Лицензия](#лицензия)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Sovinka20/programmer_help_bot.git
   ```

2. Перейдите в директорию проекта:

   ```bash
   cd programmer_help_bot
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

### Настройка GitHub Actions Secrets

Для работы бота необходимо настроить следующие секреты в GitHub Actions:

- `TELEGRAM_BOT_TOKEN`: Токен вашего Telegram-бота.
- `DB_NAME`: Имя базы данных PostgreSQL.
- `DB_USER`: Имя пользователя базы данных PostgreSQL.
- `DB_PASSWORD`: Пароль пользователя базы данных PostgreSQL.
- `DB_HOST`: Хост базы данных PostgreSQL (например, `localhost`).

## Использование

Опишите, как использовать ваш проект. Примеры команд, скриптов или API.

```bash
python bot.py
```

## Тестирование

Опишите, как запустить тесты.

```bash
pytest
```

## Разработка

Если вы хотите внести свой вклад в проект, следуйте этим шагам:

1. Сделайте форк проекта.
2. Создайте новую ветку для вашей фичи:

   ```bash
   git checkout -b имя-вашей-фичи
   ```

3. Внесите изменения и зафиксируйте их:

   ```bash
   git commit -m "Описание ваших изменений"
   ```

4. Отправьте изменения в ваш форк:

   ```bash
   git push origin имя-вашей-фичи
   ```

5. Создайте pull request.

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).

# DeliveryHero Case URL Shortener
## Installation

Run with docker

```sh
docker-compose run web
```
Migrate migrations

```sh
docker-compose exec web python manage.py migrate
```

## Endpoints

| Method | URI                                | Example Body                               | 
|--------|------------------------------------|--------------------------------------------|
| POST   | http://localhost:8000/             | {"original_url":"https://www.google.com/"} |
| GET    | http://localhost:8000/{short_code} |
| GET    | http://localhost:8000/list/        |



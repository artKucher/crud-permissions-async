# CRUD users + async ordering

---
Видеодемонстрация по [ссылке](https://drive.google.com/file/d/1Hqp2KfRDODbona7rVp3kPO07AItofnAv/view?usp=sharing)

Стек:
- FastAPI
- SQLModel(Pydantic+SQLAlchemy)
- SQLite
- Docker

Учётные данные стандартного пользователя: ***admin / admin***

# При перезапуске проекта база данных полностью очищается и стандартный пользователь создаётся заново


## Запуск в докере

1) Сбилдите контейнер
```
make build
```
2) Запустите проект
```
make run
```
3) Убедитесь, что сервис запустился корректно
```
make logs
```
4) Документация http://localhost:5003/docs
5) Для запуска фронтенда откройте файл frontend/index.html в браузере

## Запуск в venv

1) Подготовьте окружение
```
python3 -m venv venv
source venv/bin/activate
pip install -r main_service/requirements.txt
```
2) Запустите проект
```
cd main_service
python main.py
```
4) Документация http://localhost:5003/docs
5) Для запуска фронтенда откройте файл frontend/index.html в браузере
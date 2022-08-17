# CRUD users + async ordering

---
User flow demonstration on [link](https://drive.google.com/file/d/1Hqp2KfRDODbona7rVp3kPO07AItofnAv/view?usp=sharing)

Stack:
- FastAPI
- SQLModel(Pydantic+SQLAlchemy)
- SQLite
- Docker

Default user: ***admin / admin***

# Database fully restores and default user recreates on every project restart


## Running in docker

1) build the image
```
make build
```
2) run containers
```
make run
```
3) Make sure it was started correct
```
make logs
```
4) Swagger documentation http://localhost:5003/docs
5) For running frontend open ```frontend/index.html``` in browser

## Running in venv

1) Prepare environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r main_service/requirements.txt
```
2) Run the project
```
cd main_service
python main.py
```
4) Swagger documentation  http://localhost:5003/docs
5) For running frontend open ```frontend/index.html``` in browser
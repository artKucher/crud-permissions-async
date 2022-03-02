build:
	docker-compose -f docker-compose.yml build
run:
	docker-compose -f docker-compose.yml up -d
down:
	docker-compose -f docker-compose.yml down
logs:
	docker-compose -f docker-compose.yml logs --tail=10 -f main-service
restart:
	docker-compose -f docker-compose.yml restart main-service
exec:
	docker-compose -f docker-compose.yml exec main-service /bin/bash

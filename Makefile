NAME=promotions-automail
VERSION=1.0.0
IMAGE=${NAME}:${VERSION}

# build container
build:
	docker build -f docker/Dockerfile -t ${IMAGE} .

# run container
run:
	docker run \
		--name ${NAME} \
		--volume $(shell pwd)/config.yml:/files/config.yml \
		--detach \
		${IMAGE}

stop:
	docker stop ${NAME}
	docker rm ${NAME}

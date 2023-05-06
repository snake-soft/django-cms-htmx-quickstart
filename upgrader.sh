#!/bin/sh

while [ "$UPGRADE" = true ]
do 
	if [ "$UPGRADE_CI" = true ]
	then
		git reset --hard
		git pull
	fi
	docker-compose --profile upgrade pull
	docker-compose --profile upgrade up -d
	sleep ${UPGRADE_INTERVAL:-60}
done

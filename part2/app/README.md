# Application flask-redis v1

Une application qui affiche le nombre de visites depuis sa mise en service. La valeur est lue et incrémentée sur le serveur Redis.



## Remarques

- L'application est exposée sur le port 5000

- L'application utilise la variable d'environnement REDIS_SERVICE (à définir dans K8s)



### Endpoints

/ 	affiche le nombre de 'hits' réalisés sur l'application depuis sa mise en service



### Version

La v1 fonctionne normalement.
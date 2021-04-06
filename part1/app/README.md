# Application hello-world

Une application qui permet de tester l'accès, la santé d'une application et les volumes éphémères.



## Remarques

- L'application est exposée sur le port 5000



### Endpoints

/					affiche un message hello world et spécifie le hostname du conteneur

/health		 permet de tester la santé de l'application; retourne une erreur 500 une fois sur deux

/text		     affiche le contenu du fichier /usr/share/html/text.txt
# Part 2 / Deploying an application
Here you will get to build a deployment by yourself and learn about more advanced notions.
In order to do that, you will use the Docker images available on the `sejren/flask-counter-app` repository, which is a basic Flask-Redis application.

1. Create a deployment for the redis image and expose it.
2. Create another deployment using the flask-counter image (version 1). Don't forget to define the `REDIS_SERVICE` env var.
3. Create an internal service to service your flask application. Create an Ingress on top of this service with the name `tp.local`
4. Create a secondary application (for example using the `sejren/tp-kubernetes` image that we previously used)
5. Autorize HTTPS trafic to your application and store your certificate in a Secret.
6. Enable autoscaling
7. Update your flask app by changing the image to `sejren/flask-counter-app:v2`. There's an error in the application, so it should fail.
8. Revert changes.
9. Add a readiness probe to your deployment to ensure that this won't happen again.
10. Update again, ans see how Kubernetes reacts.

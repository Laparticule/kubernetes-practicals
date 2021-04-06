# Part 1 / Introduction
Here, you will learn about the main components of K8s and its syntax.
In order to do that, you will use the Docker images available on the `sejren/tp-kubernetes` repository. This is a web application written in Flask and listening on port 5000 (you can find it in the app/ folder as well)

## Your first deployment
1. List your resources with `kubectl get all`
2. Create a deployment with `kubectl create deployment hello-world --image=sejren/tp-kubernetes --replicas=3`
3. Expose your application with `kubectl expose deployment hello-world --type=NodePort --port=80 --target-port=5000`
4. List your resources again, and try to access your application using curl
5. Delete everything using `kubectl delete all --all `

## Pods
1. Create a Pod using `kubectl run pod1 --image=sejren/tp-kubernetes`
2. Write a YAML file describing another pod, then use the `kubectl apply -f pod.yaml` to create the Pod
3. Make sure that your pods have been created correctly using `kubectl get` and `kubectl describe`
4. Use `kubectl logs` and `kubectl exec` to confirm that everything works correctly without warnings or errors
5. Try to access your Pod from inside the cluster using curl
6. Add a label to one of your pods using either `kubectl edit` or the configuration file
7. Use selectors to list only the pods who have a specific label
6. Delete both Pods

## Controllers
1. Create a ReplicaSet with 3 replicas
2. Delete one of the Pods and see what happens
3. Edit your ReplicaSet to increase or decrease the number of replicas
4. Add a liveness probe to your ReplicaSet. The application has been configure so that /health randomly returns errors.
5. Create a Job that acts as a timer
6. Once it works, simply remove the liveness probe from your ReplicaSet configuration

## Services
1. Create a ClusterIP pointing to your ReplicaSet
2. Access your application multiples from the inside of your cluster
3. Create a NodePort pointing to your ReplicaSet
4. Access your application both from the inside of your cluster and from the outside
5. Delete everything in your cluster

## Volumes
1. Create a Pod with two containers and one volume (EmptyDir). One of the containers will write data to the volume, and the other one will serve the information.
Write your data to /usr/share/html/text.txt and then use the /text endpoint to print what's in the file.
2. Recreate your Pod. Notice that your data has been lost.
3. Recreate the example using a HostPath.
4. Notice that your data is now persistent, even though it's an imperfect solution

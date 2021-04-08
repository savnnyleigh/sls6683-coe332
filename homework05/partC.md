# Part C


## To Create the Pod

```bash
kubectl apply -f deployment-C.yml
```
We should then see 

```
deployment.apps/hw05-deployment
```

## Pods in deployment and IP Addresses

The command:

```bash
kubectl get pods -o wide
```
Gave the results (formatted for answer, different form in command line):


| Pods in Deployment  | IP address |
| ------------- | ------------- |
| hw05-deployment-565979bd6-7gkss | 10.244.7.116  |
| hw05-deployment-565979bd6-m9l5d | 10.244.3.124  |
| hw05-deployment-565979bd6-xjvx4 | 10.244.6.161  |


## Pod logs

Used the commands: 

```bash
kubectl logs hw05-deployment-565979bd6-7gkss
kubectl logs hw05-deployment-565979bd6-m9l5d
kubectl logs hw05-deployment-565979bd6-xjvx4
```
Gave the results:

```
Hello, Savannah from IP 10.244.7.116!
Hello, Savannah from IP 10.244.3.124!
Hello, Savannah from IP 10.244.6.161!

```


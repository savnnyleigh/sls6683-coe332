# Part A


## To Create the Pod

```bash
kubectl apply -f pod-A.yml
```
We should then see 

```
pod/hello created
```

## How to get the pod with the appropriate selector

```bash
kubectl get pods --selector "greeting"
```
or

```bash
kubectl get pods --selector "greeting=personalized"
```

## Pod Logs

The command:

```bash
kubectl logs hello
```
Gave the result:

```
Hello,
```
It was the output I expected, because we did not assign any variable to NAME so there wasn't anything for the system to put there.

## To delete the pod

Use the command: 

```bash
kubectl delete pods hello
```
Gave the result:

```
pod "hello" deleted
```

# Part B


## To Create the Pod

```bash
kubectl apply -f pod-B.yml
```
We should then see 

```
pod/hello-name created
```

## Pod Logs

The command:

```bash
kubectl logs hello-name
```
Gave the result:

```
Hello, Savannah!
```

## To delete the pod

Use the command: 

```bash
kubectl delete pods hello-name
```
Gave the result:

```
pod "hello-name" deleted
```


@echo off
echo Stopping Kubernetes services...
.\kubectl.exe delete -f deployment.yaml
.\kubectl.exe delete -f service.yaml

echo.
echo Stopping Minikube...
.\minikube-windows-amd64.exe stop

echo.
echo Cleanup complete!
pause
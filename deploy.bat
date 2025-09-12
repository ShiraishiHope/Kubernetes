@echo off
echo Starting Minikube...
.\minikube-windows-amd64.exe start --driver=docker

echo.
echo Deploying application...
.\kubectl.exe apply -f deployment.yaml
.\kubectl.exe apply -f service.yaml

echo.
echo Waiting for deployment to be ready...
timeout /t 15 /nobreak >nul

echo.
echo Opening application...
.\minikube-windows-amd64.exe service todo-app-service

echo.
echo Deployment complete! Keep this terminal open for the service tunnel.
pause
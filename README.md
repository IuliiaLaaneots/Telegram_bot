# Telegram_bot

In order to make this bot working please follow the steps:
1. Clone the repository to your local computer. You can use "git clone <link_to_repo>" or download zip. 
2. If you do not have Docker, please install it.
3. Navigate yourself to the folder where Dockerfile and bot.py are located and run:
   ```
   docker build -t telegram-bot .
   ```
   This would build the image that you would need to push to the image registry in order to run it in the cloud.
5. In order to test the bot locally, you can run the command:
```
  docker run -e TELEGRAM_TOKEN=<copy-here-your-token> telegram-bot
  ```
Token is passed to the container as enviromental parmeter, as it is a good practise not to use it in the hardcoded way. 

6. In order to run this image in Aruze, i assume the easiest way would be to run it using Azure Container Instances:
   - **Step 1**: Push Your Docker Image to a Container Registry (Using Azure Container Registry):
-- Create an Azure Container Registry:
```
az acr create --resource-group yourResourceGroup --name yourRegistryName --sku Basic
```
-- Login to Azure Container Registry:
```
az acr login --name yourRegistryName
```
-- Tag your Docker image:
```
docker tag your-image-name:tag yourRegistryName.azurecr.io/your-repository-name:tag
```
-- Push the Docker image:
```
docker push yourRegistryName.azurecr.io/your-repository-name:tag
```
  - **Step 2**: Create an Azure Container Instance
Once your image is in a registry, you can create a container instance:
-- Log in to Azure:
```
az login
```
-- Create a resource group (if you don't have one):
```
az group create --name myResourceGroup --location eastus
```
-- Run your Docker image in Azure Container Instances:
```
az container create --resource-group myResourceGroup \
  --name mycontainer \
  --image yourRegistryName.azurecr.io/your-repository-name:tag \
  --dns-name-label myapp --ports 80 \
  --registry-login-server yourRegistryName.azurecr.io \
  --registry-username $(az acr credential show --name yourRegistryName --query username --output tsv) \
  --registry-password $(az acr credential show --name yourRegistryName --query passwords[0].value --output tsv) \
  --environment-variables TELEGRAM_TOKEN=your_token_here
```
-- Check the status of your container:
```
az container show --resource-group myResourceGroup --name mycontainer --query instanceView.state
```

**Please note that in some cases it might need administrative rights in order to run the commands.**

   

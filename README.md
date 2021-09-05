# demo-prototype
The basics

## The landing page structure
* This assumes that the QR code carries the unique identifier of an asset
* Each page links to a 3 seperate views: <Asset> Report, Site Safety Report, <Asset> Service Docs

### Configuring flask run (Powershell)
* cd vir_env_flask\Scripts
* .\activate
* cd ..\Demo-Application\flaskr
* $env:FLASK_APP = "app"
* $env:FLASK_ENV = "development"
* flask run
#To Do:
* Create .env file to remove manually configuration of environment variables within powershell

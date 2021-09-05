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

#### Dependency
* pip install qrcode
* pip install PilImage
* *To Do:
* Create .env file to remove manually configuration of environment variables within powershell

##### Secure tunnel (step by step)
* download/install ngrok
* CMD-Powershell : ngrok http 5000
* Copy generated port forwarding address into 'input_data' variable of genQR_local.py
* CMD-Powershell python genQR_local.py 
* scan QR, verify that landing_menu.html renders

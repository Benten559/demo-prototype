# demo-prototype
All commands written with directions were used with Windows Powershell
Make sure you have flask installed.


* Mobile/Web 
  I've been testing this by using my machine to host it. It's quick for trying it out on my phone.
  Port forwarding of this application is handled with ngrok
  During this development phase ngrok can handle 2 hours of serving files from your local 5000 with simple traffic restriction.

* Starting it up, **flask run**
  Once all dependencies are installed, to use the framework you begin the development server with the cmd.
  If all the environment variables are set correctly it will target the file app.py and its styling/webpage folders.



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

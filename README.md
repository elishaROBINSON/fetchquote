# fetchquote
prerequisite
> have latest version of docker and docker-compose
> user should have access to it https://docs.docker.com/engine/install/linux-postinstall/

initial setup
create a file **.env** file in the path **fetchquote/fetchquote/.env**
content should be like this 

"""

secrect_key_api=**#alphavantage-api-key#**

"""

to run the code clone the repo 
  
  ```
  $git clone https://github.com/elishaROBINSON/fetchquote.git
  $cd fetchquote
  $docker-compose up --build
```
after services are started go to browser on this url
http://localhost:8000/api/v1/quotes

to access the api and test its features with GET and POST methods

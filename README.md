# task_management

How to run the code?

This application is dockerized so it can accessed by below commands:

1. clone the repo(git clone ....)
2. Build the docker image
    docker build -t fastapi:latest .
3. Run the container
    docker run -d --name fastapicontainer -p 80:80 fastapi:latest
4. Access the swagger page under below url
    http://0.0.0.0/docs
   

There are 4 APIs to consume for GET, POST, PUT and DELETE operations

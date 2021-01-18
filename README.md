##  Plotly dashboard with postgress backend: 

### Use it:  
The following step are specific of my set up on wsl.

- activate conda env: source activate base 
- docker-compose build 
- docker-compose up -d
- check docker-compose ps and docker-compose logs to make sure that the services started correctly
- run jupyter notebook that is injecting data to postgressql
- have a look at the app at localhost:80

### Goal:
the goal of this repo is for me to tinkering a bit with dash and docker-compose so needs to be considered a personal PoC. 

### What I learned/useful things: 
- docker compose details and features
- dash basic template with update for future needs
- docker compose networking (https://docs.docker.com/compose/networking/)

### What I would do differently in production:
- hosting postgresql in docker is not a great idea for a production env unless you are sure it will always be a small DB.
(https://vsupalov.com/database-in-docker/)
- refactor dash code and likely not use pandas for the data retrieval
- have a more meaningful plot :)
- reevaluate size of dash's app docker container
- use secrets and dont hardcode env variables


# Grunnleggande Docker - Demo applikasjon og øvelser

## Applikasjonsoppsett
Applikasjonen er en relativt enkel python applikasjon som henter data frå en postgres database. Formålet er å gi en demo applikasjon som en kan enkelt sette opp med Docker. 

## Øvelser 
1. Opprette Dockerfile.
2. Bygg docker image. Sett tag "latest".
3. Lag en ny tag for eksistande docker image. Kall den "1.0.0". 
4. Applikasjonen køyrer default på port 5000 inne i containeren. Bruk port mapping til at den blir tilgjengelig på 8080 på hosten. 
5. Sjekk ut branchen 'create-dockerfile' og lag et image med den Dockerfila. Sett UID=2000 og GID=2000 når du bygger. 
6. Opprett en docker-compose.yml til å bygge og deploye både web applikasjonen og en tilhørande Postgres database. 
7. Start applikasjonen og databasen med docker compose. 
8. Finn IDen til webapp containeren og åpne et shell i den mens den køyrer. 
9. Finn ID til brukeren som køyrer containeren. 

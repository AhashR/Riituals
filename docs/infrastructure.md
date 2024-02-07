## Infrastructuur SAAS oplossing.

De SAAS oplossing zal in de cloud gaan draaien. Maar wat is nu `de cloud`? Deze term wordt voor bijna alles wat tegenvoordig op een scherm ziet en niet van een vooraf geinstalleerde applicatie af komt.

Je bouwt dit blok zelf een SAAS oplossing met behulp van Flask en een database. Om die beschikbaar te stellen aan gebruikers, zul je als team moeten bepalen welke infrastructuur daarvoor geschikt is. De keuze komt voort uit een analyse van behoeften (technische requirements analyse) en een keuze die je maakt daaruit met behulp van de MOSCOW methode. Uiteindelijk koppel je die analyse aan de technische mogelijkheden die de twee aangeboden opties bieden.

Met deze stappen voldoe je aan Infrastructuur Analyse en Infrastructuur Ontwerp.

## Keuze opties

De technische keuze die te maken is bevat grofweg 2 opties
1. De cloud oplossing met Docker als techniek. De docker containers worden met CI/CD in Gitlab gebouwd en gehost op de hva-fys.nl cloud. In dit project is al een docker compose bestand mee geleverd met een vergelijkbare opzet die elk teamlid op de eigen ontwikkelmachine kan draaien.
2. Een eigen Debian 11 server. Op die server kan een team zelf software installeren, opslag regelen en meer. De specificaties worden separaat aangeboden.

Beschrijf in detail de technische mogelijkheden van deze twee opties. Doe dit als team en koppel het resultaat aan de Moscow tabel met requirements.

## Analyse technische mogelijkheden infrastructuur
Je bouwt zelfstandig de portainer/traefik containers op je eigen laptop. Gebruik de meegeleverde `infra-docker-compose.yml`. Bespreek de vragen "Wat ga ik leren"uit de learning story met je medestudenten en vervolgens met een expert. Neem naar de expert in ieder geval de netwerk tekening mee. Maak een tekening volgens de geldende normen van deze infrastructuur!
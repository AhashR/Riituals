## BIM Blok 3

[[_TOC_]]

## Opdrachtomschrijving

Dit is het project voor de leerroute BIM in blok 3 (2023 - 2024).

## Wat je gaat maken

In blok 1 heb je als trainee bij ZMARD gewerkt aan Dokkie. 
In het tweede blok ben je uitgedaagd om als ondernemer samen met een andere student een zogenaamde Software as a Service (SaaS) oplossing te bedenken en te
bouwen voor kleinere bedrijven. Na een kort onderzooek had je het idee welke je hebt uitwerkt in een business plan. Gelijktijdig heb je een “Minimum Viable Product”, gebouwd dat je gebruikt hebt om feedback te krijgen van potentiële klanten. Het blok is afgesloten met een Dragon's Den meeting.

In het tweede semester (blok 3 en 4) werk je in een team van zo'n 4 studenten aan een project waarbij je een SAAS oplossing ontwerpt en bouwt. Dit kan zijn het ontwikkelen van een SaaS product voor ons eigen bedrijf ZMARD; een nieuw project voor een externe opdrachtgever of een project dat je als team zelf hebt bedacht en succesvol hebt “gepitched” in blok 2.

## Wat ga je leren?
Dit blok ligt de focus vanuit de leerroute op Organisatie Processen. Welk proces gaat jullie product ondersteunen? Je leert dit proces in kaart te brengen en met een opdrachtgever te communiceren. Verder borduur je voort op alle techniek die je al kent. Je verdiept je kennis op het vlak van Software en Gebruikersinteractie. Je apolicatie bouw je weer met Flask. Extra dit blok is ook Infrastructuur. Je SAAS oplossing moet namelijk ook ergens live komen te staan.
Dit blok ga je ook in een echt SCRUM team werken. Dus verdiep je je kennis over samenwerken, de sprintplanning en kwaliteitscontrole.

## Learning stories en User stories

Tijdens dit blok 2 project werk je weer aan learning stories. Daarin staan de te leren vaardigheden en competenties binnen dit project. Ze geven je houvast bij wat je moet leren. Je vindt ze samen met de user stories onder `Issues > Boards > Back log. 
<br>In dit blok ben jezelf verantwoordelijk voor het opstellen van de user stories maar voor sprint 1 zijn wel enkele user stories gedefinieerd ter inspiratie. Iedere user story bevat een aantal acceptatiecriteria en taken, die je houvast geven bij het bouwen.

Wat is een user story ook alweer? Op [scrumguide.nl](https://scrumguide.nl/user-story/) vind je de volgende definitie: “Een User Story is een korte beschrijving (Story) van wat een gebruiker (User) wil. User Stories worden gebruikt bij het ontwikkelen van producten of software binnen Agile raamwerken, waaronder Scrum. Een User Story bestaat uit enkele zinnen waarin staat wat de gebruiker van het product moet / wil doen. Een User Story is eigenlijk weinig gedetailleerd en zou moeten kunnen passen op een post-it. Via de User Story heeft de gebruiker invloed op het ontwikkelen van een systeem of product en uiteindelijk de functionaliteit ervan.”

Een user story noteer je volgens een vast format: _Als … (soort gebruiker) wil ik … (feature/actie), zodat … (doel/voordeel).<br>
Een voorbeeld van een user story: _“Als gamer wil ik met mijn ruimteschip kunnen schieten als ik op de spatiebalk druk, zodat ik vijandige aliens kan uitschakelen.”_

## Milestones en sprintboard

- Je werkt in zogeheten sprints. Tijdens een sprint selecteer je de learning stories en de user stories van de Product Backlog die je wil gaan oppakken en afronden in 2 of 3 weken (de duur van een sprint in deze opdracht). In totaal zijn er 3 sprints. Om een user story of learning story toe te wijzen aan een sprint wijs je deze toe aan een Milestone. Dit kun je doen bij de eigenschappen van een issue. Je kan hiervoor ook het board Sprint 1 gebruiken.
- Onder Issues > Milestones > Sprint 1 kun je de burndown van de eerste sprint zien, wat er voor de sprint gepland staat, waar je mee bezig bent en wat af (done) is. 
- Sprint 1, duurt 2 weken en loopt van 5 februari t/m 16 februari 2024;
- Sprint 2, duurt 3 weken en loopt van 19 februari t/m 8 maart 2024;
- Sprint 3, duurt 3 weken en loopt van 11 maart t/m 29 maart 2024.
- Boards
  - Onder de pagina `Issues > Boards `(te vinden via de balk links 👈🏽) vind je onder andere de volgendev boards:
    - Product backlog met alle user stories en learning stories;
    - Sprint 1.

Om een user story toe te wijzen aan een sprint wijs je deze toe aan een `Milestone`. Dit kun je doen bij de eigenschappen van een user story Zie hiervoor wederom de pagina `Issues`.  het eind van een sprint moet er altijd een bruikbaar product zijn voor de eindgebruiker. User stories die niet af zijn gaan door naar de volgende sprint. Test een user story dus goed voordat je deze op closed zet!

## Definition of Done (DoD)

Binnen scrum dient iedere user story te voldoen aan een zogenaamde Definition of Done (DoD). Door het opstellen en aanhouden van een Definition Of Done, zorg je ervoor dat het werk wat je aflevert ook daadwerkelijk gebruikt kan worden. Als je een user story af hebt zet je 'm in _Verify_ en controleer je of deze voldoet aan de _Definition of Done_ (zie hieronder). Pas als dat in orde is kun je de user story op _Done_ zetten.

- [ ] Alle acceptatiecriteria van de betreffende user story zijn afgevinkt.
- [ ] Je hebt volgens de HBO-ICT werkstandaarden gewerkt (Agile, GitLab, sprint boards, sprint planning, HBO-ICT conventions etc.)
- [ ] Het werk is technisch gedocumenteerd in het Engels en relevant voor collega-ontwikkelaars. Denk o.a. aan ERD, UML, testen en testresultaten.
- [ ] Het leerproces is beschreven in Standaardnederlands.
- [ ] Het werk is gereviewd door een peer.
- [ ] Het UX/UI gedeelte van de applicatie voldoet aan het Think-Make-Check (TMC) principe.
- [ ] De code is functioneel getest op fouten.
- [ ] De code werkt zonder fouten bij normaal gebruik.
- [ ] De webapplicatie dient zowel op mobiele- als desktop-apparaten gebruikt te kunnen worden.

## Kwaliteitscriteria

Voor het bouwen van deze opdracht heb je 3 sprints de tijd. Aan het einde van die periode moet je applicatie aan een aantal verwachtingen voldoen. We noemen dit de kwaliteitscriteria. Voor dit blok zien de kwaliteitscriteria er als volgt uit:

| Nr | Kwaliteitscriteria | HBO-i model |
|----|--------------------|-------------|
| K1 | Je hebt object georiënteerde software gemaakt die samenwerkt met een database. | S-O, S-R, S-MC |
| K2 | Je hebt de wensen en behoeften van gebruikers verwerkt in een goed doordacht prototype. | G-A, G-O, G-R |
| K3 | Je hebt een infrastructuur ontworpen en gebouwd volgens de gegeven specificaties. | I-O, I-R, I-MC |
| K4 | Je kan eenvoudig(e) organisatieprocessen, gegevensstromen, databehoeften en procesbesturing analyseren | O-A |
| K5 | Je kan een eenvoudig(e) organisatieproces, organisatie, gegevensstroom, databehoefte en procesbesturing ontwerpen | O-O |

## Gedragscriteria

Om een IT-project succesvol op te leveren, is het noodzakelijk dat je leert om je als een professional te ontwikkelen. Je hebt hiervoor vaardigheden nodig, die we binnen het HBO 'professional skills' noemen. Voor dit project dient je gedrag aan de volgende criteria te voldoen:

| Nr | Gedragscriteria | HBO-i model |
|----|-----------------|-------------|
| G1 | Je ontwikkelt je op persoonlijk vlak en blijft leren. | PL-O, PL-PO |
| G2 | Je werkt constructief samen in een team. | DI-C, DI-S |
| G3 | Je werkt planmatig en volgens gegeven aanpak aan een project. | TO-I, TO-M |

## Lesmateriaal

In de **learning stories** en **user stories** staan verwijzingen naar het lesmateriaal.

## HBO-i

_Binnen deze opdracht ligt de focus op de volgende beroepstaken:_

- Software ontwerpen (S-O) : niveau 1
- Software realiseren (S-R) : niveau 1
- Software manage & control (S-MC) : niveau 1
- Gebruikersinteractie analyseren (G-I) : niveau 1
- Gebruikersinteractie ontwerpen (G-O) : niveau 1
- Gebruikersinteractie realiseren (G-R) : niveau 1
- Infrastructuur ontwerpen (I-O): niveau 1
- Infrastructuur realiseren (I-R): niveau 1
- Infrastructuur manage & control (I-MC): niveau 
- Organisatieprocessen analyseren (O-A): niveau 1
- Organisatieprocessen ontwerpen (O-O): niveau 1

_Binnen deze opdracht ligt de focus op de volgende professional skills:_

- Persoonlijk leiderschap (PL) :
  - Ondernemend zijn (PL-O) : niveau 1
  - Persoonlijke ontwikkeling (PL-PO): niveau 1
- Toekomstgericht organiseren (TO)
  - Managen (TO-M) : niveau 1
  - Ethiek (TO-E) : niveau 1
- Doelgericht interacteren (DI)
  - Communiceren (DI-C) : niveau 1
  - Samenwerken (DI-S): niveau 1

  Een overzicht van alle competenties vind je [hier](http://haru.hva-fys.nl:28002/).

## Hoe installeer ik het?
...

De installatie is hetzelfde als in blok 2. Daarbij krijg je een aantal docker compose bestanden. Die heb je nodig om lokaal dus op je eigen laptop, een netwerk te bouwen zodat de losse onderdelen van jullie applicatie (webapp, database, etc) met elkaar kunnen praten.

Ga nu eerst oefenen met het werken met git in een team.

1. Maak een clone van het project. Ieder lid 1
2. Iedereen met een clone van dit project moet controleren of de volgende bestanden de juiste naam hebben, en zo nodig hernoemen:
- gitignore -> `.gitignore` (indien nog niet voorzien van een `.`)
- dockerignore -> `.dockerignore` (indien nog niet voorzien van een `.`)
3. Het lid met de rol SCRUM master gaat nu een git branch maken in VSC. Geef de branch een duidelijke naam, bijvoorbeeld `dev`. Maak een nieuw bestand aan in docs en commit. Let op dat je nu commit in de branch die je zojuist hebt aangemaakt. De SCRUM master pushed hem naar Gitlab.
4. Controleer op Gitlab of deze nieuwe branch zichtbaar is.
5. Alle andere leden doen nu een pull, oftewel ze halen de wijzigingen van Gitlab op.
6. Alle leden doen een checkout van deze nieuwe branch. Controleer of je het nieuwe bestand ziet.
7. Maak nu een merge request aan op Gitlab en voer de merge uit. Controleer of er nog maar 1 branch is: `main`.
7. Alle leden doen een synch en checkout van de `main` branch.
8. Zorg ervoor dat iedereen in een eigen branch werkt; gebruik voor die branch bijvoorbeeld de naam van de betreffende blueprint. Werk niet in `main` maar maak alleen merge requests aan naar `main` toe.

Ga vervolgens de database koppelen. Lees de omschrijvingen en verander alle `VARIABELEN`, dus de variabelen in HOOFDLETTERS. Zie verder blok 2.

Bepaal nu samen met het team en de docent welke _blueprints_ jullie nodig hebben.

## Hoe gebruik ik dit, documentatie

In de `docs` folder van de broncode zet je de technische documentatie én beschrijf je wat geleerd hebt. Belangrijk is dat de documentatie onderdeel wordt van de broncode. Zo kan je vanuit de ontwikkelomgeving documentatie bijhouden.
Al het bewijsmateriaal neem je op in GITLAB zodat dat je daarna kan verwijzen vanuit een user of learning story en Scorion. Definieer daarvoor een folder structuur waarbij je rekening houd met sprints en dat een deel van het bewijsmateriaal per student is.

Zorg dat er in je GITLAB omgeving een beschrijving is van je project. Die moet je dus zelf maken want niet alle teams werken aan precies hetzelfde project.


# circolari_lorenzini
## I bidelli non portano più le circolari in classe per via del covid?
## E tu sei già stanco di controllare periodicamente sul sito della scuola?
Non ti preoccupare, ho io la soluzione per te!\
Questo **fantastico** bot telegram ti manderà un messaggio contenente numero, titolo, data e link di ogni circolare nel momento in cui viene pubblicata sul sito della scuola.

## Utilizzo
Scrivi ```/start``` al bot **_@LorenziniBot_** ed il gioco è fatto

### Info tecniche sul progetto
Linguaggio: python3\
Modulo per il bot: python-telegram-bot\
Modulo per scraping: beautifulsoup\
Database: mysql

#### Sentiti libero di contribuire al progetto,
Per contribuire, suggerimenti, bug report o maggiori informazioni contatta _@palumbo_luca__ su instagram. Non sono necessarie skill di programmazione per contribuire.


## Set up
Per prima cosa è necessario decidere dove hostare il bot. Ci sono vari servizi di hosting online. Consiglio di creare un account AWS e attivare una macchina EC2 ubuntu con il piano gratuito per 12 mesi.\
\
Dopodiche si deve accedere alla macchina (ti verranno fornite le chiavi di accesso da Amazon). Per farlo bisogna sapere usare un minimo la shell linux.\
Una volta connessi si deve lanciare in successione:
- ```git clone https://github.com/LucaPalumbo/circolari_lorenzini.git``` per clonare questa repository.
- Adesso si dovrà creare un file chiamato `secrets.py` all'interno della cartella `src`.\
Al suo interno si dovrà scrivere:
```
DB_PASSWORD = "<password>"
TOKEN = "<token>"
```
  Chiaramente sostituendo `<password>` con una password scelta per il database e `<token>` con il token del bot telegram.
- Il passo successivo è modificare il file `docker-compose.yml` in corrispondenza della riga con scritto `MYSQL_ROOT_PASSWORD: secret`. Sostituite la parola `secret` con la password del database scelta prima.
- ```cd circolari_lorenzini``` per cambiare la directory corrente.
- ```docker-compose up -d``` per buildare il container. Potrebbe essere necessario prima installare docker. Con questo comando si avvia uno script che pensa al setup del database e ad avviare il programma.

A questo punto il bot è perfettamente funzionante!

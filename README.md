# DEPLOY - HOWTO
## Prerequsities:
* redis in place
* postgres in place with proper schema

## Deploying data retrieval services:
python deploy_data_retrieval

## Deploying arbitrage bots
python deploy

### How to run dedicated services from subfolder:
python -m services.telegram_notifier

## Kill ALL processes
``` bash
ps -ef | grep arbitrage | awk '{print $2}' | xargs kill -9 $1
```
or just
pkill python

## Kill ALL screens with all session MacOs
``` bash
screen -ls | awk '{print $1}' | xargs -I{} screen -S {} -X quit
```
based on  https://stackoverflow.com/questions/1509677/kill-detached-screen-session

``` bash
alias cleanscreen="screen -ls | tail -n +2 | head -n -2 | awk '{print $1}'| xargs -I{} screen -S {} -X quit"
```

### REMOTE_ACCESS:
``` bash
ssh -v -N -L 7777:192.168.1.106:5432 86.97.142.164 -i .ssh/crptdb_sec_openssh -l dima -p 8883
ssh -i .ssh/crptdb_sec_openssh -v dima@86.97.142.164 -p 8883
ssh dima@86.96.108.235 -p 8883
```

### MacOs dependencies:
pip install python-telegram-bot --user

### redis
type <key>
and depending on the response perform:

https://lzone.de/cheat-sheet/Redis
for "string": get <key>
for "hash": hgetall <key>
for "list": lrange <key> 0 -1
for "set": smembers <key>
for "zset": zrange <key> 0 -1 withscores

### POSTGRES
https://wiki.postgresql.org/wiki/Deleting_duplicates

Postgres backups:
pg_dump -h 192.168.1.106 -p 5432 -U postgres -F c -b -v -f "/home/dima/full_DDMMYYYY"
pg_dump -h 192.168.1.106 -p 5432 -U postgres -s public


### TELEGRAM BOT
How to get ID of telegram chat:
https://api.telegram.org/bot<YourBOTToken>/getUpdates

"""
How to check what the fuck is happening with the bot:
https://api.telegram.org/bot438844686:AAE8lS3VyMsNgtytR4I1uWy4DLUaot2e5hU/getUpdates

"""
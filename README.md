# Project structure

System consist from multiple independent processes that may be run on different node.   
Communication is implemented on top of various message queues on top of redis.    
Redis is also used as distributed caching layer - to reflect actual balance across all exchanges.    
Data in queues usually pickled.  
Persistence for historical data - postgres.    
Alerting is implemented on top of Telegram messenger.   
CLI management is done manually using scripts within this project.    

NOTE: Web based UI and data scrapping framework from various resources are NOT part of this repo.

## Terminology
- _**bot**_ - arbitrage process that trade single commodity between exactly two exchanges
- _**order**_ - what bot is placed to markets
- _**trade**_ - what was actually executed at markets, single order may be closed by multiple trades


## Key services:
- _**telegram notifier**_ - watch message queues and forward messages based on their severity 
to corresponding Telegram channels
- _**balance_monitoring**_ - update cached values of balances for all currencies for all exchanges in portfolio
All trading processes validate time of last update and will immediately stopped if it expired.
- _**expired order processing**_ - due to many reasons order placed by bot may be not closed in time,
this service re-process them trying to minimise loss 
- _**failed order processing**_ - timeout, exchange errors and ill fate may lead to situation that 
we got errors as result of order placement request. This service carefully check current state of order:
whether it was registered within exchange or not, whether it was fulfilled or not.

## Data analysis:
- _**order saving**_ - save all orders that were placed by arbitrage processes into Postgres db
- _**bot trade retrieval**_ - retrieve information from all exchanges in regards to recently executed trades. 
- _**arbitrage monitoring**_ - read tickers for all supported currency across all exchanges and 
issue a telegram notification about direct arbitrage opportunities



You may find all available services under services packages.

# DEPLOY - HOWTO

## Prerequisites:
Node with data and cache:
* redis in place
```bash
sudo service docker start
cd ~/crypto_deploy/redis
# NOTE: you may want to edit path to mounted volume for data persistence 
sudo docker-compose -f redis_compose.yml up
# NOTE: redis IP is hardcoded there:
python redis_queue.py
```
* postgres in place with proper schema and data:
```bash
sudo service docker start
cd ~/crypto_deploy/postgres
# NOTE: you may want to edit path to mounted volume for data persistence
sudo docker-compose -f docker-compose-postgres.yml up
psql -h 127.0.0.1 -Upostgres -f schema/schema.sql
psql -h 127.0.0.1 -Upostgres -f schema/data.sql
```
* data retrieval & nodes with bot processes:
```bash
yum groupinstall "Development Tools"
pip install -r requirements.txt
``` 
* copy `common_sample.cfg` to `common.cfg` and update it with proper public IP addresses and domain names
* make sure that firewall rules at aws allow incoming connections from bot nodes to data node

## Deploying data retrieval services

Will deploy: 
* order_book, history, candles, 
* arbitrage notifications based on tickers
* telegram notifications
```bash
python deploy_data_retrieval.py
```

## Deploying arbitrage bots
1. verify settings at config file:
more deploy/deploy.cfg
2. Initiate deployment processes
python deploy_arbitrage_bots.py deploy/deploy.cfg

### How to run dedicated services from subfolder:
``` bash
python -m services.telegram_notifier
```
## Kill ALL processes
``` bash
ps -ef | grep arbitrage | awk '{print $2}' | xargs kill -9 $1
```
or just
``` bash
pkill python
```

## Kill ALL screens with all session MacOs
``` bash
screen -ls | awk '{print $1}' | xargs -I{} screen -S {} -X quit
```
screen -ls | grep -v deploy | awk '{print $1}' | xargs -I{} screen -S {} -X quit
based on  https://stackoverflow.com/questions/1509677/kill-detached-screen-session

``` bash
alias cleanscreen="screen -ls | tail -n +2 | head -n -1|cut -d'.' -f 1 |xargs kill -9 ; screen -wipe"

alias bot_count='ps -ef | grep python | wc -l'
alias bot_kill='pkill python'
alias bot_stop_screen="screen -ls | tail -n +2 | head -n -1|cut -d'.' -f 1 |xargs kill -9 ; screen -wipe"
```

## Rename existing screen session
``` bash
screen -S old_session_name -X sessionname new_session_name
```

### REMOTE_ACCESS:
``` bash
ssh -v -N -L 7777:192.168.1.106:5432 86.97.142.164 -i .ssh/crptdb_sec_openssh -l dima -p 8883
ssh -i .ssh/crptdb_sec_openssh -v dima@86.97.142.164 -p 8883
ssh dima@86.96.108.235 -p 8883
```

### MacOs dependencies:
``` bash
pip install python-telegram-bot --user
```

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
``` bash
pg_dump -h 192.168.1.106 -p 5432 -U postgres -F c -b -v -f "/home/dima/full_DDMMYYYY"
pg_dump -h 192.168.1.106 -p 5432 -U postgres -s public
-- How to do full dump without particular tables
pg_dump -h 192.168.1.106 -p 5432 -U postgres -F c -b -v --exclude-table=alarams --exclude-table=tmp_binance_orders --exclude-table=tmp_history_trades --exclude-table=tmp_trades --exclude-table=trades -f "/home/dima/full_DDMMYYYY"
```

AWS:
``` bash
psql --host=orders.cervsj06c8zw.us-west-1.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=crypto
```


### TELEGRAM BOT
How to get ID of telegram chat:
https://api.telegram.org/bot<YourBOTToken>/getUpdates

"""
How to check what the fuck is happening with the bot:
https://api.telegram.org/bot438844686:AAE8lS3VyMsNgtytR4I1uWy4DLUaot2e5hU/getUpdates

"""


### Get all tradable pairs
https://www.binance.com/api/v1/ticker/allBookTickers
https://bittrex.com/api/v1.1/public/getmarkets

https://api.kraken.com/0/public/Assets
https://api.kraken.com/0/public/AssetPairs

https://poloniex.com/public?command=returnTicker

http://api.huobi.pro/v1/common/symbols


### Socket subscriptions endpoints:
wraping out websocket into class with callbacks:
https://github.com/websocket-client/websocket-client

exchanges API:
https://bittrex.github.io/#ws-api-overview
https://github.com/binance-exchange/binance-official-api-docs/blob/master/web-socket-streams.md
https://github.com/huobiapi/API_Docs_en/wiki/Huobi-API
https://poloniex.com/support/api/ - not too much info
kraken - na

Examples of implementation:
https://github.com/s4w3d0ff/python-poloniex
https://github.com/absortium/poloniex-api
https://github.com/czheo/huobi-client-python
https://github.com/sammchardy/python-binance
https://github.com/slazarov/python-bittrex-websocket


### Rounding rules

https://support.binance.com/hc/en-us/articles/115000594711-Trading-Rule


### Setup balance monitoring from the scratch
``` bash
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo yum install docker, mc, git
sudo service docker start
sudo /usr/local/bin/docker-compose -f docker_compose.yml up
scp -i wtf.pem -r crypto_crawler/secret_keys/ ec2-user@ec2-54-183-153-123.us-west-1.compute.amazonaws.com:/tmp/
```


### sysops
``` bash
sudo logrotate -s /var/log/logstatus /etc/logrotate.conf
/home/ec2-user/crypto_crawler/logs/*.log {
    size 10M
    compress
    rotate 10
    nodateext
    missingok
    notifempty
}

sudo vim /etc/crontab
*/5 * * * * root logrotate -f /etc/logrotate.conf

sudo service crond restart
```

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario3


### Logs analysis

How to find last modified files recursively:
``` bash
find $1 -type f -print0 | xargs -0 stat --format '%Y :%y %n' | sort -nr | cut -d: -f2- | head
```

How to merge all files in single file sorted by numerical indexes:
```bash
ls socket_errors.log* | sort -Vr | xargs cat > history.log
```

How to find all lines in log containing PID and sort entries by time:
```bash
grep 'PID: 9848' *.log* | sed 's/:/ : /'  | sort -k 3 > 9848_sorted_by_time.log
```

How to select log entries that are within particular time range:
```bash
awk '($3 >= 1553066553) && ($3<=1553066599)' 9848_1.log > suspect.log
```

How to build processing histogram:
```bash
head all_profile.log
1553052602 :  PID: 19399 Start: 1553052602200 ms End: 1553052602201 ms Runtime: 1 ms
1553052602 :  PID: 19115 Start: 1553052602187 ms End: 1553052602201 ms Runtime: 14 ms
1553052602 :  PID: 18629 Start: 1553052602201 ms End: 1553052602202 ms Runtime: 1 ms

more all_profile.log | awk '{ print $12 }' | sort -n | uniq -c

```


### Anaconda profit report How-TO Windows
1. Install https://www.anaconda.com/download/ for 2.7 Python
2. Run  Start->Programs->Anaconda Prompt
3. Install necessary dependencies using pip:
``` bash
    pip install redis tqdm
```
4. Run Start->Programs->Jupiter Notebook
5. Open Notebook from ipython_notebooks/iPython_local_Input.ipynb
6. Adjust following parameters:
* CRYPTO_MODULE
* should_fetch_data
* time_end
* time_start
* api_key_full_path
7. Sequentially execute all sells
8. Profit report should be under your %HOME%/logs folder



### How to setup dynuiuc domain name update
```bash
more /usr/lib/systemd/system/dynuiuc.service
[Unit]
Description=Dynu

[Service]
Type=forking
PIDFile=/var/run/dynuiuc.pid
ExecStart=/usr/bin/dynuiuc --conf_file /etc/dynuiuc/dynuiuc.conf --log_file /var/log/dynuiuc.log --pid_file /var/run/dynuiuc.pid --daemon
ExecReload=/bin/kill -HUP $MAINPID
# DK manually
Restart=always

[Install]
WantedBy=multi-user.target
```
sudo systemctl enable dynuiuc.service
sudo service dynuiuc start


###
python -m services.arbitrage_between_pair_subscription --threshold 1.2 --reverse_threshold 0.71 --balance_threshold 15 --sell_exchange_id 4 --buy_exchange_id 4 --pair_id 1 --deal_expire_timeout 15 --cfg deploy/deploy.cfg

### Postgres various
```sql
-- avg amount of records per table
SELECT schemaname,relname,n_live_tup 
  FROM pg_stat_user_tables 
  ORDER BY n_live_tup DESC;
```
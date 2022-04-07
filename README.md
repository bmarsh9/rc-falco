# rc-falco

## About

This repository provides a minimal example of using [Falco](https://falco.org/) for detection and analysis. If you follow the instructions below, you will have Falco running, an Web UI to consume the Falco alerts and the Falco alert generator.

<p align="center">
  <img height="600px" src="https://github.com/bmarsh9/rc-falco/raw/main/images/web-ui.png" alt="Logo"/>
</p>

## Prereqs

+ Ubuntu/debian based OS
+ Docker installed (with docker tools for building images)

## Warning

This is for learning and not production use. Encryption/authentication is not enabled.

## First we need to install Falco

#### Install Falco on the host/node (Ubuntu/Debian)

```
curl -s https://falco.org/repo/falcosecurity-3672BA8F.asc | apt-key add -
echo "deb https://download.falco.org/packages/deb stable main" | tee -a /etc/apt/sources.list.d/falcosecurity.list
apt-get update -y

apt-get -y install linux-headers-$(uname -r)
apt-get install -y falco
```

#### Edit the config files

```
# Open /etc/falco/falco.yaml
# Find the section that starts with `program_output` and it should look like below.
# Be sure to replace your IP address (private) within the curl command

program_output:
  enabled: true
  keep_alive: false 
  program: "jq '{event: .}' | curl --header 'Content-Type: application/json' -d @- -X POST http://your-ip:5000/events"
```

#### Start falco

```
falco -pc
```

## Now we are going to install our custom containers


#### Get started with docker

```
git clone https://github.com/bmarsh9/rc-falco.git
docker build -t rc-falco .
docker run -p 5000:5000 rc-falco
```

#### (Or) Get started from scratch 

```
git clone https://github.com/bmarsh9/rc-falco.git
pip3 install -r requirements.txt
python3 app.py
```

Now browse to `http://your-ip:5000` and you should see the UI


#### Generate some fake events

```
docker pull falcosecurity/event-generator:latest
docker run falcosecurity/event-generator run
```

Back in the UI - you should see events populated

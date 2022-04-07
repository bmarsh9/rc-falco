# rc-falco

#### Get started with docker

```
git clone https://github.com/bmarsh9/rc-falco.git
docker build -t rc-falco .
docker run -p 5000:5000 rc-falco
```

#### Get started from scratch 

```
git clone https://github.com/bmarsh9/rc-falco.git
pip3 install -r requirements.txt
python3 app.py
```

Now browse to `http://your-ip:5000`


#### Generate some fake events

```
docker pull falcosecurity/event-generator:latest
docker run falcosecurity/event-generator run
```

## Config daemon do Docker 

```sh
vagrant ssh 
sudo mkdir -p /etc/systemd/system/docker.service.d/
```

### Criar override.conf

```sh
sudo nano /etc/systemd/system/docker.service.d/override.conf
```

#### copiar e colar

```sh
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2379
```

## Reload no Daemon

```sh
sudo systemctl daemon-reload
sudo systemctl restart docker.service
```
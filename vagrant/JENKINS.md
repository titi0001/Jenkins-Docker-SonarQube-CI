# Configurando o ambiente e conectando máquina virtual

## Máquina virtual com o vagrant

### Subindo o ambiente virtualizado

```sh
vagrant plugin install vagrant-disksize
vagrant up
vagrant ssh
ps -ef | grep -i mysql # Verificando se o MySQL esta rodando
mysql -u devops -p # Senha mestre; show databases
mysql -u devops_dev -p # Senha mestre; show databases
# Instalando o Jenkins
cd /vagrant/scripts
# Instalando o docker
sudo ./docker.sh
# Visualizar o conteudo do arquivo de instalacao do jenkins
sudo ./jenkins.sh

# Acessar:  192.168.33.10:8080
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# Reload nas permissoes do docker
sudo usermod -aG docker $USER
sudo usermod -aG docker jenkins
exit
vagrant reload
```

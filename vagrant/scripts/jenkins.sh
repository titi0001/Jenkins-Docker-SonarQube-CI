# 1. Adiciona a chave GPG para o repositório Jenkins
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

# 2. Adiciona o repositório Jenkins à lista de fontes do apt
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

# 3. Atualiza os pacotes e instala o Jenkins
sudo apt-get update
sudo apt-get install jenkins -y

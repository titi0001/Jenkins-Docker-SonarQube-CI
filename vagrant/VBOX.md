# Instalação do virtualbox no windows

### 1. Instalar o Chocolatey (se ainda não estiver instalado)

Se você ainda não tem o Chocolatey instalado, siga estes passos:

Abra o PowerShell como Administrador.
Execute o seguinte comando para instalar o Chocolatey:

```sh
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

###  2.Instalar o VirtualBox Usando o Chocolatey
Depois de instalar o Chocolatey, você pode instalar o VirtualBox com um simples comando no PowerShell:

Ainda no PowerShell (como Administrador), execute:
```sh
choco install virtualbox -y
```

 * ###  2.1 Verificar a Instalação
   Após a instalação, você pode verificar se o VirtualBox foi instalado corretamente executando:

```sh
  virtualbox
```

- - -

### Alternativa: Download Manual e Instalação Via PowerShell

Se você preferir não usar o Chocolatey, também pode baixar o instalador do VirtualBox diretamente do site oficial e instalá-lo via PowerShell:

#### 1.Baixar o Instalador:

Use o PowerShell para baixar o instalador do VirtualBox:

```shell
Invoke-WebRequest -Uri "<https://download.virtualbox.org/virtualbox/7.0.6/VirtualBox-7.0.6-156879-Win.exe>" -OutFile "$env:USERPROFILE\Downloads\VirtualBox-Installer.exe"
```

#### 2.Instalar o VirtualBox:

Execute o seguinte comando para instalar o Chocolatey:

```sh
Start-Process "$env:USERPROFILE\Downloads\VirtualBox-Installer.exe" -ArgumentList "/S" -Wait
```

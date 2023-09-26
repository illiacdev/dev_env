# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "docker4dev" do |config|
    config.vm.box = "ubuntu/jammy64"
    config.vm.hostname = "docker4dev"
    config.vm.network "private_network", ip: "192.168.100.100"
    config.vm.provider "virtualbox" do |vb|
      vb.name = "docker4dev"
      vb.cpus = 2
      vb.memory = 4096
    end
  end
  

  # Hostmanager plugin
  config.hostmanager.enabled = true
  config.hostmanager.manage_guest = true

  config.vm.provision :docker
  config.vm.provision :docker_compose

  # Enable SSH Password Authentication
  config.vm.provision "shell", inline: <<-SHELL
    sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
    sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
    sed -i 's/security.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
    systemctl restart ssh
    systemctl start systemd-timesyncd
    timedatectl set-timezone UTC
  SHELL
end
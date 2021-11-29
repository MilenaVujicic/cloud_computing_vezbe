Virtuelne mašine
=================

Vagrant
-------
Instalacija: 
    - Potrebno je instalirati Oracle VM VirtualBox: https://www.virtualbox.org/wiki/Downloads
    - Zatim je potrebno instalirati Vagrant: https://www.vagrantup.com/docs/installation

Vagrant je alat za automatsko kreiranje i podešavanje virtuelnih mašina.
Vagrant Cloud sadrži repozitorijum Vagrant Box-ova koji se koriste za kreiranje virtuelne mašine: https://app.vagrantup.com/boxes/search
Vagrantfile se koristi za konfiguraciju virtuelne mašine
Najbitnije Vagrant komande su:
    - vagrant init (inicijalizacija Vagrantfile-a)
    - vagrant up (pokretanje virtuelne mašine)
    - vagrant halt (zaustavljanje virtuelne mašine)
    - vagrant suspend (pauziranje izvršavanja virtuelne mašine)
    - vagrant reload (ponovno pokretanje virtuelne mašine)
    - vagrant ssh (pristup konzoli virtuelne mašine)

Provisioning:
    - Izvršavanje skript fajlova i kopiranje fajlova na Vagrant mašinu. Prilikom pokretanja mašine potrebno je definisati flag --provision.

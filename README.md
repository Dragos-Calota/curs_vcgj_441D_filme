# curs_vcgj_441D_filme

Pentru acest proiect am avut nevoie sa folosim Docker, Jenkins si Python3 pe care le-am incarcat prin intermediul comenzilor git proiectul pe platforma GitHub. 

Pentru inceput am creat un folder local pe masina virtuala in care voi incarca toate fisierele. Cu ajutorul git clone am copiat folderul de pe serverul remote, pe masina virtuala.

Prin utilizarea comenzii git branch devel/TaranuCostin am creat branchul personal pe care am publicat toate fisierele aferente realizarii proiectului.

Pentru tema, am ales filmul 21 Jump Street, aparut in 2012 si cu o nota pe IMDB de 7.2, detalii pe care le am incarcat in fisierul biblioteca_filme.py, care vor fi afisate pe pagina web pe care am creat-o.

Dupa scrierea codului si a toturor dependtelor necesare aplicatie, am rulat comanda python3 441D_filme.py care a pornit aplicatia pe adresa IP 127.0.0.1 pe portul 5001. Pentru a afisa anul si rating-ul filmui va fi nevoie sa accesam 127.0.0.1:5001/21.

Dupa verificarea functionalitatii site-ului, am testat functionalitatea programului Jenkins, cu ajutorul plug-in-ului Ocean Blue care are o interfata grafica prietenoasa si ajuta la o verificare mai usoara asupra procesului de CI/CD, un proces foarte folosit in domeniul devOps. 

Trebuie sa luam in considerare, ca pentru orice modificare a codului trebuie sa trimitem din masina virtuala modificarile catre GitHub apoi sa dam build in Jenkins.

Pentru containerizarea cu Docker, am avut de creat un dockerfile, care a fost folosit pentru crearea containerului, pe care voi lansa aplicatia descrisa mai sus. Containerul l-am facut sa ruleze pe portul 8020, si poate fi accesat prin scrierea IP-ului configurat sau localhost, 127.0.0.1:8020.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/03187426-e98b-442e-a992-a0ebb310bde8)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/c3ba891d-b7e2-4735-a4b3-2b8e8719cbc3)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/6995a881-1393-491f-932c-7a15639296b6)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/427a10f0-a130-4510-807f-8bf345d60e44)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/7604b010-ca0b-48f0-8623-a8191189ca64)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/b79405a5-75dd-42c2-9c20-c1d8379e0d5d)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/978bccc3-b81b-48af-b480-9fda3edd0405)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/b7f1587d-b054-46c6-bbf2-215529d8b038)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/116729792/8b65ff2b-c5e7-46e5-a84f-2b71de4a8ddb)


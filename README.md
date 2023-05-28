## Proiect VCGJ 441D
Film:Baywatch

# Introducerea
În cadrul acestui proiect, veți dezvolta o aplicație web Flask pentru afișarea informațiilor despre filme. Pentru a realiza acest lucru, veți utiliza un set divers de unelte din industria software, precum mașina virtuală, Git și GitHub, Jenkins și Docker. Aceste unelte vă vor ajuta în dezvoltarea și implementarea aplicației într-un mod eficient și structurat.

# Configuratia

În primul rând, va trebui să instalam mai multe programe pe mașina virtuală cu sistemul de operare `Ubuntu`, inclusiv `git`, `gedit`, `vim`, `python3`, `pytest`, `pip`, `docker` și `jenkins`.

Pentru a începe proiectul, cream un director de lucru utilizând comanda `mkdir git`, iar apoi clonam repo-ul de pe GitHub (https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git) în acest director.

Pentru a verifica dacă directorul git este sub supravegherea git, utilizați comanda git status în linia de comandă și veți vedea starea acestuia.
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/a6a84137-bdbf-44b3-80e5-a4eaef3dfaab)
Vom crea fisierele care contin rutele 441D_filme.py
În cadrul proiectului /home/git/curs_vcgj_441D_filme, vom crea un nou director numit /app, folosind comanda mkdir. Acest director va conține fisierele și codul aplicației noastre. Având în vedere că am ales filmul "Baywatch", vom implementa două funcții esențiale: an_lansare_baywatch(), care va returna `2017` sub formă de string, și rating_baywatch(), care va returna `5.5 tot sub formă de string. Pentru a completa structura, vom crea și directorul /lib în cadrul directorului /app, folosind comanda mkdir, iar apoi vom crea fișierul biblioteca_filme.py în același director, utilizând comanda touch. Acest fișier va conține implementarea funcțiilor menționate mai devreme. Pentru a edita fișierul, vom utiliza comanda gedit.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/ba339354-6ed7-4199-bcf3-be92897d36f7)

441d_Filme.py

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/31f83663-e256-4e15-885a-925b911304cf)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/2aa4289e-b9bc-4092-b608-7a956ecd6268)

Aplicația Flask va fi rulată și va folosi portul 5001 prin intermediul următoarei linii de cod: `app.run(host="127.0.0.1", port=5001)`. Astfel, aplicația va fi accesibilă local prin intermediul adresei `IP "127.0.0.1"` și 'portul 5001' va fi utilizat pentru comunicare.
Acum avem posibilitatea să pornim aplicația 441D_filme.py din directorul `/app` folosind următoarea comandă: `python3 441D_filme.py`. Programul va fi lansat pe mașina locală.
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/e918d5d2-84c9-43a0-b0f7-c9aac5d185fb)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/085c763e-70a1-4740-ab2f-3740bf208f42)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/749325c5-31b4-4a78-96cb-673fa1fec9ac)
`test_biblioteca_filme_py`
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/f7374bfb-d924-4c45-a1d3-70841a1543ca)

# Testarea cu Jenkins

`sudo systemctl enable jenkins`,`sudo systemctl start jenkins`,`sudo systemctl status jenkins`

http://localhost:8080/ - serverul de jenkins va fi accesat la aceasta adresa

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/4fb8effc-d642-4a10-b456-d3a2e39a919c)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/a3cac398-4845-438e-ac40-38ebdda48d98)

Setarile pentru Jenkins
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/40944352-ab4f-4fa7-81c6-a0adb4fb30b4)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/489eaed8-f64f-46c5-b126-a8ece86bdd52)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/97eec698-cbbe-4852-9155-37dd716d21c4)

# Docker
Vom crea Dockerfile care va fi folosit pentru a crea containerul
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/f8f628d6-146a-42ab-bc3c-14999d7289f2)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/3baba7bd-7e60-4bba-9dff-8a31a205db9d)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/a62b732f-b678-4a9a-ab77-0525920c74b2)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/92727024/6486dccf-be7b-4d26-a25b-dfd9a5945a7f)









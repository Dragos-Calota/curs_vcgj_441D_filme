# Proiect VCGJ 441D
Film: Shooter

# Introducere

În cadrul acestui proiect, veți crea o aplicație web Flask care va afișa informații despre filme. Pentru a atinge acest obiectiv, veți beneficia de un set variat de instrumente din industria software, inclusiv o mașină virtuală, Git și GitHub, Jenkins și Docker. Utilizarea acestor unelte vă va permite să dezvoltați și să implementați aplicația într-un mod eficient și bine structurat, facilitând procesul de lucru în echipă și asigurând livrarea de calitate a proiectului.

# Configuratia

Sunt necesare mai multe programe pe masina virtuala de Ubuntu, `git`, `gedit`, `vim`, `python3`, `pytest`, `pip`, `docker`si `jekins`.

Ca si inceput, trebuie sa cream un folder folosind comanda `mkdir`, dupa care clonam repo-ul de pe GitHub in acest director (git clone https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git).

![Screenshot 2023-05-29 011355](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/8538f2a1-892c-4a1d-872e-5382950d9fb0)

In acest folder, se va crea un folder app, care contine `441D_filme.py` care stocheaza rutele. Sunt implementate 2 functii esentiale: `an_lansare_shooter` si `an_lansare_shooter`, care vor returna `2007` respectiv `7.1`.
In acest folder, folosim comanda `mkdir` pentru a mai crea unul, cu numele `/lib` in care vom adauga fisierul `biblioteca_filme.py`.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/ca7be243-8c83-416b-8332-5b492a03e47c)

Fisierul 441D_filme.py:

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/84be272f-79aa-449a-97ea-39b7015338e3)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/3d82d809-941b-433b-bfcd-523b3d7769c5)

Folosind Flask si portul 5001, putem rula aplicatia `441D_filme.py`, utilizand comanda: `python3 441D_filme.py`.


![Screenshot 2023-05-28 221817](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/1a1104b8-37a2-42ae-9be3-d2ad1689bdcd)


![Screenshot 2023-05-28 221612](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/2550920b-b54e-424b-a1fd-f5a9025128fa)


![Screenshot 2023-05-28 221718](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/badaf525-42b7-47a0-b299-2f6703c94a9a)


![Screenshot 2023-05-28 221739](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/b27623b9-5afe-4abd-aa5f-2b556e06bcf0)


![Screenshot 2023-05-28 222250](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/1777f9e7-1510-4648-aad9-ca1d376147ec)


# Jenkins

Dupa ce am instalat Jenkins pe masina virtuala si activarea acesteia, putem vedea statusul acesteia folosind comanda: `sudo systemctl status jenkins`.



![Screenshot 2023-05-28 225857](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/9284985e-518d-4eb6-b9ea-e139553a0ada)


Serverul de Jenkins poate fi accesat la adresa `localhost` pe portul `8080`.

*********

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/866ead91-0188-4ebe-b866-64f27223905e)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/d70a2dc1-b615-4e4e-a4be-0cad13b189ad)

*********
Setarile sunt acestea:

![Screenshot 2023-05-29 002542](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/a0b8cab1-4809-42a4-bd08-67465052e326)


![Screenshot 2023-05-29 002930](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/41b793ba-0b0e-4115-b350-6b02e2dc6342)

![Screenshot 2023-05-29 003624](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/491a7553-1e3e-4cf0-905f-f712b31f0018)

# Docker

Ca prim pas, cream fisierul Dockerfile, dupa care Dockerul.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/5075d662-6306-4236-90b4-1ef686813c69)


![Screenshot 2023-05-29 010927](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/2199ffb9-a32d-4e62-bd92-74579b4b9077)


![Screenshot 2023-05-29 011051](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/bad00e7b-9311-461e-9db0-585ceab96b73)


![Screenshot 2023-05-29 011116](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/04a76776-0ae8-4cc6-890e-a62796230cfb)


![Screenshot 2023-05-29 012153](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/96300867/ca6b41ed-5f40-40d5-b70c-fbd2d5cbb529)

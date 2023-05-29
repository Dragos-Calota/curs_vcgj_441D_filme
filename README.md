# curs_vcgj_441D_filme

# Proiect VCGJ 441D - Aplicație web/Flask cu filme
Film ales: Se7en

Introducere
Acest proiect implică crearea unei aplicații web Flask care va afișa informații despre filme și se vor utiliza diferite unelte din industria software, inclusiv mașina virtuală, Git și GitHub, Jenkins și Docker, pentru a dezvolta și implementa aplicația.

Configurare initiala
Pentru inceput vom avea nevoie de mai multe programe instalate pe masina virtuala cu Ubuntu : git,gedit,vim,python3,pytest,pip,docker,jenkins.

Pentru acest proiect am avut nevoie de un director in care voi lucra :se va crea cu mkdir git apoi in acest director am clonat de pe Github repo-ul(https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git). In CLI, dam un git status pentru a vedea daca directorul git este supervizat de git: `git status`

`cd curs_vcgj_441D_filme` ,`ls -la` – pentru a vedea daca s-au clonat de pe GitHub fisierele 

`git branch devel/GeorgescuMarius` - am creat branch-ul meu

`git checkout devel/GeorgescuMarius` -trecem pe branch 

Acum putem crea fisierele necesare proiectului, in primul rand, 441D_filme.py care va contine rutele si in el vom apela functiile necesare.

Vom crea in `/home/mariusdaniel99/Desktop/Proiect/curs_vcgj_441D_filme` alt director `/app` :  `mkdir app` iar in acest folder va se vor afla fisierele si codul aplicatiei.
Eu am ales filmul “se7en”, deci vom avea nevoie de functiile :  `an_lansare_se7en()` care va intoarce string-ul “1995” , `rating_se7en()` – care va intoarce “8.6”.
Vom crea inca un director in `/home/mariusdaniel99/Desktop/Proiect/curs_vcgj_441D_filme/app` -> `/lib`  cu `mkdir lib`
`touch biblioteca_filme.py` `gedit biblioteca_filme.py` Aici o sa scriem functiile.


![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/7b515f56-d16b-47dc-9125-b6161cd941e6)

______________________________________________________________________________________________________________________

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/77272d94-6218-42cd-8104-7e2f15917115)


cu linia urmatoare aplicatia Flask va rula si va folosi portul 5001:
`app.run(host = "127.0.0.1", port = 5001)`

Acum vom putea porni aplicatia 441D_filme.py din directorul /app astfel: `python3 441D_filme.py` Programul va porni pe masina locala, accesand link-ul 127.0.0.1:5001.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/f1115181-b742-4fb5-b2b6-5c079de01581)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/18bd77a5-6e02-4ebc-9977-cdbb1877880d)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/5661270a-2538-4076-93c0-135341c88148)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/d9f867db-b0b6-4fea-843b-877212b267b8)


In directorul /app am creat un director cu numele tests. Aici vom crea fisierul `test_biblioteca_filme.py` si vom crea functiile de testare, bfilme este fisierul importat din /lib – biblioteca_filme.py Pentru a vedea daca functioneaza testele, instalam pytest : `sudo apt install pip` `pip install pytest`
Pentru a rula testele local - pytest, folosim comanda (pentru python 3.10): `python3 -m pytest -v`

![2023-05-28_18-03](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/dd0e65f1-69c2-48a8-8298-e80ccad7ec6f)

Pentru a pune modificarile facute pe server in directorul /home/git/curs_vcgj_441D_filme vom da urmatoarele comenzi:
`git status` apoi `git add .` pentru a adauga fisierele in zona de staging apoi  `git commit -m “mesaj’` ,apoi 
`git push`.


# Testare cu Jenkins

`sudo systemctl enable jenkins`,`sudo systemctl start jenkins`,`sudo systemctl status jenkins` - pentru a porni Jenkins

Serverul Jenkins poate fi accesat la urmatoarea adresa: `http://localhost:8080/`

Pentru a rula intr-un mod automat, Jenkins are nevoie de un Virtual Environment si de quickrequirements.txt, care contine programele cerute pentru a putea rula in venv.Un venv va fi local – activeaza_venv, iar celalalt pentru Jenkins pe server – activeaza_venv_jenkins.
De asemenea, pentru a rula aplicatia pe server avem nevoie de alt fisier ruleaza_aplicatia. Pentru a configura testarea automata vom crea un pipeline.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/d3f3c8da-0cbf-47e1-9b4a-053e36740677)


In Blue Ocean dam build si testul va rula:

![2023-05-29_00-53](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/090a29ea-aae7-4ef9-9a83-d54d1040ecea)


# Docker
Avem nevoie de un Dockerfile care va fi folosit pentru crearea containerului cu aplicatia care contine functionalitatea la care se lucreaza, o imagine, un fisier pentru a porni serviciul docker – dockerstart.sh . Am creat imaginea folosind `sudo docker build -t 441d_filme:v01 .`

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/103530922/79d53ae3-ab30-4a3b-a654-6e18dda707b5)

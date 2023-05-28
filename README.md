# Proiect VCGJ 441D - Aplicație web/Flask cu filme

## Introducere 


Acest proiect implică crearea unei aplicații web Flask care va afișa informații despre filme. Se va utiliza mașina virtuală, Git și GitHub, Jenkins și Docker pentru a dezvolta și implementa aplicația.

### Configurație inițială

Pentru început vom avea nevoie de mai multe programe instalate pe mașina virtuală cu Ubuntu : git, gedit, vim, python3, pytest, pip, docker, jenkins.

Pentru acest proiect am avut nevoie de un director pe care l-am făcut pe Desktop cu comanda `mkdir git` în care să lucrez și să clonez de pe GitHub repository-ul https://github.com/Dragos-Calota/curs_vcgj_441D_filme cu comanda `git clone https://github.com/Dragos-Calota/curs_vcgj_441D_filme`

`git branch devel/marinalarisa_filme` - pentru a crea branch-ul personal și
`git checkout devel/marinalarisa_filme` - pentru a trece pe branch-ul personal

După am putut să creez fișierele necesare proiectului, cel mai important fiind 441D_filme.py care conține rutele și în care voi apela funcțiile necesare.

Am creat în /Desktop/git/curs_vcgj_441D_filme alt director /app cu comanda `mkdir app`, iar în acest folder se află fișierele și codul aplicației. Am ales filmul “Titanic”, deci am avut nevoie de funcțiile : an_lansare_titanic() care va intoarce string-ul “1997”, rating_titanic() – care va intoarce “7.9”. Am creat în /Desktop/git/curs_vcgj_441D_filme/app un director /lib cu comanda `mkdir lib`. Am creat aici un fișier cu comanda `touch biblioteca_filme.py` unde am scris funcțiile.

<img width="263" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/58a9c840-09cb-4dfd-b413-6440341a3e69">

Am creat în /Desktop/git/curs_vcgj_441D_filme/app un fișier cu comanda `touch 441D_filme.py`.

<img width="257" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/bf922693-3feb-45df-97ad-8a59478f0c96">


Acum a putut să pornească aplicația 441D_filme.py cu ajutorul comenzii `python3 441D_filme.py`.Programul a pornit pe mașina locală pe localhost:5001.

<img width="326" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/64627c28-efba-4c83-a251-f40d00c1573e">

<img width="329" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/9aa0efc7-090e-44c9-8fde-c0b158483791">

<img width="326" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/172873fa-68d2-4ab4-870a-c240f0d59ea3">

<img width="326" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/f696036d-e61a-4b93-ba9a-1b7b8ede9848">


În directorul /app am mai creat un director cu comanda `mkdir tests` unde am creat un fișier cu comanda `test_biblioteca_filme.py` și am pus funcțiile de testare. 

<img width="264" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/aaa72d1c-2fea-4a51-be31-815e52a05588">


Pentru a vedea dacă funcționează testele am folosit comanda `python3 -m pytest -v`.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/dc486b35-9547-41c9-af9e-75f049939fba)

Pentru a pune modificările făcute pe server în directorul /Desktop/git/curs_vcgj_441D_filme am dat comenzile: `git status`, `git add .` pentru a adăuga fișierele în zona de staging, `git commit -m "mesaj"`, `git push origin devel/marinalarisa_filme`. Pentru autentificare au fost cerute credențialele, parola fiind un token generat pe GitHub.

## Testare cu Jenkins

localhost:8080/ - serverul de jenkins va fi accesat la această adresă

Am instalat plugin-ul Blue Ocean care oferă o interfață prietenoasă în cadrul căreia putem vedea stage-urile, erorile, mesajele. Pentru testare automată cu Jenkins pipeline, am avut nevoie de Jenkinsfile care este fișierul de configurare folosit pentru a defini si executa pipeline-urile.

<img width="256" alt="image" src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/f8112f6d-a112-4488-b975-2c4152a1ede2">

Pentru a rula automat, Jenkins are nevoie de un Virtual Environment și de requirements.txt care conține programele cerute pentru a putea rula în venv. Un venv este local – activeaza_venv, iar celălalt pentru Jenkins pe server – activeaza_venv_jenkins. De asemenea, pentru a rula aplicația pe server am avut nevoie de alt fișier ruleaza_aplicatia. Pentru a configura testarea automată am selectat new build, am pus nume, am selectat pipeline și apoi:

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/e2fb8217-b600-44aa-94c2-7b24f9f2f732)

După ce am dat build în Blue Ocean am putut vedea toate stage-urile.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/343f9b7f-8401-46d7-80b9-56b97d42192c)


## Containterizare cu docker

Am avut nevoie de Dockerfile pe care l-am folosit pentru crearea container-ului cu aplicația care conține funcționalitatea la care am lucrat, o imagine, creată cu comanda `sudo docker build -t 441d_filme:v01` .

Am rulat containerul folosind comanda `sudo docker run --name 441d_filme -p 8020:5020 441d_filme:v01`  8020 este portul de pe care poate fi accesată aplicatia din container

Cu comanda `sudo docker ps`putem vedea containerul.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/8a3a0988-ea95-4f34-b7f1-779423c06d9a)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/f494313a-b07f-4637-be16-8ae70d247d9b)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/cce0ff37-efa6-46c6-9c60-c9b6922d56d9)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/105736202/e054c5ae-720e-4f28-9d7a-83e1a84f5993)









 ``

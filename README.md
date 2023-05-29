# Proiect VCGJ 441D-Aplicație web/Flask cu filme
Film ales:Heat

## Introducere
Acest proiect implică crearea unei aplicații web Flask care va afișa informații despre filme și se vor utiliza diferite unelte din industria software, inclusiv mașina virtuală, Git și GitHub, Jenkins și Docker, pentru a dezvolta și implementa aplicația.

##### Configurare initiala

Pentru inceput vom avea nevoie de mai multe programe instalate pe masina virtuala cu Ubuntu : git,gedit,vim,python3,pytest,pip,docker,jenkins.

Pentru acest proiect am avut nevoie de un director in care voi lucra :se va crea cu
`mkdir git` apoi in acest director voi clona de pe GitHub repo ul(https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git). 
In CLI, dam un git status pentru a vedea daca directorul git este supervizat de git : `git status`

`cd curs_vcgj_441D_filme ,ls -la` – verificam daca s-au clonat fisierele de pe GitHub

`git branch devel/MandaeAdrian` - creearea branch-ului

`git checkout devel/MandaeAdrian`  -trecem pe branch
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/134146583/71486ca6-09ce-4ff6-a3eb-54e72d908ade)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/134146583/01bcdf4a-1ce0-4593-bc33-40e5122ac146)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/134146583/73193039-76dd-474b-ae08-2347d8b49767)


## TESTARE CU JENKINS : 

`sudo systemctl enable jenkins`,`sudo systemctl start jenkins`,`sudo systemctl status jenkins`

`http://localhost:8080/` - accesarea serverului de jenkins

Va fi instalat plugin ul Blue Ocean care ofera o interfata prietenoasa in cadrul careia vedem stage urile,erorile,mesajele.
Pentru testare automata cu Jenkins pipeline, vom avea nevoie de Jenkinsfile care este fisierul de configurare folosit pentru a defini si executa pipeline urile.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/134146583/486afecc-9a08-4c6e-8448-6ef9315841e8)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/134146583/ba437859-99f9-42e8-82ae-5724406e8e7f)

Pentru orice modificare adusa codului va trebui sa facem din nou operatiunile git add,git commit,git push si apoi build.

## Containerizare cu docker

Vom avea nevoie de Dockerfile care va fi folosit pentru crearea contaierului cu aplicatia care  contine functionalitatea la care se lucreaza, o imagine, un fisier pentru a porni serviciul docker – dockerstart.sh 
Cream imaginea folosind `sudo docker build -t 441d_filme:v01 .`

Rulam containerul folosind sudo docker run --name 441d_filme -p 8020:5020 441d_filme:v01: Unde 8020 va fi portul de pe care poate fi accesata aplicatia din container

Cu `sudo docker` ps putem vedea containerul. 

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/134146583/01bfd76e-dc5c-4611-aae3-631441d57226)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/134146583/ce823390-1a70-4177-89bf-0ff58812f6df)




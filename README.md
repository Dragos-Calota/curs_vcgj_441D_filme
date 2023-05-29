# curs_vcgj_441D_filme


INTRODUCERE


Proiectul implica dezvoltarea unei aplicatii web prin care sa se poata vizualiza detalii despre anumite filme. Acest lucru il vom realiza prin intermediul unei masini virtuale, Git, Jenkins si Docker. Astfel, va trebui sa instalam mai intai git, gedit. python3, pytest, jenkins, docker.


ETAPA DE REALIZARE


Am creat directorul git cu ajutorul comenzii mkdir git. Apoi am folosit comanda git clone pentru a putea accesa repository-ul(https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git). 
Mai departe am intrat in curs_vcgj_441D_filme(cu ajutorul comenzii cd) si mi-am creat branchul personal(git branch devel/CristiLeustean), iar apoi am intrat pe branch pentru a dezvolta fisierele necesare proiectului(git checkout devel/CristiLeustean).

Am creat directorul app care va contine codul aplicatiei. In cadrul acestui cod(441D_filme.py), am avut nevoie sa apelez niste functii care sa imi returneze niste valori(an lansare, respectiv rating-ul filmului). Aceste functii le-am facut in alt director (lib) in fisierul biblioteca.py. Mai jos atasez o captura de ecran cu liniile codului pentru 441D_filme:

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/121881599/97f3ca97-c7bc-447f-b518-ddc460b48788)

Vom rula aplicatia cu ajutorul comenzii python3 441D_filme.py. Programul va porni local si vom putea vedea rezultatele aplicatiei pe linkul http://127.0.0.1 :5001, adica practic se deschide un host local pe portul 5001.
Eu am ales filmul The Irishman lansat in anul 2019 cu un rating IMDB de 7.8. Aceste informatii pot fi vazute accesand linkul si intrand pe filmul ales de mine.



![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/121881599/922a5f28-2ff2-489c-b8d9-cc5146110685)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/121881599/37898da2-12c0-4748-96a5-ffb41e9361e0)
 
Am creat apoi un director nou numit tests. Acolo am creat fisierul test_biblioteca.py cu ajutorul caruia testez rularea aplicatiei. Am rulat testele local cu ajutorul comenzii python3 -m pytest -v si am primit mesajul PASSED pentru cele doua functii(an lansare si rating). 

Mai departe, pentru a pune in GitHub fisierele create, am folosit comanda git status pentru a vedea cate fisiere trebuie bagate, apoi git add . pentru a le adauga in zona de staging. Am folosit comanda git commit -m "mesaj" si git push origin devel/CristiLeustean. A trebuit mai intai sa ma autentific, am avut de asemenea nevoie sa imi generez un token cu acces la repository. Am dat comanda ls -la pentru a vedea exact toate fisierele


![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/121881599/44d991f0-d2bd-4aa6-96ef-2bab4ee819fe)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/121881599/1e330b4d-0ebd-417a-8b28-9d1a2414b007)


JENKINS 

Am parcurs pasii de instalare pentru Jenkins. De asemenea, am instalat plugin-ul Blue Ocean care ne ofera o interfata mai usor de interpretat. Am creat Jenkinsfile care este fisierul de configurare care defineste si executa pipeline-urile. Pentru a rula automat, am creat fisierele activeaza_venv, activeaza_venv_jenkins si quickrequirements.txt pentru a putea rula aplicatia in venv (virtual environment). Pentru a rula efectiv aplicatia am creat fisierul ruleaza_aplicatia. In Jenkins, care se deschide local la adresa http://localhost:8080/, dupa ce am setat user si parola noua, am creat un pipeline nou, la care i-am dat adresa repository-ului in care lucrez proiectul (https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git) si la branch specifier, am pus branch-ul meu. Am dat build iar testele au fost rulate cu succes.


![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/121881599/2861d80c-21e8-469c-bab3-af727fac3377)



DOCKER

Partea de containerizare a aplicatiei am realizat folosind programul Docker. Am instalat aplicatia iar apoi, dupa ce am adaugat o imagine am pornit serviciul. Am creat imaginea folosind comanda sudo docker build -t 441d_filme:v01. Am rulat containerul folosind sudo docker run --name 441d_filme -p 8020:5020 441d_filme:v01, unde portul 8020 se foloseste pentru a accesa aplicatia din container.







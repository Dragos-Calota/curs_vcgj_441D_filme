# Proiect VCGJ 441D - Aplicație web/Flask cu filme 🎥🎥🎥🎥
Film ales: Complet Necunoscuti

## Introducere
Acest proiect implică crearea unei aplicații web Flask care va afișa informații despre filme și se vor utiliza diferite unelte din industria software, inclusiv mașina virtuală, Git și GitHub, Jenkins și Docker, pentru a dezvolta și implementa aplicația.

##### Configurare initiala

Pentru inceput vom avea nevoie de mai multe programe instalate pe masina virtuala cu Ubuntu : git,gedit,vim,python3,pytest,pip,docker,jenkins.

Pentru acest proiect am avut nevoie de un director in care voi lucra :se va crea cu
`mkdir git` apoi in acest director voi clona de pe GitHub repo ul(https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git). 
In CLI, dam un git status pentru a vedea daca directorul git este supervizat de git : `git status`

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/376a4dde-51b4-4051-b380-4e15080b51b8)

`cd curs_vcgj_441D_filme` ,`ls -la` – pentru a vedea daca s-au clonat de pe GitHub fisierele 

`git branch devel/LileaAndrei` -voi crea branch ul personal 

`git checkout devel/LileaAndrei` -trecem pe branch 

Acum putem crea fisierele necesare proiectului, cel mai important fiind 441D_filme.py care va contine rutele si in el vom apela functiile necesare.

Vom crea in `/home/git/curs_vcgj_441D_filme` alt director `/app` :  `mkdir app` iar in acest folder va se vor afla fisierele si codul aplicatiei.
Eu am ales filmul “tenet”, deci vom avea nevoie de functiile :  `an_lansare_tenet()` care va intoarce string-ul “2020” , `rating_tenet()` – care va intoarce “7.3”.
Vom crea inca un director in `/home/git/curs_vcgj_441D_filme/app` -> `/lib`  cu `mkdir lib`
`touch biblioteca_filme.py` `gedit biblioteca_filme.py` Aici vom scrie functiile.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/6f5cc2c8-c52a-4b79-9a15-f3dd4a3dae4e)

441D_filme.py cod:

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/88652e53-5d90-48c9-83e4-397f39e34b16)

cu linia urmatoare aplicatia Flask va rula si va folosi portul 5001:
`app.run(host = "127.0.0.1", port = 5001)`

Acum vom putea porni aplicatia 441D_filme.py din directorul /app astfel: `python3 441D_filme.py` Programul va porni pe masina locala, putem accesa link-ul `127.0.0.1 :5001` SAU `localhost :5001` 

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/55c79606-ea4f-4f78-a314-862fe1417774)

Ruta standard `‘/’`,`/CompletNecunoscuti` ->pentru informatii film ,`/CompletNecunoscuti/rating` si `/CompletNecunoscuti/an_lansare`

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/c168da0c-148e-4ce7-9962-96fe55dd45bb)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/a2f7a123-d016-41f3-b34a-1b1359bbea68)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/fb5d48ec-8655-497b-bbe0-b14550832a42)

 In directorul /app vom mai face un director cu numele tests :
`mkdir tests` Aici vom crea fisierul `test_biblioteca_filme.py` si vom crea functiile de testare, bfilme este fisierul importat din /lib – biblioteca_filme.py Pentru a vedea daca functioneaza testele, instalam pytest : `sudo apt install pip` `pip install pytest`
Pentru a rula testele local - pytest, folosim comanda (pentru python 3.10): `python3 -m pytest -v`

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/6da7d02a-22f1-4bb4-89fb-b98d850030a2)

Pentru a pune modificarile facute pe server in directorul /home/git/curs_vcgj_444D_flori vom da urmatoarele comenzi:
`git status` apoi `git add*` pentru a adauga fisierele in zona de staging apoi  `git commit -m “mesaj’` ,apoi 
`git push origin devel/LabesNarcis`
Pentru autentificare ne va cere credentialele.
$git config –global user.email(mail@domain.x) $git config –global user.name(name) $git config –credentials.helper store–username-ul si parola care va fi un token generat pe site, iar credentialele noastre vor fi salvate pentru acest repository.

# Testare cu Jenkins <img src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/e02d06e9-e06e-4e47-aabd-b42ae6a7c150"  width="53" height="43"> <img src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/e02d06e9-e06e-4e47-aabd-b42ae6a7c150"  width="53" height="43">



`sudo systemctl enable jenkins`,`sudo systemctl start jenkins`,`sudo systemctl status jenkins`

`http://localhost:8080/` - serverul de jenkins va fi accesat la aceasta adresa

Va fi instalat plugin ul Blue Ocean care ofera o interfata prietenoasa in cadrul careia vedem stage urile,erorile,mesajele.
Pentru testare automata cu Jenkins pipeline, vom avea nevoie de Jenkinsfile care este fisierul de configurare folosit pentru a defini si executa pipeline urile : 

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/f1a74a96-3f18-4a0d-8003-69fb20d5ed97)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/129889527/bd18325c-0e15-4ccb-95aa-b68a96e02bd4)

Pentru a rula automat, Jenkins-ul are nevoie de un Virtual Environment si de requirements.txt –care contine  programele cerute pentru a putea rula in venv.Un venv va fi local – activeaza_venv, iar celalalt pentru Jenkins pe server – activeaza_venv_jenkins.De asemenea, pentru a rula aplicatia pe server avem nevoie de alt fisier ruleaza_aplicatia.
Pentru a configura testarea automata apasam pe new build,punem nume si selectam pipeline apoi:
 
<img src="https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/2202a6a6-33f1-4f95-97dd-3041800c687e" alt="Screenshot 2023-05-23 215151" width="535" height="434">

Dam build apoi in Blue Ocean vom vedea toate stage urile ca in poza urmatoare:

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/3bb769ec-29ca-4ad6-a1e6-fe237c2fe73e )

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/e5a1185b-1762-4bb9-b99a-acb352957909)


Pentru orice modificare adusa codului va trebui sa facem din nou operatiunile git add,git commit,git push si apoi build.

# Containerizare cu docker

Vom avea nevoie de Dockerfile care va fi folosit pentru crearea contaierului cu aplicatia care  contine functionalitatea la care se lucreaza, o imagine, un fisier pentru a porni serviciul docker – dockerstart.sh 
Cream imaginea folosind `sudo docker build -t 441d_filme:v01`


![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/dd8eb449-2936-484e-9005-70abfd832725)

Rulam containerul folosind `sudo docker run –name 441d_filme -p 8020:5020 441d_filme:v01`:
Unde 8020 va fi portul de pe care poate fi accesata aplicatia din container 

Cu `sudo docker ps` putem vedea containerul:

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/e584de82-8ae6-4c2c-a33c-e19d5405126d)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/501afaef-741f-40c6-b33d-71972c52436d)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/24204707/806ad8a7-a628-4bb2-a689-a8839fa0d32b)



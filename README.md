Transporter, 2002, 6.8


  Initial, pe masina virtuala am instalat mai multe aplicatii, iar printre cele mai importante regasim: git, python3, python3-pip, pytest, docker, jenkins, gedit, vim.

  Pe desktop, am creat un folder cu numele git( mkdir git ), iar in acest folder am clonat repo-ul de pe GitHub cu ajutorul comenzii:

git clone https://github.com/Dragos-Calota/curs_vcgj_441D_filme.git

  Pentru a crea branch-ul personal am folosit comanda git branch devel/ConstantinSilvian
  Pentru a lucra pe branch-ul personal am folosit comanda git checkout devel/ConstantinSilvian
  
  Pe branch-ul personal am creat toate fisiere necesare proiectului:
        Folderul app ce contine:
- fisierul py 441D_filme.py unde avem toate functiile necesare


![poza1](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132925943/4cdad7f4-1651-4d2b-97a0-e88215a37ce6)
        
- folderul lib in interiorul caruia gasim un fisier denumit biblioteca_filme.py

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132925943/546bb065-ef4f-4eba-9103-280d616b5364)

-folderul test in interiorul caruia gasim un fisier denumit test_biblioteca_filme.py

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132925943/7ad304d7-f16c-430f-af56-c31917e2e4c1)

Rulam aplicatia 441D_filme.py din folderul app. Cu ajutorul aplicatiei Flask ni se vor afisa informatii despre numele filmului, rating si an lansare.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132925943/0a4c61ac-1b8f-408a-a981-b21cdbe3f4ec)


Cu ajutorul aplicatiilor pip si pytest deja instalate, apelam functiile de testare din fisierul test_biblioteca_filme.py care se regaseste in /app/tests .

Rulam comanda python3 -m pytest -v pentru a verifica testele.

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132925943/06fe0cd7-075c-4ba8-941c-7cbc714d6d3f)


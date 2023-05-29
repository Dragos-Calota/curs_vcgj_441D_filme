# curs_vcgj_441D_filme
Acest proiect implică crearea unei aplicații web Flask care va afișa informații despre filme. Se va utiliza mașina virtuală, Git și GitHub, Jenkins pentru a dezvolta și implementa aplicația.
Pentru început vom avea nevoie de mai multe programe instalate pe mașina virtuală cu Ubuntu : git, vscode,  python3, pytest, pip, jenkins.
Pentru acest proiect am avut nevoie de un director pe care l-am făcut pe Desktop cu comanda mkdir git în care să lucrez și să clonez de pe GitHub repository-ul https://github.com/Dragos-Calota/curs_vcgj_441D_filme cu comanda git clone https://github.com/Dragos-Calota/curs_vcgj_441D_filme
git branch devel/VerdesAlexandra - pentru a crea branch-ul personal și git checkout devel/VerdesAlexandra - pentru a trece pe branch-ul personal
După am creat fișierele necesare proiectului, cel mai important fiind 441D_filme.py ce conține rutele și în care voi apela funcțiile necesare.
Am creat în /Desktop/git/curs_vcgj_441D_filme alt director /app cu comanda mkdir app, iar în acest folder se află fișierele și codul aplicației. Am ales filmul “We Bought a Zoo”, deci am avut nevoie de funcțiile : an_lansare_We_Bought_a_Zoo() care va intoarce string-ul “2011”, rating_ We_Bought_a_Zoo () – care va intoarce “7.1”. Am creat în /Desktop/git/curs_vcgj_441D_filme/app un director /lib cu comanda mkdir lib. Am creat aici un fișier cu comanda touch biblioteca_filme.py unde am scris funcțiile.
Am creat în /Desktop/git/curs_vcgj_441D_filme/app un fișier cu comanda touch 441D_filme.py
Acum a putut să pornească aplicația 441D_filme.py cu ajutorul comenzii python3 441D_filme.py.Programul a pornit pe mașina locală pe localhost:5001
În directorul /app am mai creat un director cu comanda mkdir tests unde am creat un fișier cu comanda test_biblioteca_filme.py și am pus funcțiile de testare
Pentru a vedea dacă funcționează testele am folosit comanda python3 -m pytest -v.
Testare cu Jenkins
localhost:8080/ - serverul de jenkins va fi accesat la această adresă
Am instalat plugin-ul Blue Ocean care oferă o interfață prietenoasă în cadrul căreia putem vedea stage-urile, erorile, mesajele. Pentru testare automată cu Jenkins pipeline, am avut nevoie de Jenkinsfile care este fișierul de configurare folosit pentru a defini si executa pipeline-urile.
Pentru a rula automat, Jenkins are nevoie de un Virtual Environment și de requirements.txt care conține programele cerute pentru a putea rula în venv. Un venv este local – activeaza_venv, iar celălalt pentru Jenkins pe server – activeaza_venv_jenkins. De asemenea, pentru a rula aplicația pe server am avut nevoie de alt fișier ruleaza_aplicatia. Pentru a configura testarea automată am selectat new build, am pus nume, am selectat pipeline și apoi am pus repository URL si am specificat branch-ul meu.

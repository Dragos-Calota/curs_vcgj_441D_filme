##### Proiect VCGJ 441

    Acest proiect implica crearea unei aplicatii FLask care afiseaza informatii despre filme(anul aparitiei si ratingul de e 
    platforma IMDb) utilizandu-se tehnologii din industria software precum VM, Git, GitHUB si Docker pentru a dezvolta si 
    implementa aplicatia.
    
    In directorul app se vor afla fisieree si codul apliatiei. Primul fisier (care returneaza anul lansarii si ratingul):
    
 ![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/dac177e5-416a-4e54-9785-43f46c9ae68e)


   Aplicatia 441D_filme are urmatorul continut:
   ![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/446e05c4-da94-460e-b2f8-219558c5f99d)
    ![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/e92e1343-be3e-41ec-9925-d6d6e0a572b2)

   Aplicatia se porneste folosind comanda: python3 441D_filme.py
    ![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/37713485-d6cd-41a0-be68-81a6c6c4dd1a)

  
  Dupa rulare se va accesa link-ul in browser:
  
  ![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/aacf1ccf-c940-431e-8c77-7176eba3b95c)
  
  Pentru informatiile filmului se foloseste ruta '/' : "rating" si "an_lasare":
  ![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/d9e37a84-fb03-41d9-a8e0-9abcfc65e5cd)
  ![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/17290bc8-66b6-4d43-940a-c883206dd710)



Pentru a realiza testarea vom crea inca un director in directorul app(numit tests) care va contine fisierul 
test_biblioteca_filme.py

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/0f6923d8-7ae1-4e33-a66b-242582c5d083)

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/965b097e-5786-4619-9e28-78e115773612)




 

### Containerizare cu docker

Pentru a utiliza docker vom avea nevoie de Dockerfile care este folosit pentru a crea containerul cu aplicatia care contine 
functionalitatea. Vom crea imaginra folosind comanda: sudo docker build -t 441d_filme:v01 . :

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/93c6e78a-ad4d-400b-bc06-08c645bc348e)


Containerul se ruleaza folosind comanda : "sudo docker run --name 441d_filme -p 8020:5020 441d_filme:v01"
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/bf7d4eb8-1579-4bdf-b17e-af1373e70e9e)



Si se observa ca fuctioneaza corect:

![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/19ce9d3e-87bf-44a8-9d0c-fd8eef287011)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/6b3fc0a4-f0cb-4910-b364-8b909a75507e)
![image](https://github.com/Dragos-Calota/curs_vcgj_441D_filme/assets/132938214/7ef72656-2673-40b4-a5b8-30188e1093ac)



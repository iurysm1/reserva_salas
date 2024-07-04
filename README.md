Um sistema de reserva de cadeiras. Feito em DJango para a discplina de Desenvolvimento Web II.


Requisitos: ter python instalado.

Como usar:


- Crie um ambiente virtual dentro da pasta "reserva", executando o comando: py -m venv nome_do_ambiente_virtual;
- Ative o ambiente com o comando: nome_do_ambiente_virtual\scripts\activate;
- Instale os requirements com o comando: pip install -r requirements.txt;
- Faça as migrações do banco com os comando: py manage.py migrate | py manage.py makemigrations | py manage.py migrate main | py manage.py makemigrations main;
- Ative o server: py manage.py runserver;
- Agora é só acessar pelo navegador o endereço: localhost:8000 ou 127.0.0.1:8000.

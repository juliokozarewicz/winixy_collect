<h1 align="center">
  <br>
  <img src="images/logo.png" width="400">
  <br><br>
</h1>

<p align="center"> 
  <a href="https://www.linkedin.com/in/julioerk/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
  <a href="https://www.linkedin.com/in/julioerk/">
    <img src="https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white">
  </a>
  </a>
  <a href="https://www.linkedin.com/in/julioerk/">
    <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white">
  </a>
  <br>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white">
  </a>
  <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white">
  </a>
  <a href="https://www.postgresql.org/">
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
  </a>
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
  </a>
  <a href="https://docs.conda.io/en/latest/">
    <img src="https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white">
  </a>
  <br>
  <a href="https://www.gnu.org/distros/free-distros.html">
    <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
  </a>
  </a>
  <a href="https://archlinux.org/">
    <img src="https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white">
  </a>
  <a href="https://www.redhat.com/">
    <img src="https://img.shields.io/badge/Red%20Hat-EE0000?style=for-the-badge&logo=redhat&logoColor=white">
  </a>
  <a href="https://www.vim.org/">
    <img src="https://img.shields.io/badge/VIM-%2311AB00.svg?&style=for-the-badge&logo=vim&logoColor=white">
  </a>
</p>

# **Descri????o:**
O **WINIXY COLLECT** ?? um sistema de coleta de dados da bolsa de valores brasileira, a Brasil, Bolsa, Balc??o (B3). Sendo assim, tem como fun????o coletar dados em tempo real e dentro de uma janela de tempo mais r??pida que os segundos.

## **??rea de aplica????o:**
Mercado financeiro e de capitais, investimentos e outros.

## **Problema:**
Coletar dados de ativos em tempo real para fazer an??lises de investimentos no mercado de capitais.

## **Abordagem do problema:**
A coleta de dados ocorre atrav??s da utiliza????o de linguagem Python para se conectar com uma plataforma de investimentos, onde essa fornece os dados em tempo real. O sistema acessa esse servidor disponibilizado pela plataforma, coleta e envia os dados para uma data base.

## **Processos da aplica????o:**
Essa coleta de informa????es ocorre separadamente, uma fun????o salva os dados passados do ativo selecionado, faz um pr?? processamento e envia essas informa????es para uma tabela de banco de dados relacional local, o mesmo ocorre em rela????o ao times and trades e por ??ltimo uma outra fun????o ?? executada em um processo paralelo para armazenar informa????es do book de ofertas do ativo e atualizar um arquivo csv local. Tamb??m, o sistema foi programado para funcionar apenas no hor??rio definido, no caso o hor??rio em que o mercado est?? aberto, e para ser desligado nos finais de semana, em s??bados e domingos.


## **Algumas m??tricas:**

Quantidade de observa????es geradas por hora:
Mais de **8.000** mil linhas de informa????es.

Quantidade de observa????es geradas por dia:
Mais de **60.000** mil linhas de informa????es.

Quantidade de observa????es geradas por m??s:
Mais de **1.2 milh??es** de linhas de informa????es.

Quantidade de observa????es geradas por ano:
Mais de **15 milh??es** de linhas de informa????es.

> Informa????es para testes realizados em um computador desktop de configura????o mediana. Esses n??meros podem aumentar ainda mais caso seja utilizado uma m??quina mais robusta.

<br>

# **Demonstra????o**


## **M??dulo para monitorar o status e ter um feedback visual das informa????es b??sicas:**
<img src="images/visual.png" width="500"> <br /> <br />

## **Relat??rios e notifica????es por email:**

<img src="images/email.png" width="700"> <br /> <br />

## **Winixy Collect funcionando:**
Em breve...

<br>

# **Avalia????o do projeto:**
A coleta de dados ocorreu como o esperado, a aplica????o conseguiu fazer a captura????o das informa????es dentro da janela dos segundos e em tempo real. Por??m, deve-se levar em considera????o algumas limita????es, como por exemplo, a conex??o com o servidor que ocorre pelo protocolo TCP, causando assim uma certa lentid??o por causa da ocorr??ncia do Three-way Handshake, seria mais interessante se o servidor aceitasse o protocolo UDP.

Apesar disso, a coleta de dados da bolsa de valores brasileira atrav??s do Winixy Collect ?? bastante eficiente. Conseguiu-se atingir o objetivo principal do projeto, a partir desses dados coletados ser?? estimado modelos de predi????o de pre??os de ativos do mercado financeiro utilizando estat??stica para algoritmos de machine learning.

## **Utiliza????o:**
?? necess??rio um estudo pr??vio para descobrir como a plataforma de interesse ir?? disponibilizar a conex??o ou API para receber os dados da bolsa em tempo real. Tamb??m, cada plataforma disponibiliza sua ordem e tipo das tabelas, isso demanda um estudo e ser?? ??til para a cria????o do banco de dados, todas as configura????es est??o alocadas no arquivo "configs.py", depois de tudo ajustado ?? s?? executar o arquivo "connect.py".

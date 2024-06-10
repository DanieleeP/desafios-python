### Desafios de Programação
Este repositório contém exercícios de programação que devem ser resolvidos utilizando seus conhecimentos e a linguagem Python. 
Siga as instruções abaixo para configurar o projeto localmente, desenvolver suas soluções e enviar suas respostas 
via pull request.

### Pré Requisitos
* [Python](https://www.python.org/)
* [Git](https://git-scm.com/)

### Passo a Passo
#### 1. Fazer um Fork do Repositório
1. Vá para a página principal deste repositório no GitHub.
2. Clique no botão "Fork" no canto superior direito para criar uma cópia deste repositório em sua conta do GitHub.

#### 2. Clonar o repositório
```
git clone https://github.com/SEU-USUARIO/desafios-python.git
```

#### 3. Navegar até o diretório do projeto
```
cd desafios-python
```

#### 4. Criar um ambiente virtual
```
python -m venv .venv
```
#### 5. Ativar o ambiente virtual
```
.venv\Scripts\activate
```
#### 6. Instalar os requisitos
```
pip install -r requirements.txt
```
#### 7. Abrir no VsCode
```
code .
```
#### 8. Desenvolver os exercícios
Você encontrará os exercícios no diretório exercises. Cada arquivo representa um exercício. Edite esses arquivos para implementar suas soluções.
#### 9. Rodar os testes
Para garantir que as soluções estão corretas, execute os testes:<br>
* Para executar separadamente
```
cd tests
```
```
pytest test_nome_do_arquivo.py
```
* Para executar todos de uma vez
```
pytest
```
Certifique-se de que todos os testes passem antes de enviar sua submissão.
#### 10. Commit e Push
Depois de implementar suas soluções e garantir que todos os testes passaram, faça commit das suas mudanças e envie para o seu repositório no GitHub:
```
git add .
git commit -m "Solução dos exercícios"
git push origin main
```
#### 11.  Criar um Pull Request
Vá para a página do seu repositório forkado no GitHub.<br>
Clique no botão "Pull Request" para enviar suas mudanças para o repositório original.<br>
Preencha os detalhes do pull request e envie.

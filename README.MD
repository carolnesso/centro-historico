# Projeto avaliativo de computação gráfica

Trabalho avaliativo para realizar a modelagem 3D de um centro histórico de nossa preferência. Eu e minha dupla, Victor Ferro, escolhemos o [Cine Teatro Apolo](https://www.google.com/search?q=cine+teatro+apolo&source=lmns&bih=980&biw=1862&hl=pt-BR&sa=X&ved=2ahUKEwj6--7SqNP4AhWLKLkGHU8XCh8Q_AUoAHoECAEQAA) que fica localizado em Palmares - PE.

Estamos utilizando o PyOpenGL, PyGame e a modelagem foi feita com o Blender em sua versão 3.0.1. e o python3.

Para conseguirmos importar o nosso objeto modelado no Blender utilizamos uma função de leitura de wavefront que o pygame disponibiliza no [site](https://www.pygame.org/wiki/OBJFileLoader), onde utilizam uma versão anterior do python, para o [python3](https://github.com/yarolig/OBJFileLoader) é esse aqui.

- - -
## Rodando o projeto

Para rodar o projeto baixe o repositório e digite os seguintes comandos:
- Instalando as bibliotecas

``` 
    pip install -r requirements.txt
```
- Rodando o arquivo main

``` 
    python3 projeto.py
```
### Movimentando a modelagem
Para se mover na tela da modelagem utilizaremos apenas os botõs do mouse onde:
- Botão esquerdo do mouse é para rotacionar a câmera
- Botão direito do mouse é para movimentar a câmera 
- Scroll do mouse serve para dar zoom in e zoom out

Realizado por:

[@carolnesso](https://github.com/carolnesso)

[@victorferro](https://github.com/vsosmonteiro)

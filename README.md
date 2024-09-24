# Central de Atendimento ao Estudante v2

## Refatoração do projeto CAE 
Este repositório é uma **versão independente** do repositório **Cae_** que está em fase de **testes**. Uma vez que eu terminar de configurá-lo corretamente existirá apenas um repositório do projeto com 2 branchs diferentes.

## Objetivo
No projeto inicial, eu estava usando as seguintes tecnologias para o commit: `dj-static` `gunicorn` `heroku` para que projeto pudesse servir arquivos estáticos e de mídia. 

Entretanto, os arquivos quando publicados desta forma são perdidos após um período de tempo, toda vez que um dyno reseta no Heroku, ele faz com que eu perca todos os arquivos de mídia que eu tinha inserido no projeto em produção.

Este projeto visa uma alternativa diferente para servir os arquivos, utilizando `django-heroku` `boto3` `django-storages` `AWS S3` `Heroku`

Basicamente consiste em fazer com que os arquivos fiquem armazenados em um **bucket** do **S3** e sejam apresentados corretamente na aplicação **Heroku**. 

## Observação
Foi necessário refatorar o projeto pois agora estou fazendo o uso de `settings.py` de uma forma diferente; Consiste em criar um diretório para `settings/` com a seguinte estrutura:

    settings/
        base.py
        prod.py
        dev.py

Isso me permite ter controle da configuração do ambiente para **localhost** e para **produção**.

Se este repositório ainda existe isso significa que eu ainda estou buscando por uma solução consistente para configurar corretamente meu projeto.
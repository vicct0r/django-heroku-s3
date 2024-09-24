# Central de Atendimento ao Estudante v2

## Refatoração do Projeto CAE

Este repositório é uma **versão finalizada** do repositório [Cae_](https://github.com/vicct0r/Cae_), que foi anteriormente desenvolvido. Esta versão apresenta uma configuração otimizada para atender às necessidades do projeto.

## Objetivo

O projeto inicial utilizava as seguintes tecnologias: `dj-static`, `gunicorn` e `Heroku` para servir arquivos estáticos e de mídia. No entanto, os arquivos publicados desta forma eram perdidos após um período, toda vez que um dyno no Heroku era reiniciado, resultando na perda de todos os arquivos de mídia inseridos no projeto em produção.

Este projeto busca uma alternativa robusta para o armazenamento de arquivos, utilizando `django-heroku`, `boto3`, `django-storages`, `AWS S3` e `Heroku`. O objetivo é garantir que os arquivos sejam armazenados em um **bucket** do **S3** e apresentados corretamente na aplicação hospedada no **Heroku**.

## Estrutura de Configuração

Para melhor gerenciar as configurações de ambiente, o projeto foi refatorado para incluir um diretório `settings/` com a seguinte estrutura:

    settings/
        base.py
        prod.py
        dev.py


Essa organização permite um controle eficiente das configurações para **localhost** e **produção**.

## Observação

Se este repositório está ativo, significa que o projeto foi finalizado e está utilizando as tecnologias mencionadas de forma eficaz. Para visualizar a aplicação em funcionamento, você pode acessar o link abaixo:

[Aplicação CAE publicada](https://sistema-cae-v5-ecab78bbbd3c.herokuapp.com/)

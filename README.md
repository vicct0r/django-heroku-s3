# Central de Atendimento ao Estudante v2

## Refatoração do Projeto CAE

Este repositório é uma **versão em produção** do projeto [Cae_](https://github.com/vicct0r/Cae_), que foi previamente desenvolvido. Esta versão apresenta uma configuração otimizada para atender às necessidades do projeto.

## Objetivo

O projeto inicial utilizava as tecnologias `dj-static`, `gunicorn` e `Heroku` para servir arquivos estáticos e de mídia. No entanto, os arquivos publicados dessa forma eram perdidos após um período, sempre que um dyno no Heroku era reiniciado, resultando na perda de todos os arquivos de mídia inseridos na aplicação em produção.

Esta versão do projeto busca uma alternativa robusta para o armazenamento de arquivos, utilizando `django-heroku`, `boto3`, `django-storages`, `AWS S3` e `Heroku`. O objetivo é garantir que os arquivos sejam armazenados em um **bucket** do **S3** e apresentados corretamente na aplicação hospedada no **Heroku**.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento do sistema.
- **AWS S3**: Armazenamento de arquivos estáticos e de mídia.
- **Heroku**: Plataforma de hospedagem.
- **django-heroku**: Integração do Django com o Heroku.
- **boto3**: Biblioteca AWS SDK para Python.
- **django-storages**: Extensão para gerenciar o armazenamento de arquivos.

## Estrutura de Configuração

Para melhor gerenciar as configurações de ambiente, o projeto foi refatorado para incluir um diretório `settings/` com a seguinte estrutura:

```
settings/
├── __init__.py
├── base.py
├── local.py
└── production.py
```

Essa organização permite um controle eficiente das configurações para **localhost** e **produção**.

## Contribuições

### Diretrizes para Colaboração

Para aqueles que desejam contribuir com este projeto, é importante observar que há vários aspectos que precisam ser abordados. Atualmente, não disponho do diagrama atualizado que reflete a arquitetura do projeto. No entanto, existem várias áreas em que melhorias são bem-vindas:

- **Correção de Erros**: Identificação e correção de bugs na lógica do backend.
- **Responsividade**: Melhoria na apresentação visual e na experiência do usuário em diferentes dispositivos.
- **Performance**: Investigar e implementar maneiras de otimizar a resposta do sistema, visando uma redução no tempo de resposta.

### Instruções para Pull Requests

Caso você decida colaborar com o projeto, solicito que mantenha a organização nas suas contribuições. É essencial que você destaque:

- As principais alterações realizadas.
- Se houveram testes, por favor, inclua-os.
- Detalhes sobre os erros que você corrigiu e a lógica aplicada nas mudanças.

Essa abordagem facilitará a compreensão das suas contribuições e permitirá uma revisão mais eficiente.

## Observações

Se este repositório está ativo, significa que o projeto foi finalizado e está utilizando as tecnologias mencionadas de forma eficaz. Para visualizar a aplicação em funcionamento, você pode acessar o seguinte link:

[Aplicação CAE em produção](https://sistema-cae-v5-ecab78bbbd3c.herokuapp.com/)

## Tags

**Tags**: #Django #S3 #Heroku #django-storages #boto3 #armazenamento #gestão acadêmica #aplicação web #projeto finalizado

# Centro de Atendimento ao Estudante v2

## Refatoração do Projeto CAE

Este repositório é uma **versão de produção** do projeto [Cae_](https://github.com/vicct0r/Cae_) previamente desenvolvido. Esta versão apresenta uma configuração otimizada para atender às necessidades do projeto.

## Objetivo

O projeto inicial utilizava tecnologias como `dj-static`, `gunicorn` e `Heroku` para servir arquivos estáticos e de mídia. No entanto, os arquivos publicados dessa maneira eram perdidos após certo tempo, sempre que um dyno no Heroku era reiniciado, resultando na perda de todos os arquivos de mídia enviados para a aplicação em produção.

Esta versão do projeto busca uma alternativa robusta para armazenamento de arquivos utilizando `django-heroku`, `boto3`, `django-storages`, `AWS S3` e `Heroku`. O objetivo é garantir que os arquivos sejam armazenados em um **bucket S3** e exibidos corretamente na aplicação hospedada no **Heroku**.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento do sistema.
- **AWS S3**: Armazenamento para arquivos estáticos e de mídia.
- **Heroku**: Plataforma de hospedagem.
- **django-heroku**: Integração do Django com Heroku.
- **boto3**: SDK da AWS para Python.
- **django-storages**: Extensão para gerenciamento de armazenamento de arquivos.

## Estrutura de Configuração

Para gerenciar melhor as configurações de ambiente, o projeto foi refatorado para incluir um diretório `settings/` com a seguinte estrutura:



```
settings/
├── __init__.py
├── base.py
├── local.py
└── production.py
```

Essa organização permite um controle eficiente das configurações para os ambientes de **localhost** e **produção**.

## Contribuições

### Diretrizes de Colaboração

Para aqueles que têm interesse em contribuir com este projeto, é importante observar que há várias áreas que precisam de atenção. Atualmente, não possuo um diagrama atualizado que reflita a arquitetura do projeto. No entanto, há várias áreas onde melhorias são bem-vindas:

- **Correção de Bugs**: Identificar e corrigir problemas na lógica do backend.
- **Responsividade**: Melhorar a apresentação visual e a experiência do usuário em diferentes dispositivos.
- **Desempenho**: Investigar e implementar maneiras de otimizar os tempos de resposta do sistema e reduzir a latência.

### Instruções para Pull Request

Se você decidir contribuir com o projeto, certifique-se de que suas contribuições estejam bem organizadas. É essencial destacar:

- As principais mudanças que você fez.
- Se foram incluídos testes, forneça-os.
- Detalhes sobre os bugs que você corrigiu e a lógica por trás das mudanças.

Essa abordagem facilitará o entendimento das suas contribuições e permitirá um processo de revisão mais eficiente.

## Aviso Importante

O código atualmente está escrito em português, mas estou realizando uma transição parcial para o inglês para possibilitar a participação de novos colaboradores no projeto no futuro.

## Observações

Se este repositório está ativo, significa que o projeto foi concluído e está utilizando as tecnologias mencionadas de forma eficaz. Para ver a aplicação em ação, você pode visitar o seguinte link:

[Aplicação de Produção do CAE](https://sistema-cae-v5-ecab78bbbd3c.herokuapp.com/)


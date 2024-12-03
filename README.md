# Anotações


- Cosmic Python: https://www.cosmicpython.com/book/preface.html, Harry Percival & Bob Gregory
- Clean Architecture, Robert C. Martin
- Domaing-Driven Design, Eric Evans
- Implementing Domain-Driven Design, Vaugh Vernon
- Blog do Martin Fowler: https://martinfowler.com/

---

Combinação:

FastAPI:

Fornece uma base sólida para construir a lógica do sistema e APIs REST.
Rápido e escalável, ideal para backend.
Suporte a templates (como Jinja2) para renderização de páginas no servidor.

HTMX:

Permite criar interatividade e recursos dinâmicos diretamente no HTML usando atributos.
Evita a necessidade de frameworks como React ou Vue para interatividade simples.
Excelente para projetos onde o backend renderiza as páginas e o frontend precisa apenas de atualizações dinâmicas.

Tailwind CSS:

Facilita a criação de interfaces modernas e responsivas com classes utilitárias.
Evita escrever muito CSS customizado, acelerando o desenvolvimento.

Framework Web:

- FastAPI: Um framework moderno, rápido (alta performance) para construir APIs com Python baseado em padrões abertos. É especialmente bom para criar APIs RESTful e tem suporte nativo para documentação automática.

Bibliotecas:
asyncpg - https://magicstack.github.io/asyncpg/current/
(PostgreSQL assíncrono), o que pode melhorar o desempenho em consultas complexas e múltiplas conexões.

Documentação completa em português:
https://fastapidozero.dunossauro.com/


ORM (Object-Relational Mapping):
- SQLAlchemy: Oferece flexibilidade e poder para trabalhar com diversos bancos de dados relacionais.
- Alternativa: Peewee para um ORM mais leve e fácil de usar.

Tarefas assíncronas e agendamento:
- Celery: Para processamento assíncrono de tarefas, como o processamento em lote de documentos.
- APScheduler: Para agendar tarefas recorrentes, como atualizações automáticas ou notificações.

Validação de dados:
- Pydantic: Para validação de dados e configurações, especialmente útil com FastAPI.

Segurança:
- python-jose: Para implementar JWT (JSON Web Tokens) para autenticação.
- passlib: Para hash e verificação de senhas.
- PyJWT: 

Testes:
- pytest: Framework de teste poderoso e fácil de usar.

Documentação:
- Swagger UI (integrado com FastAPI) ou Flask-RESTX: Para documentação interativa da API.

4. Integração de IA para Leitura de PDFs e Preenchimento de Formulários:
- OCR e extração de texto: Tesseract.js (biblioteca de código aberto para OCR)
- Processamento de linguagem natural: spaCy ou NLTK
- Framework de IA: TensorFlow.js ou ONNX.js para execução de modelos no navegador

Para recursos de IA e bancos de dados vetoriais:

- Banco de dados vetorial: 
Pinecone (Free tier)

Milvus (Open source) (otimizados para consultas de similaridade em alta dimensão):
  https://github.com/milvus-io/bootcamp/blob/master/bootcamp/tutorials/integration/rag_with_milvus_and_llamaindex.ipynb

  https://github.com/milvus-io/bootcamp/blob/master/bootcamp/tutorials/quickstart/build_RAG_with_milvus.ipynb


Modelos para textos jurídicos - 

BERTimbau (Large)
- Desenvolvido especificamente para o português brasileiro
- Treinado em um grande corpus de textos jurídicos e gerais
- Bom desempenho em tarefas de NLP em português

LegalBERT-PT
- Adaptação do BERT para o domínio jurídico em português
- Treinado em textos legais, o que pode ser muito relevante para contratos

XLM-RoBERTa (Large)
- Modelo multilíngue com excelente desempenho em português
- Capaz de lidar com documentos longos

BERT Multilingual (Base ou Large)
- Bom desempenho em várias línguas, incluindo português
- Pode ser fine-tuned para o domínio jurídico

Javascript:

https://www.npmjs.com/package/pdf-parse
https://mozilla.github.io/pdf.js/

autenticação do usuário:

Keycloack

Autenticação
Gereciamento de usuários - User profiles
Controle de acesso


https://www.keycloak.org/

Json Webserver
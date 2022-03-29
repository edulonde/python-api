FROM python:3-alpine as base
# criação de um diretórios
RUN mkdir /install
# mudança do diretório vigente para o diretório /install
WORKDIR /install
# cópia do arquivo de dependencias da app
COPY ./requirements.txt /requirements.txt
# instalação das dependencias através do pip em um diretório
RUN pip install --prefix=/install -r /requirements.txt
# Cria um novo estágio
FROM base
# copia arquivos da imagem base recém criada
COPY --from=base /install /usr/local/
# copiar a aplicação para o container
COPY . /app
# define o diretório de trabalho
WORKDIR /app
# expõe a porta do container
EXPOSE 5000
# Variáveis de ambiente
ENV MONGODB_USER=python
ENV MONGODB_URI=localhost
ENV MONGODB_PASSWD=qwe123qwe
# Execução
CMD python app.py
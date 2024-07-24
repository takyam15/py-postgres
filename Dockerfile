FROM python:3.12
ARG DIR_WORK=/work
WORKDIR ${DIR_WORK}
COPY requirements.txt ${DIR_WORK}/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Usage: docker build -t audiocodes/rasa:2.8.26 .
FROM rasa/rasa:2.8.26
USER root
RUN pip install --upgrade pip
RUN pip install rasa-audiocodes
USER 1001

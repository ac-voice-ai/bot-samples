# Usage: docker build -t audiocodes/rasa:1.10.15 .
FROM rasa/rasa:1.10.15
USER root
RUN pip install --upgrade pip
RUN pip install rasa-audiocodes
USER 1001

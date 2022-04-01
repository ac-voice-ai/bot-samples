# Usage: docker build -t audiocodes/rasa:3.1.0 .
FROM rasa/rasa:3.1.0
USER root
RUN pip install --upgrade pip
RUN pip install rasa-audiocodes
USER 1001

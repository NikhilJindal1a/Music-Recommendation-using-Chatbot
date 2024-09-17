FROM python:3.9.9-slim
WORKDIR /app
COPY requirement.txt /app
RUN pip install -r requirement.txt
# RUN python training.py
CMD python backend/output_chatbot.py 

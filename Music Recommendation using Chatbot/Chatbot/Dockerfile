FROM python:3.8.16-slim
WORKDIR /app
COPY requirement.txt /app
RUN pip install -r requirement.txt
EXPOSE 3000
CMD python chatbot.py 

# docker run -v $(pwd):/chatbot -d ab8f64eda96a
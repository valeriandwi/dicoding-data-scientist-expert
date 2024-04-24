FROM python:3.9-slim
 
COPY . /app
WORKDIR /app
 
RUN pip3 install numpy pandas scipy scikit-learn==1.2.2 joblib==1.3.1 streamlit==1.24.0
 
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
 
ENTRYPOINT ["streamlit", "run", "credit_scoring_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
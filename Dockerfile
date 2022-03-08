FROM python
EXPOSE 8087
WORKDIR /app
COPY requirements.txt backend.py frontend.py ./
RUN pip install -r requirements.txt
CMD ["python","frontend.py"]



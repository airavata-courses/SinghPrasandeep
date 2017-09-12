FROM python:3.4-alpine
ADD . /python
WORKDIR /python
RUN pip install -r requirements.txt
EXPOSE 5000 15672
CMD ["python", "api.py"]

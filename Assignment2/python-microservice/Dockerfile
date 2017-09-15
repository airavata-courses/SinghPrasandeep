FROM python:3.4-alpine
ADD . /python
WORKDIR /python
RUN pip install -r requirements.txt
EXPOSE 5000 15672 5672 5671
CMD ["python", "api.py"]

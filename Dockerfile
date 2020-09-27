FROM python:3.6-slim-buster
# RUN apt-get update && apt-get install -y g++
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt --use-feature=2020-resolver

COPY ./ /app/

# ENTRYPOINT ["python"]
# CMD ["app.py"]

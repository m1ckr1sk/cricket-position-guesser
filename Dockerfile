FROM python:3.9-slim

RUN apt-get update && apt-get upgrade -y && apt-get clean

COPY ./pyproject.toml /pyproject.toml
COPY ./LICENSE /LICENSE
COPY ./cricketpositionguesser /cricketpositionguesser
COPY ./api /api

RUN pip install --upgrade pip
RUN pip install --no-cache-dir .

CMD ["fastapi", "run", "api/api.py", "--port", "80"]
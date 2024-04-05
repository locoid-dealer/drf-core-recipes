# Ref. https://hub.docker.com/_/python
FROM python:3.11.6

WORKDIR /app

# Ref. https://docs.python.org/ja/3/using/cmdline.html#envvar-PYTHONPATH
# Ref. https://dev.classmethod.jp/articles/pythonpath-be-careful/
ENV PYTHONPATH /app

# Ref. https://docs.python.org/ja/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
# Ref. https://devlights.hatenablog.com/entry/2018/02/23/124719
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip \
&& pip install poetry

RUN poetry config virtualenvs.create false

COPY src/pyproject.toml pyproject.toml
RUN poetry install

CMD ["bash"]
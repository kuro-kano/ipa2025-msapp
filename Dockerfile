FROM python
RUN pip install --no-cache-dir --progress-bar=off flask

COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY app.py /home/myapp/

EXPOSE 8080
CMD python /home/myapp/app.py

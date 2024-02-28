FROM python:bullseye

WORKDIR /projects
# закидываем requirements.txt в первую очередь
ADD requirements.txt ./ourapp/requirements.txt
# заходим в директорию
WORKDIR /projects/ourapp
# устанавливаем все зависимости
RUN pip3 install -r requirements.txt
# и только потом закидываем остальные файлы (в данном случае 1 файл)
ADD flask-hw.py flask-hw.py

ENTRYPOINT [ "python3", "flask-hw.py" ]

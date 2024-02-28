# Flask hello world with docker

## Без докера
```bash
pip3 install -r requirements.txt
python3 flask-hw.py
# доступно здесь: http://127.0.0.1:4566/
```

## С докером
```bash
docker build -t flaskhw -f Dockerfile .
docker run -p 7777:4566 -it flaskhw
# доступно здесь: http://127.0.0.1:7777/
```

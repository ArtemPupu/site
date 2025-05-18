from site1 import app1
from site2 import app
from threading import Thread

def run_app1():
    app1.run(port=5000)

def run_app2():
    app.run(port=5001)

if __name__ == '__main__':
    Thread(target=run_app1).start()
    Thread(target=run_app2).start()
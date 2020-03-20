from app import flask_app


mobileip="192.168.43.45"
localip="127.0.0.1"

if __name__ == "__main__":
    flask_app.run(host = mobileip,port = 5050,debug = 1)
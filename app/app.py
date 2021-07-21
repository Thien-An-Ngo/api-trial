from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        'hello': 'hello'
    })


def main():
    app.run()


if __name__ == "__main__":
    main()

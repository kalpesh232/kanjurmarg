from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'HEAD'])
def example():
    response_body = "This is the response body for the GET request."
    print('request.method : ', request.method)
    if request.method == 'HEAD':
        # For a HEAD request, return only the headers without the body
        return '', 200, {'Content-Length': len(response_body)}

    # For a regular GET request, return both headers and the response body
    return response_body

if __name__ == '__main__':
    app.run(debug=True)

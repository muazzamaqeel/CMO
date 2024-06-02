from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='assets', template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
    if filename.startswith('assets/'):
        return send_from_directory('assets', filename[len('assets/'):])
    elif filename.startswith('forms/'):
        return send_from_directory('forms', filename[len('forms/'):])
    else:
        return render_template(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

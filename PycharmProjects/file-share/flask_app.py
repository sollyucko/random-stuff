"""
We'll render HTML templates and access data sent by POST using the request object from flask. Redirect and url_for
will be used to redirect the user once the upload is done and send_from_directory will help us to send/show on the
browser the file that the user just uploaded.
"""

from os import path, listdir, remove
from os.path import splitext

from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': '98ru98eriuy76t5ouhy76tTtridkjgfhrey7fiutj4398gtju4598t45uti094i04fk49it4598tu4598vtu4509vtu4598vtu458vtu4598vtu4598tu498gtu45t45j9i4jgjgtijgtg45jg4igivgj45igj5igj45oigjeioythjit87rhiufthuDYGTRTyug763giuyt67oijfje98tjgkrkytporigfthRytruoitroiritr09tirt09eite09ite09tir',
    'UPLOAD_FOLDER': 'uploads',
    'ALLOWED_EXTENSIONS': {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'},
})


def file_is_allowed(filename):
    return splitext(filename) in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/files')
def show():
    return render_template('files.html', files=listdir('uploads'))


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    
    if not file:
        return redirect('/')
    
    filename = secure_filename(file.filename)
    
    if not file_is_allowed(filename):
        flash('Invalid file type')
        return redirect('/')
    
    file_path = path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    flash(f'File {filename} uploaded successfully!')
    return redirect('/')


# This route is expecting a parameter containing the name of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads an image, that image is going to be show after the
# upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/edit/<filename>', methods=['GET', 'POST'])
def edit(filename):
    if request.method == 'POST':
        with open('uploads/' + filename, 'w+') as f:
            file_data = f.read()
            f.write(request.form['text'])
        
        return render_template('edit.html', file=file_data, filename=filename)
    else:
        with open(path.join('uploads', filename)) as f:
            file_data = f.read()
        
        return render_template('edit.html', file=file_data, filename=filename)


@app.route('/delete/<filename>')
def delete_file(filename):
    remove(path.join('uploads', filename))
    return redirect(url_for('show'))

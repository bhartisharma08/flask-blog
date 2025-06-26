from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for blog posts
posts = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    posts.append({'title': title, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


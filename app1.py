#   app.py

from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

aplication = app.app
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    import uvicorn
    uvicorn.run("main:application", host="0.0.0.0", port=8000, reload=True)

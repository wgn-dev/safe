import string
import random
from cari import *
from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Flask, jsonify, request, redirect
#from faunadb import query as q
#from faunadb.objects import Ref
#from faunadb.client import FaunaClient
import json
app = Flask(__name__)
#client = FaunaClient(secret="your-secret-here")


def generate_identifier(n=6):
    return "".join(random.choice(string.ascii_letters) for _ in range(n))


@app.after_request
def add_header(r):

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method != 'POST':
        return render_template('index.html')
    url = request.form['url']
    if not url:
        flash('The URL is required!')
        return redirect(url_for('index'))
    #short_url = request.host_url + hashid
    identifier = generate_identifier()
    db = f"{identifier} - {url}"
    with open(f"db/{identifier}", "w") as f:
        f.write(db)
        f.close()
    short_url = request.url + identifier

    return render_template('index.html', short_url=short_url)




@app.route("/<string:key>")
def gas(key):
    #a = menuju(key)
    link = tautan(key)
    #return link
    #return redirect(link)
    return render_template('ads.html', link=key)



@app.route("/go/<string:key>")
def gas2(key):
    #a = menuju(key)
    link = tautan(key)
    #return link
    #return redirect(link)
    return render_template('ads2.html', link=link)

    


@app.route("/gen")
def gen():
    url = request.args.get('url')
    identifier = generate_identifier()
    db = f"{identifier} - {url}"
    with open(f"db/{identifier}", "w") as f:
        f.write(db)
        f.close()
    link = tautan(identifier)
    pp = {
            "key" : identifier,
            "url" : link,
            }
    return jsonify(pp)

@app.route("/api")
def generate():
    url = request.args.get('url')
    identifier = generate_identifier()
    db = f"{identifier} - {url}"
    with open(f"db/{identifier}", "w") as f:
        f.write(db)
        f.close()
    link = tautan(identifier)
    pp = {
            "key" : identifier,
            "url" : link,
            }
    #return jsonify(pp)
    return redirect("/" + identifier)

    #shortened_url = request.host_url + identifier
    #return jsonify({"identifier": identifier, "shortened_url": shortened_url})


if __name__ == "__main__":
    app.run(debug=True, port="5000")

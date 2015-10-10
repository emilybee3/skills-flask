from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application-form")
def application_form():
    """show application form page"""
    
    return render_template("application-form.html")

@app.route("/application")
def application_submitted():
    first = request.args.get("firstname")
    last = request.args.get("lastname")
    pos = request.args.get("position")
    sal = request.args.get("salary")

    return render_template("application-response.html", firstname=first, lastname=last, position=pos, salary=sal)

if __name__ == "__main__":
    app.run(debug=True)

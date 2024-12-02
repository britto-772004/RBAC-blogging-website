from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

#landing page 
@app.route("/")
def landing_page():
    return render_template("landing_page.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/blogs",methods =["POST"])
def blog_foremail():
    email = request.form.get("email")
    print("email =>",email)
    if (email == "michaeljohnbritto772004@gmail.com"):
        return render_template("blog.html")
    return render_template("normal-blog.html")

if (__name__ == "__main__"):
    app.run(debug=True)
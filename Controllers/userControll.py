

@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if not email or not password:
        print("eksik bilgi")
    else:
        user = User.query.filter_by(email=email,password=password).first()
        login_user(user)
        print("giris yapildi")
        return render_template("home.html")
    return render_template("index.html")


@app.route("/signup" , methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    if not username or not email or not password :
        print("eksik bilgi")
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        print("already exists")
        return render_template("index.html")
    else:
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return render_template("home.html")
        print("kayit olundu")

    return render_template("index.html")


@app.route("/logout",methods=['GET'])
def logout():
    logout_user()
    return redirect('/')
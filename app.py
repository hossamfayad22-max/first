from flask import Flask,request,render_template,redirect,url_for
import random
import string
import database
import datab_st
alpha=string.ascii_letters+string.digits+string.punctuation+" "
alpha=list(alpha)
shuffled=alpha.copy()
random.shuffle(shuffled)


app=Flask("__name__")
@app.route("/",methods=["GET","POST"])
def homeo():
    return render_template('signup.html')

@app.route("/signup",methods=["GET","POST"])
def home():
    if request.form.get('username'):
        username = request.form.get('username')
        database.user_names.append(username)
    if request.form.get('password'):
        password=request.form.get('password')
        enc_pass=""
        for i in password:
            enc_pass+=shuffled[alpha.index(i)]
        database.passwords.append(enc_pass)
    if request.method == "POST":
        return redirect(url_for("homee"))    
    print("added")
    return render_template('signup.html')


@app.route("/signin",methods=["GET","POST"])
def homee():
    if request.method == "POST":
        u=request.form.get('usernamee')
        p=request.form.get('passwordd')
        e=""
        for i in p:
                if i in alpha:
                    e+=shuffled[alpha.index(i)]    
        if e in database.passwords and u in database.user_names:
            return render_template("index1.html")
        return render_template('false.html')     
    return render_template('signin.html')   
@app.route('/add', methods=["GET","POST"])
def add():
    if request.method=="POST":
        student=request.form.get("student")
        datab_st.students.append(student)
        print("added succes")
    return render_template("index2.html",students=datab_st.students)
@app.route('/edit', methods=["GET","POST"])
def edit():
    if request.method=="POST":
        if request.form.get("delete_student"):
            student=request.form.get("delete_student")
            if student in datab_st.students:
                datab_st.students.remove(student)
            if student in datab_st.present:
                datab_st.present.remove(student)
                print("removed succes")
        if request.method=="POST":
                student=request.form.get("xyz")
                datab_st.present.append(student)
    return render_template("index1.html", students=datab_st.students , present=datab_st.present)        

if __name__=="__main__":
    app.run(debug=True)
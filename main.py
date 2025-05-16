from flask import Flask, render_template, request, url_for,redirect

app = Flask(__name__)

usuarios = []
id_contador =1





@app.route("/", methods=["GET", "POST"])
def crud():
    global id_contador

    if request.method=='POST':
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        usuarios.append({"id":id_contador, "username": nombre, "email": email }) #insertando un usuario
        id_contador +=1
        return redirect(url_for("crud"))#llamar nombre de la funcion

    id_eliminar=request.args.get("borrar")
    if id_eliminar:
            #TODO: eliminar el usuario con el id del parametro de la lista
            for item in usuarios:
                if str(item['id'])==id_eliminar:
                    usuarios.remove(item)
                    break
            return redirect(url_for("crud"))# LLLAMAR NOMBRE DE LA FUNCION

    return render_template("registro.html", usuarios=usuarios) # lista que entregamos al html




if  __name__ == "__main__":
    app.run(debug=True)

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

@app.route("/update/<int:id>", methods=["GET", "POST"]) #Ruta  con parametros 
def update(id):

    estudiante_a_editar='' 
     #TODO: indentificar el diccionario del usuario con id entregad
    for diccionario in usuarios:
        if diccionario['id']==id:
            estudiante_a_editar=diccionario
            print("el estudiante a editar  es:", estudiante_a_editar)
            break

    if request.method=='POST':
            #TODO: actualizar el diccionario dle estudiantes con los datos del formulario
            estudiante_a_editar['username']=request.form.get('username')
            estudiante_a_editar['email']=request.form.get('email')
            return redirect(url_for('crud'))


            return redirect(url_for("crud"))     
    #si despues de recorrer ttoda la lista, no encontramos el id entregado 
    if estudiante_a_editar=='':
        return f"no exsite el usuario con id: {id}" #Salgo de la funcion
                   
    return render_template("editar.html",estudiante_a_editar=estudiante_a_editar)

if  __name__ == "__main__":
    app.run(debug=True)

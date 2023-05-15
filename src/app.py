from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)
conexion = MySQL(app)

@app.route('/clientes', methods=['GET'])
def listar_clientes():
  try:
    cursor = conexion.connection.cursor()
    sql = "SELECT * FROM cliente"
    cursor.execute(sql)
    datos = cursor.fetchall()
    clientes=[]
    for fila in datos:
      cliente = {'codigo':fila[0],'nombre':fila[1],'apellido':fila[2],'direccion':fila[3]}
      clientes.append(cliente)
    return jsonify({'clientes':clientes, 'mensaje':"Clientes registrados"})
  except Exception as ex:
    print (ex)
    return jsonify({'mensaje':"Error"})
    
@app.route('/clientes/<codigo>', methods=['GET'])
def leer_cliente(codigo):
  try:
    cursor=conexion.connection.cursor()
    sql="SELECT * FROM cliente WHERE codigo = '{0}'".format(codigo)
    cursor.execute(sql)
    datos = cursor.fetchone()
    if datos != None:
      curso={'codigo':datos[0], 'nombre':datos[1], 'apellido':datos[2],
    'direccion':datos[3], 'telefono':datos[4], 'email':datos[5]}
      return jsonify({'cliente':cliente, 'mensaje':"Cliente encontrado"})
    else:
      return jsonify({'Mensaje': "Cliente no encontrado"})
  except Exception as ex:
    return jsonify({'Mensaje': "Error"})
    
@app.route('/clientes',methods=['POST'])
def registrar_cliente():
  #print(request.json)
  try:
    cursor=conexion.connection.cursor()
    sql = """INSERT INTO cliente (codigo, nombre, apellido, direccion, telenono,
    email)
    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}'
    )""".format(request.json['codigo'],request.json['nombre'],request.json['apellido'],request.json['direccion'], request.json['telefono'], request.json['email'])
    cursor.execute(sql)
    conexion.connection.commit()
    return jsonify({'Mensaje': "Cliente registrado"})
  except Exception as ex:
    return jsonify({'Mensaje': "Error."})
    
@app.route('/clientes/<codigo>',methods=['DELETE'])
def eliminar_cliente(codigo):
  try:
    cursor=conexion.connection.cursor()
    sql = "DELETE FROM cliente WHERE codigo = '{0}'".format(codigo)
    cursor.execute(sql)
    conexion.connection.commit()
    return jsonify({'Mensaje': "Cliente eliminado"})
  except Exception as ex:
    return jsonify({'Mensaje': 'Error'})
    
@app.route('/clientes/<codigo>',methods=['PUT'])
def actualizar_cliente(codigo):
  try:
    cursor=conexion.connection.cursor()
    sql = """UPDATE cliente SET nombre = '{0}', apellido = '{1}', direccion = '{2}',
    telefono = '{3}', email = '{4}' WHERE codigo
    ='{2}'""".format(request.json['nombre'],request.json['apellido'],
    request.json['direccion'],request.json['telefono'], request.json['email'],
    codigo)
    cursor.execute(sql)
    conexion.connection.commit()
    return jsonify({'Mensaje': "El cliente ha sido actualizado"})
  except Exception as ex:
    return jsonify({'Mensaje': "Error"})
    
def pagina_no_encontrada(error):
  return "<h1>Página no encontrada </h1>", 404

if __name__ == '__main__':
  app.config.from_object(config['development'])
  app.register_error_handler(404, pagina_no_encontrada)
  app.run()

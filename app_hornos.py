#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#import psycopg2
import cx_Oracle
import random,threading,time,datetime




def elaboracionDePan(horno, producto,cantidad):

# crear conexión con la db para insertar la query
	con = cx_Oracle.connect('developer/developer@192.168.0.32/xe')
	cur = con.cursor()
	statement = 'insert into produccion_horno(num_horno, id_prod,cantidad) values (:2, :3, :4)'
	cur.execute(statement, (horno, producto,cantidad))
	con.commit()
	cur.close()
	con.close()




# #conexión a la base de datos postgres
# 	conn = psycopg2.connect("dbname=db_proyecto user=developer password=developer")
# #Abrir cursor de la base de datos
# 	cur = conn.cursor()
# #preparación de query para ejecutar
# 	cur.execute("INSERT INTO log_horno (id_horno, id_prod,cantidad) VALUES (%s, %s,%s)",
# 	(horno, producto,cantidad))
# #confirmar query
# 	conn.commit()
# #cerrar cursor y conexión
# 	#cur.close()
# 	#conn.close()


######################################################################
#Explicación de libreria random
#creación de número aleatorio entre 1 y 2 para designar el horno
#horno 		= random.randint(1, 2)
#creación de número aleatorio entre 1 y 3 para designar el producto
#producto 	= random.randint(1, 3)
#print 'cantidad :',int(random.uniform(30, 50))
#cantidad 	= int(random.uniform(30, 50))
######################################################################



def horno1():
	horno 		= "1"
	producto 	= random.randint(1, 3)
	cantidad 	= int(random.uniform(30, 50))
	elaboracionDePan(horno, producto,cantidad)
	hora = datetime.datetime.now()
	print hora," -","HORNO Nº",horno, "ID PROD:",producto, "TOTAL ELAB:", cantidad
	time.sleep(0)

def horno2():
	horno 		="2"
	producto 	= random.randint(1, 3)
	cantidad 	= int(random.uniform(30, 50))
	elaboracionDePan(horno, producto,cantidad)
	hora = datetime.datetime.now()
	print hora," -","HORNO Nº",horno, "ID PROD:",producto, "TOTAL ELAB:", cantidad
	time.sleep(0)

#Hilos de creación de elaboración de pan



def hilos():
	t1 = threading.Thread(horno1())
	t2 = threading.Thread(horno2())
	t1.start
	t2.start


        
# Elaboración de 16 horneadas (elaboración aprox. 30 min por 8 horas laborales)
count = 0
while count < 16:
   hilos() 
   count = count + 1
   time.sleep(180)





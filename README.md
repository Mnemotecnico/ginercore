# Ginercore

Pseudo-proyecto de código abierto para el desarrollo de una interfaz gráfica enfocada al manejo de información comercial. La función principal del programa es el manejo de inventario, registro de transacciones y la realización de los respectivos modelos estadísticos para generar conclusiones con respecto a la información tratada. 


## Estructura

Todavía no es ni una pre-alpha funcional, así que no entraré en detalles todavía.

## Dependencias

mysql-connector-python (no usar mysql-connector)
tkinter (Generalmente instalado por defecto con python)

## Base de datos

Tabla productos
CREATE TABLE productos (productID int NOT NULL AUTO_INCREMENT, codigo_barras varchar(64), nombre varchar(255), existencias int NOT NULL, precio_compra float, precio_venta float, ubicacion VARCHAR(255), PRIMARY KEY (productID));

ALTER TABLE productos AUTO_INCREMENT=10100;

Tabla transacciones
CREATE TABLE transacciones (transactionID int, productID int, cantidad int);

Tabla logsell
CREATE TABLE logsell (transactionID INT NOT NULL AUTO_INCREMENT, fecha DATETIME NOT NULL, PRIMARY KEY (transactionID));
ALTER TABLE logsell AUTO_INCREMENT=10100;

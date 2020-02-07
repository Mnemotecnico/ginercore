# Ginercore

Pseudo-proyecto de código abierto para el desarrollo de una interfaz gráfica enfocada al manejo de información comercial. La función principal del programa es el manejo de inventario, registro de transacciones y la realización de los respectivos modelos estadísticos para generar conclusiones con respecto a la información tratada. 


## Estructura

Todavía no es ni una pre-alpha funcional, así que no entraré en detalles todavía.

## Dependencias

mysql-connector-python (no usar mysql-connector, está obsoleto)

## Base de datos

CREATE TABLE productos (productID int NOT NULL AUTO_INCREMENT, codigo_barras varchar(64), nombre varchar(255), existencias int NOT NULL, precio_compra float, precio_venta float, last_sale DATE, ulocus int, PRIMARY KEY (productID));
ALTER TABLE productos AUTO_INCREMENT=10100;
CREATE TABLE transacciones (productID int, cantidad int, fecha DATE);

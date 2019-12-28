Dependencias~

mysql-connector

Base de datos~

CREATE TABLE productos (productID int NOT NULL AUTO_INCREMENT, codigo_barras varchar(64), nombre varchar(255), existencias int NOT NULL, precio_compra float, precio_venta float, last_sale DATE, ulocus int, PRIMARY KEY (productID));
ALTER TABLE productos AUTO_INCREMENT=10100;
CREATE TABLE transacciones (productID int, cantidad int, fecha DATE);
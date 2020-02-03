#!/usr/local/bin/python
# This class need <pip install mysql-connector-python>
import mysql.connector
import datetime

class Ginerdata(object):
    """
    Esta clase tendrá métodos que interactuan con la base de datos MySQL y entregará esos datos
    Para inicializar se debera meter user=, host=, password=, database=
    """

    def __init__(self, user, host, password, database):
        self.user = user
        self.host = host
        self.password = password
        self.database = database

    # La siguiente función debe incluir a futuro encriptación SSL
    def connectDatabase(self):
        return mysql.connector.connect(
            user=self.user,
            host=self.host,
            passwd=self.password,
            database=self.database
        )


    def registrarTransaccion(self, datos):
        """
        Este método registrará los datos de la venta en la tabla "transacciones"
        :param datos: Lista de tuplas de la forma (productID, cantidad, fecha)
        """

        # Se conecta con la base de datos
        sqlConnection = self.connectDatabase()
        sqlCursor = sqlConnection.cursor()

        QueryTransacciones = "INSERT INTO transacciones (transactionID, productID, cantidad, fecha) VALUES (%s, %s, %s, %s)"
        QueryBlockTransacciones = "INSERT INTO logsell (fecha) VALUES (%s)"

        sqlCursor.execute(QueryBlockTransacciones, datos[0][-1])
        sqlConnection.commit()

        sqlCursor.executemany(QueryTransacciones, datos)
        sqlConnection.commit()

        sqlConnection.close()

    def buscarProductos(self, parametro):
        """
        Método para buscar elementos de la tabla "productos"
        :param parametro: Es una cadena de texto que servirá como parámetro de búsqueda
        :return: Retornará una lista de tuplas con todos los valores de las columnas para cada fila que incluya el parametro
        """

        # El parametro se fraccionara por cada espacio que contenga
        newparams = parametro.split(' ')

        # Se eliminaran espacios de newparams y vocales solas
        while '' in newparams:
            newparams.pop(newparams.index(''))

        # Se conecta con la base de datos
        sqlConnection = self.connectDatabase()
        sqlCursor = sqlConnection.cursor()

        # Cadenas de consultas
        qProductID = "SELECT * FROM productos WHERE productID = %s"
        qCodigo_barras = "SELECT * FROM productos WHERE codigo_barras = %s"
        qNombre = "SELECT * FROM productos"

        SearchAdvance = False
        if len(newparams) == 1:  # Verifica que la lista de parametros solo contenga un elemento
            # Este condicional servirá para buscar en <ProductID> o <codigo_barras>
            sqlCursor.execute(qProductID, newparams)
            IDresult = sqlCursor.fetchall()

            if len(IDresult) == 0:  # Dice que no hay resultado para ese <ProductID> Y se buscará en codigo_barras
                sqlCursor.execute(qCodigo_barras, newparams)
                Barrasresult = sqlCursor.fetchall()
                if len(Barrasresult) == 0:
                    SearchAdvance = True
                else:
                    sqlCursor.close()
                    sqlConnection.close()
                    return Barrasresult
            else:
                sqlCursor.close()
                sqlConnection.close()
                return IDresult

        if SearchAdvance or len(newparams) > 1:  # Este bloque buscará nombres de productos
            sqlCursor.execute(qNombre)
            ProductsResult = sqlCursor.fetchall()

            # Convertira las tuplas de los datos en lista y añadirá al final un contador con valor 0
            for index in range(len(ProductsResult)):
                ProductsResult[index] = list(ProductsResult[index])
                ProductsResult[index].append(0)

            # Modificara el contador segun el numero de aciertos que haya en cada nombre con newparams
            for product in ProductsResult:
                for param in newparams:
                    if param.lower() in product[2].lower():
                        product[-1] += 1

            # Por hacer -<fl
            #   * Ordenar ProductResult en orden decreciente por el ultimo valor y eliminarlo
            #   *
            OrderResult = []  # Será la lista de filas ordenadas de mayor coincidencia a menor (sin cero)
            ocurrencias = []  # Esta lista tendrá valores de ocurrencia únicos entre todas las filas de la base de datos
            for elemento in ProductsResult:
                if elemento[-1] not in ocurrencias:
                    ocurrencias.append(elemento[-1])
            mOccur = max(ocurrencias)

            while mOccur > 0:  # Este ciclo ordenará las filas de mayor ocurrencia a menor en OrderResult
                for elemento in ProductsResult:
                    if elemento[-1] == mOccur:
                        OrderResult.append(elemento[:-1])
                mOccur -= 1
            return OrderResult


if __name__ == '__main__':
    a = Ginerdata(host='216.231.129.35', user='idemself_ginercor', password='itg#2]/pln%8dk@n', database='idemself_test')
    print(a.buscarProductos('10101'))

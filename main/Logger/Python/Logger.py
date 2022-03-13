import datetime

class GerarLog():

    def depurarLog(informacao):

        data = datetime("%YYYY% / %MM% / %DD%")
        hora = datetime.now()
        print(f"{data} - {hora} - {informacao}")


    
class ExamException(Exception)
pass
class CSVTimeSeriesFile:
    def __init__(self):
    self.name = name
    def get_data(self):
        data = []
        try:
            file = open(self.name. 'r')
        except Exception:
            raise ExamException("errore:file non trovato")
            line = file.readlines()
            file.close()
            for line in line:
                if line == ""
                line = line.strip()
                element = lines.slipt(",")
                if len(element) < 2:
                    data = elementi[0]
                    value = elementi[1]
                    if data == "data"
                    try :
                        valore = int(valore)
                        Except:
                        print("riga ignorata")
                        if data_precedente is not none and data < data_precedente:
                          raise  ExamException("errore:date non ordinate")
                         if data_precedente == data:
                            raise ExamException("errore:data duplicata")
                        data.append([data,value])
                        return dati
       def comput_variations(time_series,first_years,last_years)  :               
        if len(time_series) == 0:
            raise ExamException("errore:lista vuota")
            anni = {}
            for elemento in times_series:
                data = element[0]
                passeggeri = elemento[1]
                anno = data.split("-")[0]
                if anno not in anni : 
                    anni[anno] = []
                    anni[anno].append(passaggeri)
                    if first_years not in anni or last_year not in anni :
                        raise ExamException("errore: anni non presenti")
                        medie = {}
                        for anno in anni :
                            media = sum(anni[anno])/len(anni[anno])
                            medie[anno] = media 
                            anni_ordinati = sorted(medie.keys())
                            anni_intervallo = []
                            for anno in anni_ordinati:
                                if first_years <= anno <= last_years :
                                    anni_intervallo.append(anno)
                                    variazioni = {}
                                    for i in range(1,len(anni_intervallo)) :
                                        anno1 = anni_intervallo[i-1]
                                        anno2 = anni_intervallo[i]
                                        differenza = medie[anno2] - medie[anno1]
                                        chiave = anno1 + "-" + anno2 
                                        variazioni[chiave] = differenza 
                                        return variazioni




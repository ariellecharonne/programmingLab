class ExamExceotion(Exception):
    pass

class MovingAverage:
   def _init_ (self,window_lenght):
    if type(window_lenght)!= int or window_lenght <= 0
    raise ExamException ("fenetre invalido")
    self.window_lenght = window_lenght
    def compute (self,data):
        if type (data) != list :
            raise ExamException (" non è una lista ")
            seft.data = data 
            for elemento in data :
                if type (elemento) != int and type (elemento) != float :
                    raise ExamException ("elementi non numerici")
                if len(data) < self.window_lenght :
                    raise ExamException("lista troppo corta ")
                    result []
                    for i in range (len(data-self.window_lenght + 1))
                    somma = 0
            for j in range ( i ,i + self.window_lenght)
                    somma = somma + data [j]
                    media = somma / self.window_lenght 
                    result.append(media)
                    return result
                    






      





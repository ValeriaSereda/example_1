class Zamowienie:
    def __init__(self, nr_zam, n_zam, data_zam, wart_zam,):
        self.numer_zamowienia = nr_zam
        self.nazwa_zamowienia = n_zam
        self.data_zamowienia = data_zam
        self.wartosc_zamowienia = wart_zam
        self.pozycja = []
    def __str__(self):
        return str(self.numer_zamowienia) + ',' + self.nazwa_zamowienia + ',' + str(self.data_zamowienia) + ',' +  str(self.wartosc_zamowienia)
    def add_pozycja(self, zamowienie_pozycja): # dodawanie nowej pozycji do zamówienia
        self.pozycja.append(zamowienie_pozycja) # dodawanie nowego wiersza do tablicy 
    def print_zamowienie_z_pozycjami(self):   # Wyświetlenie zamówienia ze wszystkimi pozycjami 
        print(self)                            
        i = 0                               
        while i < len(self.pozycja):     
            print(self.pozycja[i])        
            i = i + 1                       

    def suma_all(self):                    # Wyliczenie całkowitej sumy zamówienia 
        i = 0                               
        sum_zamowien_all = 0                   
        while i < len(self.pozycja):      
            sum_zamowien_all = sum_zamowien_all + self.pozycja[i].suma 
            i = i + 1                       
        return sum_zamowien_all                

    def suma_dostawca(self, dostawca):       # Wyliczenie sumy pozycji wybranego dostawcy 
        i = 0                               
        sum_zamowienie_dost = 0                   
        while i < len(self.pozycja):      
            if self.pozycja[i].dostawca == dostawca:  
               sum_zamowienie_dost = sum_zamowienie_dost + self.pozycja[i].suma 
            i = i + 1                       
        return sum_zamowienie_dost               

class Zamowienie_pozycja:   # Tworzenie klasy obiektów podporządkowanych głównej klasie 
    def __init__(self, dostawca, num_artykul, naz_artykul, suma): 
        self.dostawca = dostawca 
        self.numer_artykul = num_artykul   
        self.nazwa_artykul = naz_artykul 
        self.suma = suma      

    def __str__(self):                                           
        return self.dostawca + ' ' + str(self.numer_artykul) + ' ' + self.nazwa_artykul + ' ' + str(self.suma) 
    
zamowienie = Zamowienie(1, 'Test Order', '29.05.2023', 100)  
zamowienie.add_pozycja(Zamowienie_pozycja('Dostawca_1', 234, 'Zeszyt A4',  340))   
zamowienie.add_pozycja(Zamowienie_pozycja('Dostawca_1', 284, 'Zeszyt A3',  40))
zamowienie.add_pozycja(Zamowienie_pozycja('Dostawca_2', 264, 'Zeszyt A4',  10))
zamowienie.add_pozycja(Zamowienie_pozycja('Dostawca_2', 224, 'Zeszyt A3',  110))
zamowienie.print_zamowienie_z_pozycjami()
print('Suma wszystkich pozycji : ' + str(zamowienie.suma_all())) 
dostawca = 'Dostawca_1'
print('Suma wszystkich pozycji' + ' ' + dostawca + ' :  ' + str(zamowienie.suma_dostawca(dostawca))) 

class Student: # definiujemy klasę (coś abstrakcyjnego, posidającego pewne cechy, np. obraz studenta)
    def __init__(self, imie, nazwisko,numer_indeksu):
        self.imie_studenta = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu 
        self.indeks = [] #jest pusta 

    def __str__(self): #robimy ciąg znaków 
        return self.imie_studenta + ' ' +self.nazwisko + ' ' + str(self.numer_indeksu)# retern - zwracamy się do self i wyciągamy
    
    def dodaj_ocene(self, ocena):
        self.indeks.append(ocena)
    
    def oblicz_sred(self):
        if len(self.indeks) == 0:
            return 0
        else:
            return sum(self.indeks) / len(self.indeks)

student_valeria = Student("Valeria", "Sereda", 123234)
student_valeria.dodaj_ocene(5.0)
student_valeria.dodaj_ocene(4.5)
student_valeria.dodaj_ocene(3.0)
student_valeria.dodaj_ocene(2.0)

print(student_valeria.oblicz_sred()) # wskazaniej komórki wirtualnej w której się znajduje informacja o student_valeria
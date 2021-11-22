class Sensorik():
    def __init__(self, Activated=False,             Leistung_Dichte_Sender=0.00,
                 Leistung_Dichte_Empfaenger=0.00,   Leistung_Rueckgestreut=0.00,
                 Leistung_Empfaenger=0.00,          Durchmesser_Apertur=0.00,
                 Oefnnungswinkel_Beta=0.00,         Querschnitt_Rueckgestreut=0.00):
        self.Activated                   = Activated
        self.Leistung_Dichte_Sender      = Leistung_Dichte_Sender
        self.Leistung_Dichte_Empfaenger  = Leistung_Dichte_Empfaenger
        self.Leistung_Rueckgestreut      = Leistung_Rueckgestreut
        self.Leistung_Empfaenger         = Leistung_Empfaenger
        self.Durchmesser_Apertur         = Durchmesser_Apertur
        self.Oefnnungswinkel_Beta        = Oefnnungswinkel_Beta
        self.Querschnitt_Rueckgestreut   = Querschnitt_Rueckgestreut

    def setNoise(self):
        self.Activated = False
        print(self.Activated)





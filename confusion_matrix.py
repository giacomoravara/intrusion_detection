import numpy as np
import plot as pl
from sklearn.metrics import confusion_matrix
import decision_tree as ds
from sklearn.metrics import accuracy_score

# calcolo la confusion matrix sul training per il calcolo del PCC
z_pred1 = ds.dt.predict(ds.dr)
y_actu = ds.dc.result
y_pred = ds.dt.predict(ds.dl)
#y_pred = ds.re.inverse_transform(y_pred1)

def five_class_transformer(real) :

    transformed = []
    for n in range(0, len(real)):
        if (real[n] == 28 or real[n] == 15 or real[n] == 1
                or real[n] == 33 or real[n] == 20 or real[n] == 8
                or real[n] == 11 or real[n] == 0 or real[n] == 22
                or real[n] == 34):
            transformed.append("DOS")
        if (real[n] == 26 or real[n] == 7 or real[n] == 21 or real[n] == 16
                or real[n] == 12 or real[n] == 10 or real[n] == 25 or real[n] == np.nan):
            transformed.append("Probe")
        if (real[n] == 35 or real[n] == 4 or real[n] == 36 or real[
            n] == 6
                or real[n] == 3 or real[n] == 13 or real[n] == 19 or real[n] == 31
                or real[n] == 29 or real[n] == 39 or real[n] == 14
                or real[n] == 27 or real[n] == 38 or real[n] == 37 or real[n] == 30):
            transformed.append("R2L")
        if (real[n] == 2 or real[n] == 24 or real[n] == 9 or real[
            n] == 18
                or real[n] == 5 or real[n] == 40 or real[n] == 23
                or real[n] == 32):
            transformed.append("U2R")
        if (real[n] == 17):
            transformed.append("normal")
    return transformed


pred = five_class_transformer(y_pred)
actu = five_class_transformer(y_actu)

cnf_matrix = confusion_matrix(actu, pred)
cnf_matrix1 = confusion_matrix(ds.df.result, z_pred1)  # confusion matrix per il calcolo dell'accuratezza del training

ACC = accuracy_score(actu, pred)
print(ACC)
#print(ACC)
ACC1 = accuracy_score(ds.df.result, z_pred1)
print(ACC1)

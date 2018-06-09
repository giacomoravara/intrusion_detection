import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing

df = pd.read_csv("train.csv")
dc = pd.read_csv("corrected.csv")

# PREPROCESSING ON TRAININGDATA

le = preprocessing.LabelEncoder()
le.fit(df.protocol)
list(le.classes_)
df.protocol = le.transform(df.protocol)

pe = preprocessing.LabelEncoder()
pe.fit(df.service)
list(pe.classes_)
df.service = pe.transform(df.service)

fe = preprocessing.LabelEncoder()
fe.fit(df.flag)
list(fe.classes_)
df.flag = fe.transform(df.flag)

re = preprocessing.LabelEncoder()
re.fit(["normal.", "ipsweep.", "nmap.", "portsweep.", "satan.",
        "mscan.", "saint.", "back.", "land.", "neptune.", "pod.",
        "smurf.", "teardrop.", "mailbomb.", "apache2.", "processtable.",
        "udpstorm.", "buffer+AF8-overflow.", "localmodule.", "loadmodule.",
        "perl.", "rootkit.", "httptunnel.", "xterm.", "ps.", "worm.",
        "ftp+AF8-write.", "guess+AF8-passwd.", "imap.", "multihop.", "phf.",
        "spy.", "warezclient.", "warezmaster.", "snmpgetattack.", "snmpguess.",
        "xsnoop.", "named.", "sendmail.", "sqlattack.", "xlock."])
#print(list(re.classes_))
#print(re.transform(re.classes_))
dc.result=re.transform(dc.result)

df.result = re.transform(df.result)
features = list(df.columns[:41])
z = df[features]

dt = DecisionTreeClassifier()  # create object of DecisionTreeClassifier class
dt = dt.fit(df[features], df.result)  # fit(x,y) function is used to train the features

##PREPROCESSING ON TESTDATA

dl = dc.copy()
del dl["result"]
de = preprocessing.LabelEncoder()
de.fit(dl.protocol)
list(le.classes_)
dl.protocol = de.transform(dl.protocol)

ge = preprocessing.LabelEncoder()
ge.fit(dl.service)
list(ge.classes_)
dl.service = ge.transform(dl.service)

he = preprocessing.LabelEncoder()
he.fit(dl.flag)
list(he.classes_)
dl.flag = he.transform(dl.flag)

dr = df.copy()
del dr["result"]
de = preprocessing.LabelEncoder()
de.fit(dr.protocol)
list(le.classes_)
dr.protocol = de.transform(dr.protocol)

ge = preprocessing.LabelEncoder()
ge.fit(dr.service)
list(ge.classes_)
dr.service = ge.transform(dr.service)

he = preprocessing.LabelEncoder()
he.fit(dr.flag)
list(he.classes_)
dr.flag = he.transform(dr.flag)

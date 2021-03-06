# -*- coding: utf-8 -*-
"""ann_breastcancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K3D7SN-83P-N4EfWmnUJcGZUzWCo0B26
"""

pip install tensorflow

#installation des packages
import numpy as np
import tensorflow as tf
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#telecharger la base de donnees
df = datasets.load_breast_cancer()

#decouvrir la base de donnees
print(df.DESCR)

print(df.data)

#preparation des donnees
X=df.data
y=df.target

scaled = StandardScaler()
X_scaled=scaled.fit_transform(X)
X_scaled

#separation des donnees d'entrainement et de test
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=42)

#construction du reseau de neurones
#Creation du reseau de neurone
model = tf.keras.models.Sequential()

#ajouter la couche cachee
model.add(tf.keras.layers.Dense(units=15,activation='relu',kernel_initializer='uniform',input_dim=30))

#ajouter une couche de sortie
model.add(tf.keras.layers.Dense(units=1,activation='sigmoid',kernel_initializer='uniform'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['binary_accuracy'])

model.summary()

#entrainer le model
model.fit(X_train,y_train,batch_size=455,epochs=100)

#tester le model
loss_test,accurate_test = model.evaluate(X_test,y_test)
print(f"test loss {loss_test} et test accurate {accurate_test}")
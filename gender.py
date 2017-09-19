from sklearn import tree

clf = tree.DecisionTreeClassifier()
# X = [tinggi,berat,ukuran sepatu]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
# Y = [data yang Masuk]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
'female', 'male', 'male']

clf = clf.fit(X, Y)

nama = str(input("Masukan Nama Anda :"))
tinggi = int(input("Masukan Tinggi anda :"))
berat = int(input("Masukan Berat Badan Anda :"))
sepatu = int(input("Masukan Ukuran Sepatu anda :"))

prediciton = clf.predict([tinggi,berat,sepatu])
print(nama,"Anda adalah seorang : ",Y)

# Dosya Açma
file = open(file='new_file.txt', mode='w', encoding='utf-8')

file.write('Full Name: Burak Yılmaz\nOccupation: Dreamer\n')
file.close()

# Var olan dosyamın içerisine yeni bir kayıt eklemek için mode argümanına 'a' veriyoruz. yani dosyamı append amacı ile açıyorum
file = open(file='new_file.txt', mode='a', encoding='utf-8')
file.write('Programing Language: Python\n')
file.close()

# Var olan dosya içerisindeki bilgileri okuma
file = open(file='new_file.txt', mode='r', encoding='utf-8')
for sentence in file.readlines():
    print(sentence)
file.close()
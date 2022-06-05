# Program Mahasiswa
i=a=b=c=0
nama=[ ]
npm=[ ]
kls=[ ]
jur=[ ]
ang=[ ]
while True:
	print (‘Masukkan data ke – ‘,i+1)
	nama.append(input(‘Nama Anda : ‘))
    	npm.append(input(‘NPM Anda : ‘))
	if len(npm[i])!=8:
		print (‘NPM Salah’)        
		print
        		nama.pop(i)
        		npm.pop(i)
        		continue
	kls.append(input(‘Kelas Anda : ‘))
  
  # Selesai 3.2

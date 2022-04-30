#!/usr/bin/python3
import os,sys,time,marshal

os.system('clear')
try:
    print(f'[+] masukan nama file\n[+] contoh - /sdcard/source.py')
    file = input(f'[+] masukan file : ')
    namafile = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        a = open(file, 'r').read()
    except IOError:
        print(f'\n[+] maaf file tidak ada !')
        sys.exit()
    try:
        b = compile(a,'','exec')
        c = marshal.dumps(b)
    except TypeError:
        print(f'[+] file sudah di compile.') 
        sys.exit()

fileout = open(namafile + 'x.py', 'w');fileout.write('#[+] compile by - irpan sopian\n#[+] https://github.com/IrpanQwerty-05\nimport marshal\nexec(marshal.loads(' + repr(c) + '))');fileout.close();time.sleep(3) 
print(f'\n[+] berhasil compile ke py3\n[+] file compile : {namafile}x.py\n');input(f'[+] tekan enter untuk kembali ke menu\n[+] CLTR + Z untuk keluar dari halaman');os.system('python compile_py.py')

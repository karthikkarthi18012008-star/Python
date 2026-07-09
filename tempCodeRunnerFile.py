
try:
    file=open('example1.txt','r')
    content=file.read()
    a=b
    print(content)

except FileNotFoundError:
    print("The file does not exists")
except Exception as ex:
    print(ex)

finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file close')
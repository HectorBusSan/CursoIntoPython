def main():
    open("/path/to/mars.jpg")
if __name__ == '__main__':
    main()


# nos dice que no encutentra en nuestra ruta la direccipon que mencionamos en la función


# Traceback (most recent call last):
#   File "c:\Users\Hector\Documents\Inovación\1Mision\10\open.py", line 4, in <module>
#     main()
#   File "c:\Users\Hector\Documents\Inovación\1Mision\10\open.py", line 2, in main    
#     open("/path/to/mars.jpg")
# FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

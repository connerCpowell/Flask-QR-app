import qrcode
import sys
import string
import random
from PIL import Image

def id_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def qr_maker(data):
    #data = sys.argv[1]
    default_patient = 'B479D647-C5E4-1B13-E053-A814000A4FDE-'
    ident = id_generator()

    patient = str(default_patient + data)
    disk = str(data + '-' + ident)
    print("disc code:", disk)


    img1 = qrcode.make(patient)
    img2 = qrcode.make(disk)


    img1.save('/home/pukowski/tmp/qr/patient.png')
    img2.save('/home/pukowski/tmp/qr/disk.png')

    # img1.show()
    # img2.show()
    return img1, img2

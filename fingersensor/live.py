from pyfingerprint.pyfingerprint import PyFingerprint
from Finger import What_Finger

def finger_live():
    f = What_Finger()
    #f = PyFingerprint()
        
    try:
        i = input("1:Enroll\t2:Match\t 3:Delete\t4:Empty\t5:Exit\n")

        if (i == '1'):
            f.enroll()
            finger_live()
        elif (i == '2'):
            f.search()
            finger_live()
        elif (i == '3'):
            f.delete()
            finger_live()
        elif (i == '4'):
            f.reset()
            finger_live()
        else:
            finger_live()


        # print("Waiting for Finger")
        # while f.readImage() is False:
        #     pass
        # f.convertImage(0x01)
        # result = f.searchTemplate()
        # pos = result[0]
        # accu = result[1]
        # if pos == -1:
        #     print('NO MATCH')
        #     finger_live()
        # else:
        #     print('Finger ID:', pos)
        #     print('Accuracy Score:', accu)
        # f.loadTemplate(pos, 0x01)
        # finger_live()

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        finger_live()

finger_live()
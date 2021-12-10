from pyfingerprint.pyfingerprint import PyFingerprint

import time


class What_Finger:
    def __init__(self):
        try:
            self.f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if self.f.verifyPassword() == False:
                print('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))

    def enroll(self):
        print('Waiting for finger...')
        ## Wait that finger is read
        while ( self.f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        self.f.convertImage(0x01)

        ## Checks if finger is already enrolled
        result = self.f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger again...')

        ## Wait that finger is read again
        while ( self.f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        self.f.convertImage(0x02)

        ## Compares the charbuffers
        if ( self.f.compareCharacteristics() == 0 ):
            raise Exception('Fingers do not match')

        ## Creates a template
        self.f.createTemplate()

        ## Saves template at new position number
        positionNumber = self.f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

    def search(self):
        print('Waiting for finger...')

        ## Wait that finger is read
        while (self.f.readImage() == False):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        self.f.convertImage(0x01)

        ## Searchs template
        result = self.f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if (positionNumber == -1):
            print('No match found!')
        else:
            print('Found template at position :' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))

        self.f.loadTemplate(positionNumber, 0x01)

    def delete(self):
        try:
            positionNumber = input('Please enter the template position you want to delete: ')
            positionNumber = int(positionNumber)

            if (self.f.deleteTemplate(positionNumber) == True):
                print('Template deleted!')

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))

    def reset(self):
        try:
            if (self.f.clearDatabase() == True):
                print('RESET Successfull!!')

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))


## Biometric Attendance Management System with Raspberry Pi

Fingerprint Sensor, which we used to see in Sci-Fi movies a few years back, has now become very common to verify the identity of a person for various purposes. In the present time we can see fingerprint-based systems everywhere in our daily life like for attendance in offices,  employee verification in banks, for cash withdrawals or deposits in ATMs, for identity verification in government offices, etc.
Using this Raspberry Pi FingerPrint System, we can enroll new fingerprints in the system and delete the already-fed fingerprints.

### Required Hardware Components:
1. Raspberry Pi 3 Model B+
1. Raspberry Pi Fan, Case, Adapter, memory card(16GB)
1. Raspberry Pi 7 Inch LCD
1. USB to Serial converter
1. Fingerprint Module
1. Push buttons(10 pcs)
1. Resistor Pack
1. Capacitor Pack
1. Breadboard
1. Jumper wires
1. LED (optional)
1. PCB(optional) 
1. Required Software Components:
1. Python Scripting: python scripting language is `opencv`. Python scripting is used for fingerprint reader access, fingerprint authentication & recognition.
1. Putty: Putty is used to access data from rpi board.
1. MySQL: Database Creation and Management
1. Postgresql: Used for database creation and management.
 


## Circuit Diagram and Explanation:

In this Raspberry Pi Fingerprint sensor interfacing project, we  use  4 push buttons: one for enrolling the new fingerprint, one for deleting the already fed fingerprints, and two for increment/decrementing the position of already fed Fingerprints. An LED is used to indicate that the fingerprint sensor is ready to take a finger for matching. Here we have used a fingerprint module that works on UART. So here we have interfaced this fingerprint module with Raspberry Pi using a USB to Serial converter.

So, first of all, we need to make all the required connections as shown in the Circuit Diagram below. Connections are simple, we have just connected the fingerprint module to the Raspberry Pi USB port by using a USB to Serial converter. A 16x2 LCD is used for displaying all messages. A 10k pot is also used with LCD for controlling the contrast of the same. 16x2 LCD pins RS, EN, d4, d5, d6, and d7 are connected with GPIO Pin 18, 23, 24, 25, 8, and 7 of Raspberry Pi respectively. Four push buttons are connected to GPIO Pin 5, 6, 13, and 19 of Raspberry Pi. LED is also connected at pin 26 of RPI.


## Operation of Fingerprint Sensor with Raspberry Pi:
The operation of this project is simple, just run the Python code and there will be some intro messages over LCD and then the user will be asked to Place a Finger on the Fingerprint Sensor. Now by putting a finger over the fingerprint module, we can check whether our fingerprints are already stored or not. If your fingerprint is stored then LCD will show the message with the storing position of the fingerprint like ‘Fount at Pos:2’ otherwise it will show ‘No Match Found’.

Now to enroll in a fingerPrint, the user needs to press the enroll button and follow the instructions messages on the LCD screen.

If the user wants to delete any of the fingerprints then the user needs to press the delete button. After which, the LCD will ask for the position of the fingerprint which is to be deleted. Now by using another two push button for increment and decrement, the user can select the position of the saved Fingerprint and press the enroll button (at this time enroll button behave as Ok button) to delete that fingerprint. For more understanding have a look at the video given at the end of the project.

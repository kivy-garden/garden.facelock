import numpy as np
import cv2
import os
from kivy.uix.widget import Widget
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, StringProperty


class FaceLock(Widget):
    '''
    Face Lock: When combined with a widget, locks the further application,
    detects your trained cascade.
    The example.py file demonstrates the use.
    '''
    
    cascade = StringProperty()
    '''
    cascade: Name of the cascade to be passed which is present in present directory.
    '''

    index = NumericProperty(0)
    '''
    index: Camera index to be passed defaults to '0', i.e. your webcam,
    which camera to use can be changed by changing the index.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_match')
        super(FaceLock, self).__init__(**kwargs)
        self.face_recognize()

    def on_match(self):
        '''
        on_match: event dispatches when it finds the cascade in the camera.
        '''
        pass

    def face_recognize(self):
        cap = cv2.VideoCapture(self.index)
        
        face_cascade = cv2.CascadeClassifier(self.cascade)
        '''
        face_cascade: cascade is entered here for further use.
        '''

        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            '''
            Converts coloured video to black and white(Grayscale).
            '''
            if np.any(face_cascade.detectMultiScale(gray, 1.3, 5)):
                
                print ("Cascade found")
                
                self.dispatch('on_match')
                
                cv2.destroyAllWindows()
                for i in range(1, 5):
                    cv2.waitKey(1)
                break
            
            else:
                print ("Not recognized")

            cv2.imshow('frame', frame)
            #Comment the above statement not to show the camera screen
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print ("Forcefully Closed")

                cv2.destroyAllWindows()
                for i in range(1, 5):
                    cv2.waitKey(1)
                break
        cap.release()
Face Lock
=============

<!-- ![ScreenShot](https://raw.github.com/) -->

##Usage Summary


This widget can be used to make your application secure and it gets unlocked by detecting faces. You can use different face cascades for granting different access to different people by adding multiple cascade. 

Latest commit adds some new features.

##How It Works


Import in your python file or kivy file
```
from kivy.garden.facelock import FaceLock
```

###See example.py file for more.
I have added cascade for general frontal face so that anyone can unlock the example application.

##FaceLock Properties

- *index* - NumericProperty(0). Index of your camera that you'd use.
- *cascade* - StringProperty(). Name of the cascade file(.xml) that you want to be detected.
- *on_match* - Event dispatched when your cascade is detected.

##Want to contribute or need to see some improvements?
I would love that, please create an issue or send a PR.

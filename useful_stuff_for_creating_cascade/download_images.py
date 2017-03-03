import urllib
import urllib2
import requests
import cv2
import numpy as np
import os


def store_raw_images():
    '''To download images from image-net
        (Change the url for different needs of cascades)
    '''
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    neg_image_urls = urllib2.urlopen(neg_images_link).read().decode()

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:

            print i
            urllib.urlretrieve(i, "neg/" + str(pic_num) + '.jpg')
            img = cv2.imread("neg/" + str(pic_num) +'.jpg',
                                cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + '.jpg', resized_image)
            pic_num = pic_num + 1

        except:
            print "error"


def find_uglies():
    '''image-net gives a default image when it's real one is not available,
        this is to remove them
    '''
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv2.imread('uglies/' + str(ugly))
                    question = cv2.imread(current_image_path)

                    if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                        print "girl you ugly"
                        os.remove(current_image_path)
                except:
                    print "error"


def create_pos_n_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)


create_pos_n_neg()

# find_uglies()

# store_raw_images()
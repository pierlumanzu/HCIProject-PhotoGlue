from PIL import Image
import os

def deleteImageDirectory(dirPath):
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath + "/" + fileName)

def acquisitionImage(photosURLs):

    photos = []

    for photoURL in photosURLs:
        photos.append(Image.open(photoURL))

    informationPhotos = generateInformationPhotos(photos)

    return photos, informationPhotos

def generateInformationPhotos(photos):

    informationPhotos = []

    for photo in photos:

        informationPhotos.append([])

        width, height = photo.size

        informationPhotos[len(informationPhotos) - 1].append(width)
        informationPhotos[len(informationPhotos) - 1].append(height)

    return informationPhotos

def acquisitionBackground(backgroundPhotoURL):

    return Image.open(backgroundPhotoURL)

def interpolateGradient(f_co, t_co, interval):
    det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]

from PIL import Image, ImageDraw
from SetupMilpForPhotos import *
from MilpCplex import *
from OutputMilpForPhotos import *

def Milp(executionTime, n, photosURLs, weigths, backgroundPhotoURL=None, colors=None, W=None, H=None):

    deleteImageDirectory("OutputPhotos")

    photos, informationPhotos = acquisitionImage(photosURLs)

    if backgroundPhotoURL is not None:
        imageBackground = acquisitionBackground(backgroundPhotoURL)
        bestSolutions, W, H = milpCplex(executionTime, n, informationPhotos, weigths, imageBackground)
    else:
        if colors is not None and W is not None and H is not None:
            bestSolutions, W, H = milpCplex(executionTime, n, informationPhotos, weigths, None, W, H)

            if len(colors) == 1:
                imageBackground = Image.new('RGB', (W, H), color=colors[0])
            else:
                if len(colors) == 2:
                    imageBackground = Image.new('RGB', (W, H), color=0)
                    draw = ImageDraw.Draw(imageBackground)

                    f_co = colors[0]
                    t_co = colors[1]
                    for i, color in enumerate(interpolateGradient(f_co, t_co, W*2)):
                        draw.line([(i, 0), (0, i)], tuple(color), width=1)

    for i in range(len(bestSolutions)):
        saveImageSolution(n, bestSolutions, i, photos, informationPhotos, imageBackground)



from PIL import Image
import copy

def saveImageSolution(n, bestSolutions, index, photos, informationPhotos, imageBackground):
    try:
        imageBackground = copy.copy(imageBackground)

        for j in range(n):
            x = int(bestSolutions[index][1][3 * j])
            y = int(bestSolutions[index][1][3 * j + 1])
            s = bestSolutions[index][1][3 * j + 2]

            if int(s * informationPhotos[j][0]) > 0 and int(s * informationPhotos[j][1]) > 0:
                photo = photos[j].resize((int(s * informationPhotos[j][0]), int(s * informationPhotos[j][1])), Image.ANTIALIAS)
                imageBackground.paste(photo, (x, y))

        imageBackground.save("OutputPhotos/{}°CollageSolution.jpg".format(index + 1))

    except IOError:
        pass


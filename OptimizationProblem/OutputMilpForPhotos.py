from PIL import Image
import copy

"""def plotSolution(n, bestSolutions, index, informationPhotos, weigths, W, H):

    limsx = (0, W)
    limsy = (0, H)

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')

    for j in range(n):
        x = int(bestSolutions[index][1][3 * j])
        y = int(bestSolutions[index][1][3 * j + 1])
        s = bestSolutions[index][1][3 * j + 2]

        ax1.add_patch(patches.Rectangle((x, y),
                                        int(s * informationPhotos[j][0]),
                                        (s * informationPhotos[j][1]), fill=None, color='black'))
        ax1.annotate('{}_{}'.format(j, weigths[j]), (
            x + int(s * informationPhotos[j][0]) / 2,
            y + int(s * informationPhotos[j][1]) / 2),
                     color='black')

    plt.ylim(limsy)
    plt.xlim(limsx)
    plt.title("{}° area più grande: {}".format(index + 1, bestSolutions[index][0]))
    plt.show()"""

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


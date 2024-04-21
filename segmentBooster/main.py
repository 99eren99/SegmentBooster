import numpy as np
import cv2


def refineMask(imagePath,segmentationMask,mask_generator):
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    masks = mask_generator.generate(image)

    masks=sorted(masks, key=(lambda x: x['area']), reverse=True)

    refinedMask = np.zeros((masks[0]['segmentation'].shape[0], masks[0]['segmentation'].shape[1]))
    for ann in masks:
        m = ann['segmentation']

        unique, counts = np.unique(segmentationMask[m], return_counts=True)

        freqs=(np.asarray((unique, counts)).T)
        freqs=freqs[freqs[:, 1].argsort()]

        mostFrequentID=freqs[-1,0]

        """ if len(freqs)>1:
            if freqs[-1,0]==0 and freqs[-2,1]/freqs[:,1].sum()>0.2:
                mostFrequentID=freqs[-2,0]
            else:
                mostFrequentID=freqs[-1,0]
        else:
            mostFrequentID=freqs[-1,0] """

        refinedMask[m] = mostFrequentID

    return refinedMask

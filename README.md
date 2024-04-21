# SegmentBooster
Refine segmentation masks with Segment Anything Model(SAM)

# Example:
<img src="https://raw.githubusercontent.com/99eren99/SegmentBooster/main/example.JPG" width="700" height="700">

# For requirements:
```java
install SAM -> https://github.com/facebookresearch/segment-anything
numpy, cv2
```
# demo.py:
```python 
from segmentBooster import refineMask
samModelType="..."
samModelCheckpoint="..."
sam = sam_model_registry[SAMtype](checkpoint=SAMcheckpoint)
mask_generator = SamAutomaticMaskGenerator(sam)

from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
imagePath"..."
segmentationMask="..."#2D numpy array with shape(image.shape), storing pixel level class IDs.

#outputs 2D numpy array with shape(image.shape), storing pixel level class IDs.
refinedMask=refineMask(imagePath,segmentationMask,mask_generator)
```

# SegmentBooster
Refine segmentation masks with Segment Anything Model(SAM)

# Example:
<img src="https://raw.githubusercontent.com/99eren99/SegmentBooster/main/example.JPG" width="512" height="512">

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
imagePath"..."
segmentationMask="..."#2D numpy array with shape(image.shape), storing pixel level class IDs.

refinedMask=refineMask(imagePath,segmentationMask,SAMtype,SAMcheckpoint)#outputs 2D numpy array with shape(image.shape), storing pixel level class IDs.
```

# SegmentBooster
Refine segmentation masks with Segment Anything Model(SAM)

<br />
![img](https://raw.githubusercontent.com/99eren99/SegmentBooster/main/example.jpg)
<br /> For requirements:<br />
```java
install SAM -> https://github.com/facebookresearch/segment-anything
numpy, cv2
```
<br />
demo.py:<br />

```python 
from segmentBooster import refineMask
samModelType="..."
samModelCheckpoint="..."
imagePath"..."
segmentationMask="..."#2D numpy array with shape(image.shape), storing pixel level class IDs.

refinedMask=refineMask(imagePath,segmentationMask,SAMtype,SAMcheckpoint)#outputs 2D numpy array with shape(image.shape), storing pixel level class IDs.
```
<br />

![MindMouse](https://imgur.com/NQYZPv1)
# MindMouse
# Spartahack 8 [2023]
### Inspiration
Computer Vision is widely used as a tool for Object Detection, Identification, and Classification, but we wanted to think of more interactive uses, that could potentially help a part of the community that did not have sufficient resources to effectively access technology. Many apps allow voice recognition or motion tracking to operate a computer but not that many exist that are designed for people who are unable to use all of their limbs. We created MindMouse to solve that issue.

### What it does
Our project uses real time footage of your face to track its horizontal tilt and vertical motion, then translates that into data which can navigate your cursor across your computer device. It also allows users to click by closing their eyes shut till they hear a confirmation sound.

### How we built it
The Project was built using Python with the help of the OpenCV, PyAutoGUI, Numpy, Playsound and Math libraries. 
1.  It uses OpenCV to capture the users camera and actively locates and creates a bounding box around the users face. When the program is run, the first few seconds to boot are used to save the default location of the users face. This location is compared to the dynamic location of their faces to determine whether the mouse should more up or down. For the horizontal motion, our program calculates the difference in height between the right and left eye to determine the direction of the tilt and whether it should move left or right.
2. It then uses PyAutoGUI to actually move the cursor accordingly to match the desired orientation. In order to click, we decided to detect whether the eyes bounding box vanished (you shut your eyes) for a specified range of time. If this range of time was satisfied, a audio cue would be played to let the user know that they can now open their eyes.

### Challenges we ran into
We initially planned on moving the cursor with head location in correlation to the camera, but this required us to move our entire bodies, which defeated the purpose of the project. Instead we decided to base the cursor movement on the direction that the users face was looking but this once again was ineffective as either an eye was not detected when the user turned left or right, or the user wasn't able to look at the screen when navigating. Our final solution was just keeping the users head looking at the screen and moving in a way that doesnt interrupt the viewing experience. 

### Accomplishments that we're proud of
We're proud of using such a small amount of libraries to accomplish such a complex task as well as do the maths to get the appropriate angles and thresholds for cursor movement as well as the numerous ways we tried to tackle the issue with the intended purpose in mind.

### What we learned
We learned an impressive amount of the OpenCV library as well as Haar Cascading ( A ML approach to facial feature recognition). We also learnt alot about accessing the ui and moving elements of it such as the cursor and clicks.

### What's next for MindMouse
By possibly developing our own form of Cascading to have a tighter, more sensitive bounding box for the face and eyes to more accurately detect motion and presence. We could also integrate a virtual keyboard once the accuracy was much higher to allow fine input of characters as well. We also had planned mouse acceleration based on the extent of the head tilt or vertical displacement to allow for faster navigation across the screen rather than a static cursor speed.

### Authors
Tanay Reddy & Navya Singh

import cv2

class text_overlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = None
        self.counter = 0
    def update_frame(self, image):
        self.image = image
        self.counter = 0
    def overlay_text(self,text, xpos):
        width = int(self.width*xpos)
        height = int(self.height*(self.counter + 1)*0.1)
        cv2.putText(self.image, text, org=(width, height), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.0, color=(255, 0, 0), thickness=2)
        self.counter += 1

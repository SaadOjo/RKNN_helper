# DTSIS: Boilerplate code for computer vision applications
# Authored by: Syed Saad Saif

# Import the libraries

from dtsis_metrics import fps, average, stopwatch
from dtsis_capture import VideoCaptureThreading
from dtsis_text_overlay import text_overlay
from timeit import default_timer as timer

import cv2
import numpy as np

#Used for busy waiting
import time

cap = VideoCaptureThreading(0, 1280, 720)
to = text_overlay(1280,720)
sw = stopwatch()
cap.start()


# Create a dictionary that will store the averager objects
time_averagers = {}
time_averagers['preprocessing_time']   = average(100)
time_averagers['inference_time']       = average(100)
time_averagers['post_processing_time'] = average(100)
time_averagers['draw_time']            = average(100)

# Create a dictionary that will store the process times
times = {}
times['preprocessing_time']   = None
times['inference_time']       = None
times['post_processing_time'] = None
times['draw_time']            = None

fps_counter = fps()

while True:

    ret, frame = cap.read()
    
    if ret == True:
        fps_counter.update()

        sw.start()
        # Simulate inference
        time.sleep(np.random.rand() * 0.05)
        time_averagers['inference_time'].update(sw.stop())
        times['inference_time'] = time_averagers['inference_time'].average()

        print('\n\n\n\n\n')
        for x in times:
            if(times[x] != None):
                print( '{}: {:.2f} ms'.format(x, times[x]*1000) ) 

        print('The frame rate is: ' + str(fps_counter.get_fps()) )

        # Overlay text to our frame
        to.update_frame(frame)
        to.overlay_text('FPS: {:.2f}'.format(fps_counter.get_fps()), 0.45 )
        
        
        cv2.imshow('Face Detection', frame)
        c = cv2.waitKey(5) & 0xFF
        if c ==27:
            cap.stop()
            cv2.destroyAllWindows()
            break
                        


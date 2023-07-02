import cv2
img = cv2.imread('solar-system.jpg')

cv2.putText(img, 
            "Sun",
            (20,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Mercury",
            (120,190),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Venus",
            (190,170),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Earth",
            (280,170),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Mars",
            (390,170),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Jupiter",
            (450,70),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Saturn",
            (700,100),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Uranus",
            (1000,120),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Neptune",
            (1150,130),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.3,
            color=(255,255,255)
            )
cv2.imshow("output",img)
cv2.waitKey(0)
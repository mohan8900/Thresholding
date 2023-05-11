#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2
img = cv2.imread('city.jpeg')
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[17]:


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[23]:


ret,thresh_img1 = cv2.threshold(img, 120,255,cv2.THRESH_BINARY)
ret,thresh_img2=cv2.threshold(gray,86,255,cv2.THRESH_BINARY_INV)

ret,thresh_img3=cv2.threshold(gray,86,255,cv2.THRESH_TOZERO)

ret,thresh_img4=cv2.threshold(gray,86,255,cv2.THRESH_TOZERO_INV)

ret,thresh_img5=cv2.threshold(gray,100,255,cv2.THRESH_TRUNC)


# In[24]:


cv2.imshow("threshold image",thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[25]:


# Use Adaptive thresholding to segment the image

thresh_img6=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

thresh_img7=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


# In[26]:


# Use Otsu's method to segment the image 
ret,thresh_img8=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# In[27]:


# Display the results

image = [thresh_img1,thresh_img2,thresh_img3,thresh_img4,thresh_img5,thresh_img6,thresh_img7,thresh_img8]
for i in range(0,8):
    cv2.imshow('threshold_image',image[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows


# In[7]:


##cv2.imshow("original",img)
#cv2.waitKey(0)
#v2.destroyAllWindows(


# In[8]:


cv2.imshow("adaptive mean thresholding",th1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


cv2.imshow("adaptive gaussian thresholding",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:


ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("otsu",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





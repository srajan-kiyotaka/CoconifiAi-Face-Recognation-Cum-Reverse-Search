<h1>About the project</h1>
<!-- <br></br> -->
<p>This is a facial recognition model. This model detects faces and extract features from that detected faces and use that features to recognise them in data set</p>
<h2><u>Salient feature of this model:</u></h2>
<ul>
    <li><strong>This model can work on small datasets:-</strong>In general CNN model about 50-100 images are required to recognise a face whereas this model requires only 1-2 image in dataset to recognise a face. This saves lot of space on system.</li>
    <li><strong>This model can gather information of unknown faces:-</strong>The object is captured automatically by cam. Image get converted into a link and this link is used for reverse image search on web browser, a technique used in web scraping for gathering information. We can get information/metadata in form of JSON. </li>
    <li><strong>This model can work on multiple faces:-</strong>Facial detection in this model can generate n no. of faces which can be recognised by <a href="https://towardsdatascience.com/hashes-power-probabilistic-data-structures-d1398d1335c6" >probalistic hashing</a> </li>
    <li><strong>This model can work on any lightning condition:-</strong>For this feature we used haar's cascade model. First it convert an RGB image into a low light binary image and constructs arrow from one bright spot to another bright spot which makes it independent of lightning condition.</li>
</ul>

<h2>Tech Stacks used:</h2>
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Google Cloud](https://img.shields.io/badge/Google%20Cloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white) ![Fortran](https://img.shields.io/badge/Fortran-%23734F96.svg?style=for-the-badge&logo=fortran&logoColor=white)
<h3>Demo video (when there is low lightning conditions)</h3>
![](https://github.com/shivamsinoliyainfinity/CoconifiAi-Face-Recognation-Cum-Reverse-Search/blob/84e1a9653de244973ed2ddeae5f37567ca943f36/demo/low_light.mov)

<h3>Demo video (when there is mid lightning conditions)</h3>
![](https://github.com/shivamsinoliyainfinity/CoconifiAi-Face-Recognation-Cum-Reverse-Search/blob/84e1a9653de244973ed2ddeae5f37567ca943f36/demo/mid_light.mp4)

<h3>Demo video (for multiple face detection)</h3>
![](https://github.com/shivamsinoliyainfinity/CoconifiAi-Face-Recognation-Cum-Reverse-Search/blob/84e1a9653de244973ed2ddeae5f37567ca943f36/demo/multiple_detection.mov)


<h3>Demo video (for unknown faces)</h3>
![](https://github.com/shivamsinoliyainfinity/CoconifiAi-Face-Recognation-Cum-Reverse-Search/blob/84e1a9653de244973ed2ddeae5f37567ca943f36/demo/unknown_meta_data.mp4)

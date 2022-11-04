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

<br>

## Demo video when there is low lightning conditions.

https://user-images.githubusercontent.com/91196806/200052963-0f23b1d2-3382-4681-ac9d-5ce45911ec25.mov

<br>

## Demo video when there is mid lightning conditions.

https://user-images.githubusercontent.com/91196806/200052953-2cff1a34-e8b2-4666-8036-058d8f056913.mp4

<br>

## Demo video for multiple face detection.

https://user-images.githubusercontent.com/91196806/200052941-be078ed4-c1ee-46e8-81fe-bf2eb00ec94b.mov

<br>

## Demo video for unknown faces.

https://user-images.githubusercontent.com/91196806/200052912-1e66a2b1-85f7-4173-a27f-b585365872f6.mp4

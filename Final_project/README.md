# 'B-BLY'(Fin# 'B-BLY'(Final project) - recommendation service system

<h2> 1. Data_set</h2>
	1) Crawling pic of men's wearing on instagram <br>
  <img width="724" alt="crawling_insta" src="https://user-images.githubusercontent.com/75061809/166146661-7a67707a-ba6e-4596-8ef8-6acd2e1226f5.png">
	2) Crawling information( pic, price, img_url., etc..) on MUSINSA.<br>
  <img width="704" alt="crawling_musinsa" src="https://user-images.githubusercontent.com/75061809/166146760-83110e65-c636-4d91-a7f2-66d1f4889f4e.png">
	3) Data preprocessing for cropping pic ( then, using object detection, detectron2 , cv2).<br>
	4) By cropping , numbering and Indexing of the top and bottom are performed respectively. <br>
	5) Saving information(crawling on 2)) on csv. <Br>
	6) Process searching as below pic.
	<img width="705" alt="process" src="https://user-images.githubusercontent.com/75061809/166146712-df801617-07bf-4456-9a9d-2d21bfdeb3ba.png">

<h2> 2. Execution_file</h2>
	1) with annoy file, json file and model, execute file. <br>
	2) Put the pic -> using RESNET 18 , check predictive value .<br>
	3) Finding similar value and  output image and information. <br>
  <img width="1227" alt="smilar_picture" src="https://user-images.githubusercontent.com/75061809/166146687-90538981-07ee-483d-8351-41a64791d5d5.png">
	4) Connecting MUSINSA page.<br>
	5) If want matching clothes( for example, if suggest top and want to find well-matched bottom), first, finding similar clothes(top) and finding matching clothes(bottom).al project) - recommendation service system. <br>
<img width="1247" alt="matching_pic" src="https://user-images.githubusercontent.com/75061809/166146784-62832723-21d9-43e3-a3c9-4dfae542e7a6.png">
  6) Have used server by AWS and PUTTY by uploading files. (AWS : ubuntu , using tensorflow) <br>
  7) Processing reference. <br>
<img width="1083" alt="processing" src="https://user-images.githubusercontent.com/75061809/166146740-1191bdfd-b1b8-4169-afc0-d1fb11160c15.png">

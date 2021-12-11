"""
Víctor Ferrer
SCAV - SP3

"""

-------------------------------------------------------

Github link: https://github.com/DrumsSound/SP3 


-------------------------------------------------------
Guide:


Once you run the program you can choose between these different actions: 

	1. Convert BBB codec
        2. Video Comparison
        3. BBB stream default IP (192.168.1.30)
        4. BBB stream select desired IP
        exit. To end the program

 Now you can navigate throught the program.
 

 1. First option allows you to convert the BBB video codec into one of the below:
	
	0. VP8
	1. VP9
	2. .h265
	3. AV1

	* the videos that appear in the folder "outputs" where done with the 1m_BBB.mp4 that is shorter.
	** the convertion to AV1 is quite slow because it's already in developement for ffmpeg (the output of AV1 is not shared).
 

 2. Second option allows you to compare to of the codec of the first chapter. We have choosen VP8 and VP9,
	to show the real and perceptible differences.

	(* It is required to have executed firstly the VP8 and VP9 codec in chapter 1. To have the videos generated.)

	Both appear at the same time.
		- VP8 left
		- VP9 right

	CONCLUSION: We've been able to see how VP9 has quite more resolution and quality than VP8.
                    Were it is more evident the difference is in the grass of the video, of the hair of the rabbit or
                    other animals, as is where more resolution is required. Also textures in generals of the video lose
                    essence in VP8 with respect to VP9.
    
      
 3. Third option allows you to stream the BBB video to a default IP adress (192.168.1.30) and default port 8080.
	
	- Whent the program asks press enter and it will start streaming. 
         

 4. Fourth option allows you to stream the BBB video, but let's you choose the IP adress in a certain range.
	
	RANGE: 192.168.0.0 and 192.168.255.255
	
	- When asked by the program introduce you IP desired.
		Ex. 192.168.X.Y
			- Enter X: 15
			- Enter Y: 112
		    IP adress: 192.168.15.112		


 exit. Finally if you want a close the program just type the word exit.


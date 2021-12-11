"""
Víctor Ferrer
SCAV - SP3

"""

import os


# First function translates 3 values in RGB into the 3 YUV values

class FFMPEG:

    @staticmethod
    def codec_converter(option_):
        """ Exercise 1. Convert BBB video to VP8, VP9, h265 and AV1.
            We let the user choose between the different formats and then we do so.
        """
        # VP8
        if option_ == 0:
            cmd = str(
                "ffmpeg -i BBB.mp4 -c:v libvpx -c:a libvorbis BBB_vp8.webm")
            os.system(cmd)

        # VP9
        elif option_ == 1:
            cmd = str("ffmpeg -i BBB.mp4 -c:v libvpx-vp9 -c:a libopus BBB_vp9.webm")
            os.system(cmd)

        # .h265
        elif option_ == 2:
            cmd = str("ffmpeg -i BBB.mp4 -c:v libx265 -c:a copy BBB_h265.mov ")
            os.system(cmd)

        # .AV1
        elif option_ == 3:
            cmd = str("ffmpeg -i BBB.mp4 -c:v libaom-av1 -strict -2 BBB_av1.mp4")
            os.system(cmd)

    @staticmethod
    def video_comparison():
        """
            Exercise 2. In this exercise we stack two videos of the ones generated in the exercise before
            and we stack them to be able to compare them.
            Codecs compared: VP8 and VP9

            CONCLUSION: We've been able to see how VP9 has quite more resolution and quality than VP8.
                    Were it is more evident the difference is in the grass of the video, of the hair of the rabbit or
                    other animals, as is where more resolution is required. Also textures in generals of the video lose
                    essence in VP8 with respect to VP9.
        """
        print("\n The codecs compared will be VP8 and VP9. \n\n")
        cmd = str('ffmpeg -i BBB_vp8.webm -i BBB_vp9.webm -filter_complex hstack comparison.mp4')

        os.system(cmd)

    @staticmethod
    def video_streaming():
        """
        Exercise 3. We Take the BBB.mp4 video and streamed into the IP address 192.168.1.30 and port 8080.
        """

        cmd = str('ffmpeg -i BBB.mp4 -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f mpegts '
                  'udp://192.168.1.30:8080')
        os.system(cmd)

    @staticmethod
    def video_streaming_selectIP():
        """
        Exercise 4. We Take the BBB.mp4 video and streamed into the IP address that the user selects.
        """
        x = int(input("\n You can choose to which IP you want to stream the BBB video."
                      "\n The allow rang goes from 192.168.0.0 to 192.168.255.255 (default port 8080)"
                      "\n So choose you preference: \n\n 192.168.X.Y \n    Enter X: "))
        y = int(input("    Enter Y: "))

        if x in range(0, 255) and y in range(0, 255):
            ip = str(str(x) + "." + str(y))
            cmd = str('ffmpeg -i BBB.mp4 -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f mpegts '
                      'udp://192.168.' + ip + ':8080')
            os.system(cmd)
        else:
            print("\n IP selected out of range.\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    option = int(input("\n Choose your action:\n\n  "
                       "1. Convert BBB codec.\n  "
                       "2. Video Comparison.\n  "
                       "3. BBB stream default IP (192.168.1.30)\n  "
                       "4. BBB stream select desired IP. \n  "
                       "exit. To end the program\n\n Your action: "))
    while option != 'exit':

        if option == 1:
            x_ = int(
                input('\n Enter from 0 to 3 te corresponding codec that you want to convert the BBB video \n  0. VP8'
                      '\n  1. VP9\n  2. .h265 \n  3. AV1 \n\n  Your option: '))
            if 0 <= x_ <= 3:
                FFMPEG.codec_converter(x_)
            else:
                print("\n You have introduced a wrong option.\n\n")

        elif option == 2:
            input("\n Make sure you have executed first chapter, as videos generated there are required. "
                  "\n Press Enter to continue. ")
            FFMPEG.video_comparison()

        elif option == 3:
            input(
                "\n The BBB will be streamed by default to IP 192.168.1.30 and port 8080. \n Press Enter to continue. ")
            FFMPEG.video_streaming()

        elif option == 4:
            FFMPEG.video_streaming_selectIP()

        else:
            print("\n The option introduced is not valid. Try again.\n\n")

        option = int(input(" Choose your action:\n\n  "
                           "1. Convert BBB codec.\n  "
                           "2. Video Comparison.\n  "
                           "3. BBB stream default IP (192.168.1.30)\n  "
                           "4. BBB stream select desired IP. \n  "
                           "exit. To end the program\n\n Your action: "))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

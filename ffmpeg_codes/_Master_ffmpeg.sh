#!/bin/bash

# ffmpeg - mp4 DIVISION for SELECTED PARTS 
##########################################
ffmpeg -i ORIGINALFILE.mp4 -acodec copy -vcodec copy -ss 0 -t 00:15:00 OUTFILE-1.mp4
ffmpeg -i ORIGINALFILE.mp4 -acodec copy -vcodec copy -ss 00:15:00 -t 00:15:00 OUTFILE-2.mp4
ffmpeg -i ORIGINALFILE.mp4 -acodec copy -vcodec copy -ss 00:30:00 -t 00:15:00 OUTFILE-3.mp4
##########################################
ffmpeg -i camera_back_left_down_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:00:00 -t 00:10:00 camera_back_left_down_120fov_01.mp4
ffmpeg -i camera_back_left_down_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:10:00 -t 00:20:00 camera_back_left_down_120fov_02.mp4
ffmpeg -i camera_back_left_down_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:20:00 -t 00:30:00 camera_back_left_down_120fov_03.mp4
ffmpeg -i camera_back_left_down_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:30:00 -t 00:40:00 camera_back_left_down_120fov_04.mp4
ffmpeg -i camera_back_left_down_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:40:00 -t 00:45:00 camera_back_left_down_120fov_05.mp4

ffmpeg -i camera_front_center_120fov.mp4 -acodec copy -vcodec copy -ss 00:00:00 -t 00:10:00 camera_front_center_120fov_01.mp4
ffmpeg -i camera_front_center_120fov.mp4 -acodec copy -vcodec copy -ss 00:10:00 -t 00:20:00 camera_front_center_120fov_02.mp4
ffmpeg -i camera_front_center_120fov.mp4 -acodec copy -vcodec copy -ss 00:20:00 -t 00:30:00 camera_front_center_120fov_03.mp4
ffmpeg -i camera_front_center_120fov.mp4 -acodec copy -vcodec copy -ss 00:30:00 -t 00:40:00 camera_front_center_120fov_04.mp4
ffmpeg -i camera_front_center_120fov.mp4 -acodec copy -vcodec copy -ss 00:40:00 -t 00:45:00 camera_front_center_120fov_05.mp4
##########################################


## DIVIDING MP4 DATA
####################
cd ~/records/wave2
mkdir cam_fc_120
ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:00:00 -t 00:10:00 ./cam_fc_120/01_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:10:00 -t 00:20:00 ./cam_fc_120/02_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:20:00 -t 00:30:00  ./cam_fc_120/03_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:30:00 -t 00:40:00  ./cam_fc_120/04_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:40:00 -t 00:50:00  ./cam_fc_120/05_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:50:00 -t 01:00:00  ./cam_fc_120/06_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:00:00 -t 01:10:00  ./cam_fc_120/07_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:10:00 -t 01:20:00  ./cam_fc_120/08_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:20:00 -t 01:30:00  ./cam_fc_120/09_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:30:00 -t 01:40:00  ./cam_fc_120/10_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:40:00 -t 01:50:00  ./cam_fc_120/11_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:50:00 -t 02:00:00  ./cam_fc_120/12_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:00:00 -t 02:10:00  ./cam_fc_120/13_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:10:00 -t 02:20:00  ./cam_fc_120/14_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:20:00 -t 02:30:00  ./cam_fc_120/15_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:30:00 -t 02:40:00  ./cam_fc_120/16_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:40:00 -t 02:46:38  ./cam_fc_120/17_10min.mp4


### FOR EXACT SPLITTING ###
###########################
ffmpeg -i input.mp4 -ss 01:00:00 -to 01:10:00 -c:v copy -c:a copy output.mp4
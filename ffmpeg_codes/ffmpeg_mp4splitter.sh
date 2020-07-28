#! /bin/bash
mkdir cam_fc_120

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:00:00 -t 00:10:00 ./cam_fc_120/01_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:10:00 -t 00:20:00 ./cam_fc_120/02_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:20:00 -t 00:30:00 ./cam_fc_120/03_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:30:00 -t 00:40:00 ./cam_fc_120/04_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:40:00 -t 00:50:00 ./cam_fc_120/05_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 00:50:00 -t 01:00:00 ./cam_fc_120/06_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:00:00 -t 01:10:00 ./cam_fc_120/07_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:10:00 -t 01:20:00 ./cam_fc_120/08_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:20:00 -t 01:30:00 ./cam_fc_120/09_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:30:00 -t 01:40:00 ./cam_fc_120/10_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:40:00 -t 01:50:00 ./cam_fc_120/11_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 01:50:00 -t 02:00:00 ./cam_fc_120/12_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:00:00 -t 02:10:00 ./cam_fc_120/13_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:10:00 -t 02:20:00 ./cam_fc_120/14_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:20:00 -t 02:30:00 ./cam_fc_120/15_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:30:00 -t 02:40:00 ./cam_fc_120/16_10min.mp4

ffmpeg -i camera_front_center_120fov.lraw.mp4 -acodec copy -vcodec copy -ss 02:40:00 -t 02:46:38 ./cam_fc_120/17_10min.mp4


ffmpeg -i camera_front_center_120fov.lraw.mp4 -ss 3600 -t 4200 -c:v copy -s 1928x1208 output1.mp4
#!/bin/bash
if [ ! -d "data/ego/video_imgs"  ];then
	mkdir "data/ego/video_imgs"
fi
for file in `ls data/ego/videos/*`
do
	name=$(basename $file .mp4)
	echo "$name"
	PTHH=data/ego/video_imgs/$name
	if [ ! -d "$PTHH"  ];then
		mkdir "$PTHH"
	fi
	ffmpeg -i "$file" -f image2 -vf fps=30 -qscale:v 2 "$PTHH/img_%05d.jpg"
done

if [ ! -d "data/ego/wave"  ];then
	mkdir "data/ego/wave"
fi
for f in `ls data/ego/videos/`
do
    echo ${f%.*}
    ffmpeg -y -i data/ego/videos/${f} -qscale:a 0 -ac 1 -vn -threads 6 -ar 16000 data/ego/wave/${f%.*}.wav -loglevel panic
done


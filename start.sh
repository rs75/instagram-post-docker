docker build . -t postinstagram
docker run -it -v `pwd`/data:/data postinstagram

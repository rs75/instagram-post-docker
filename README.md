# instagram-post-docker

Simple docker container, that creates an instagram post.

1. Clone repository
2. Update config file in `data/config.json`
3. Build the image: `docker build . -t postinstagram`
4. Create container and mount `data`directory (contains config file and image): ```docker run -it -v `pwd`/data:/data postinstagram```

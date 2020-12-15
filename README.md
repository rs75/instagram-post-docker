# instagram-post-docker

Simple docker container, that creates an instagram post.

1. Update config file in `data/config.json`
2. build the image: `docker build . -t postinstagram`
3. create container and mount `data`directory: `docker run -it -v \`pwd\`/data:/data postinstagram`

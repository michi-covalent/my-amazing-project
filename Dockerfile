FROM ubuntu
COPY my-innocent-program /usr/bin/my-innocent-program
ENTRYPOINT ["/usr/bin/my-innocent-program"]
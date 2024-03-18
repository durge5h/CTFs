# sudo docker build -t vuln
# sudo docker run -d -p 1337:1337 --rm -it vuln
FROM ubuntu:20.04
COPY Deployment .
RUN chmod +x ./ynetd && chmod +x ./chall
EXPOSE 1337
CMD ./ynetd -p 1337 ./chall

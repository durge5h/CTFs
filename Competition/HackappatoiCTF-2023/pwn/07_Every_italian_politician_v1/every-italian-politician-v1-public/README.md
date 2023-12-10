# Build

`docker build -t myasnik/every-italian-politician:v1-dbg .`

# Run

`docker run -it -p 8080:80 myasnik/every-italian-politician:v1-dbg`

Inside the container:
    - `./run_dbg.sh` will start qemu and spawn gdb attached
    - `./run_prod.sh` will start the chall in production environment

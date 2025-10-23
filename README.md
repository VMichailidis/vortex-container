# Vortex Container
---
A repo for reproducible vortex development and a collection of useful scripts to analyze runtime performance.

## Requirements:
- docker: in order to run the container
- sshfs: mount the vortex source code stored inside the container onto the host.
- uv: python and project manager to run the scripts
- just: the project's command runner

## Setup instructions
### 1. Build container

In order to build the docker file that will contain the vortex source code and the correctly configured installations of simx and verilator, simx run
```
  echo "VORTEX_REPO=https://github.com/vortexgpgpu/vortex" > .env
  just build
```

By default, the above command configures the container to use the original vortex repository. However, it is recommended that you fork vortex the vortex repository and replace the [vortexgpgpu/vortex] url with the url of your personal repo.

### 2. Mount and run the container

The following commands will start the container, mount the vortex repo to a local directory and start an interactive shell inside the container respectively

```
  just start
```
```
  just enter
```
```
  just mount
```

#### 2.a Mounting the container
In order to mount the vortex directory, the user needs to enter the root password of the container which is `vlsilab` by default.
The vortex directory of the container is mounted on the vortex directory, entering that directory allows editing the vortex source code with local tools (file manager, text editor, etc.)

#### 2.b Entering the container
After entering the container run the following command to verify correct installation:
```
  make -s
  ./ci/blackbox.sh --cores=2 --app=vecadd
```
The last command should return `PASSED!` as the second to last line

## Executing the scripts
Run
```
  chmod +x scripts/*
```
and then you can execute the scripts inside, provided you have uv installed
```
  ./scripts/script-name
```

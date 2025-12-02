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
  just build
```

By default, the above command configures the container to use the original vortex repository. However, it is recommended that you fork vortex the vortex repository and replace the [github.com/vortexgpgpu/vortex] url with the url of your personal repo.
In order to point the container to your personal vortex gpu fork, simply run
```
  just vortex-repo=https://github.com/<your-github-usernam>/vortex.git build
```


### 2. Mount and run the container

The following commands will start the container, mount the vortex repo to a local directory and start an interactive shell inside the container respectively.
Make sure that the directory `./container` exists inside the folder where you cloned this repo.

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
All the files contained inside the container can be found at the `container/` directory, by entering that directory you can edit the vortex source code with local tools (file manager, text editor, etc.)

#### 2.b Entering the container
After entering the container run the following command to verify correct installation:
```
  make -s
  ../configure
  ./ci/blackbox.sh --cores=2 --app=vecadd
```
The first two commands should be executed every time you enter the container.
The last command should return `PASSED!` as the second to last line.

## Executing the scripts
Run
```
  chmod +x scripts/*
```
and then you can execute the scripts inside, provided you have uv installed
```
  ./scripts/script-name
```

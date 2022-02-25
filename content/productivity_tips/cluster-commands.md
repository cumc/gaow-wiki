# Commonly used commands on HPC cluster

## SGE

List all nodes and memory

```
qhost
```

Show current running jobs

```
qstat
```

Show current jobs for a user `<uni>`

```
qstat -u <uni>
```

Submit a dummy job of "sleeping for 40 seconds" (`/bin/sleep 40`) to a particular node requesting 10GB memory:

```
qsub -l h="node33" -l h_vmem=10G -b y /bin/sleep 40
```

See [here](http://bioinformatics.mdc-berlin.de/intro2UnixandSGE/sun_grid_engine_for_beginners/how_to_submit_a_job_using_qsub.html)
for a list of options and explanations.

## slurm

### Status of a previous job

eg, how much memory it was using:

```
$ sacct -j 15215620 --format=jobid,jobname,partition,account,alloccpus,state,maxvmsize

         JobID    JobName  Partition    Account  AllocCPUS      State  MaxVMSize
  ------------ ---------- ---------- ---------- ---------- ---------- ----------
  15215620          RCDAS     sandyb pi-msteph+         16  COMPLETED
  15215620.ba+      batch            pi-msteph+         16  COMPLETED  83752696K
```

### Find and rerun multiple jobs

```bash
qstat | grep "Q batch" | cut -f 1 -d " " | xargs sudo qrun
```

## Contact
Gao Wang
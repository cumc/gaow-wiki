# R tips

## "commandArgs" example

Save a script `cmd.R` with contents below:

```r
eval(parse(text=commandArgs(T)))
print(c(x,y,z))
```

then run `Rscript cmd.R x=1 y=2 z=3` to see the outcome.
# Veronica E. Figueroa, 2022

setwd("C:/Users/lalaf/OneDrive/Documents/Drosophila/OmegaValues")


# make sure the only files in above wd are the 3 omega tables!!
#add external loop and add counter to output to run multiple times
files = list.files()


for (x in files) {
  values = read.table(x)
  name = paste("boot", x, sep = "_")
  boot_values= slice_sample(values, n= 257, replace = "TRUE")
  write.table(boot_values, name, sep = "    ", quote = FALSE, row.names = FALSE, col.names = FALSE)
}
  
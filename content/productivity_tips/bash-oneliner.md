# Useful One-liners Computer Commands

## Basics

### List hidden folders


```bash
ls -la | awk '{print $9}' | grep "^\." | grep -v "\.$" | grep -v "^.vtools"
```

### Terminal colored text


```bash
echo -e "\e[1;34mThis is bold blue text.\e[0m"
echo -e "\e[4;31mThis is underlined red text.\e[0m"
```

## Search related

### Find large files


```bash
sudo find /itch -size +20G -exec du -h {} \; > LargeFiles.txt
```

### Find and remove folders


```bash
find . -type d -name ".svn" -exec rm -r {} \;
find . -name .svn -print0 | xargs -0 rm -r
```

### Find and replace pattern from all files

```bash
perl -pi.bak -e 's/sample_variant_/genotype_/g' *.py
perl -pi.bak -e 's/@@@\\\(/{\$\\\(/g' *.notes
perl -pi.bak -e 's/\\\)@@@/\\\)\$}/g' *.notes
perl -pi.bak -e 's/\\\]@@@/\\\]\$}/g' *.notes
perl -pi.bak -e 's/@@@\\\[/{\$\\\[/g' *.notes
```
### Figure out and add file extension

```bash
find . -type f -not -name "*.*" -print0 | xargs -0 file | grep  'JPEG image data' | sed 's/:.*//' | xargs -I % echo mv % %.jpg > rename.sh
```

## Administration

### Change folder to 755, file to 644


```bash
find . -type f -print0 | xargs -I {} -0 chmod 0644 {}
find . -type d -print0 | xargs -I {} -0 chmod 0755 {}
```

### shred


```bash
shred -n 200 -z -u  personalinfo.tar.gz
shred -vfz -n 10 /dev/sda5
```

## awk and sed

### awk sum

```bash
cut -d" " -f5 LargeFile.txt | sed 's/G//' | awk 'BEGIN{sum=0}{sum += $1}END{print sum}'
cut -d" " -f5 LargeFile.txt | sed 's/G//' | awk 'BEGIN{sum=0}{sum += $1}END{print sum/NR}'
```

### Remove the first line of file
#### Generate new file

```bash
sed 1d delete_old_capture_file.dump > delete_old_capture_file.list
```
#### Update same file

```bash
sed -i 1d /tmp/delete_old_capture_file.dump
```

## PDF, images and videos

### Combine / split PDFs


```bash
gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=combinedpdf.pdf -dBATCH 1.pdf 2.pdf 3.pdf
pdftk *.pdf cat output combined.pdf
pdftk combinedpdf.pdf burst
```

### Resize photo


```bash
find ./ -name '*.jpg' -exec convert -resize 600x480 {} {} \;
```

### Image file conversion


```bash
convert 1.pdf 1.jpg -density 250
```

### JVC mod file to mp4


```bash
ffmpeg -i MOV001.MOD -vcodec copy -acodec copy -f mp4 1.mp4
```

### Extract clip from video


```bash
avconv -ss <start-time> -i long-video.mp4 -codec copy -t <duration> important-clip.mp4
ffmpeg -ss 00:32:15 -t 00:00:48 -i long-video.mp4 -vcodec copy -acodec copy important-clip.mp4
```

### MOV to mp4


```bash
avconv -i 09380001.MOV  -acodec aac -strict experimental -ab 128k -vb 3000k -f mp4 carcam-`date +%Y%m%d`.mp4
```

## Multi-line recipe

### Output duplicated lines

For example based on the 2nd column duplicate. The awk script is


```bash
%%bash
  BEGIN { FS = "\t" }
  {
      # Keep count of the fields in second column
      count[$2]++;
  
      # Save the line the first time we encounter a unique field
      if (count[$2] == 1)
          first[$2] = $0;
  
      # If we encounter the field for the second time, print the
      # previously saved line
      if (count[$2] == 2)
          print first[$2];
  
      # From the second time onward. always print because the field is
      # duplicated
      if (count[$2] > 1)
          print
  }
```

Command

```bash
cut -f1,4,5,6 *.bim | sort -g -k2 | awk -f dup.awk
```
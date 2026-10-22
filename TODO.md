# TO DO:

## Project breakdown/script requirments:
!!! CANT USE BASE64 MODUAL !!!

Encode.py:

- [ ] Accept binary/image files
- [ ] `import base64`
- [ ] read image as bytes useing "rb" (read binary)
- [ ] Encode bytes into base64
- [ ] Make textfile from Encoded bytes
- [ ] Create text file
- [ ] Read filename and type of orignail file
- [ ] Take "file.type" and return "{file}_b64_{type}.txt"

- [ ] working prototype? 
 
Decode.py:

- [x] Read filename and type 
- [x] Remove "_b64_" from filename
- [x] Change and return filetype
- [x] Convert textfile to string
- [x] Interprate text as binary
- [x] Identify orignal filetype (or just assume everything is going to be a png)
- [x] Compile binary into orignal file type 
- [ ] target file can be called from script launch insted of user input

- [x] working prototype? 

## tutorials:

https://www.w3schools.com/python/ref_module_base64.asp

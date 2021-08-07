import os
import io
import re 
from fnmatch import fnmatch

tRoot = "php"
dRoot = "data"
pattern = "*.php"
targetPath = os.path.join(tRoot)
saveTo      = os.path.join(dRoot, targetPath)
saveToPath  = os.path.join(dRoot, 'strings.blade.php')
strings_data = []

if not os.path.exists(saveTo):
    os.makedirs(saveTo)

for targetPath, subdirs, files in os.walk(tRoot):
    for fileName in files:
        print(fileName+' >>> extracting... \n\n')
        if fnmatch(fileName, pattern):
            target_file = os.path.join(targetPath, fileName)
            
            f = open(target_file, 'r')
            file_code   = f.read()
            f.close()
            
            strs = re.findall("{{ __\(.+\) }}", file_code)
            
            for str in strs:
                strings_data.append(str)
            
strings_data = list(dict.fromkeys(strings_data))

for str in strings_data:
    with io.open(saveToPath, "a", encoding="utf-8") as file:
        file.write(str+'\n')
        file.close()


print('>>> STRING EXTRACTION COMPLETE <<<')
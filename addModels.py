#!/usr/local/bin/python

# run this script as the user which libretranslate service is running on
# do: ps aux | grep -i libretranslate from shell if unsure
import glob
from argostranslate import package, translate

models_path = './'
models_list = glob.glob(models_path + '*.argosmodel')

for model in models_list:
        print ('Adding model: ' + model)
        package.install_from_path(model)

print("Installed languages:")
installed_languages = translate.get_installed_languages()
for i in range(0,len(installed_languages)):
        print(installed_languages[i])

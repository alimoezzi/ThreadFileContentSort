import os

for i in os.scandir():
    if ' - lang_en_vs1' in i.name:
        try:
            os.rename(
                i.name,
                str(
                    int(
                        i.name.split(' - ')[0]
                    ) + 2
                ) + ' - ' + i.name.split(' - ')[1].rstrip() + ".srt")
        except Exception as e:
            print(e)
            os.system('pause')

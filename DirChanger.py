import os
from time import strftime, localtime

__path__ = []

mainDir = '.'
logFileName = 'DirChanger.log'
_file = None

oldDirName  = str(input('Old patch version: '))
newDirName  = str(input('New patch version: '))

if not oldDirName == newDirName:
    log = 'Changed directory of mod version\n'

    try:
        _file = open(os.path.join(mainDir, logFileName), 'w')
        _file.write('Changing time: ' + strftime('%H:%M:%S', localtime()) + '\n')
        _file.write(log)
            
        for _path, _sub_dirs, _files in os.walk(mainDir):
            if oldDirName in _sub_dirs:
                os.rename(os.path.join(_path, oldDirName), os.path.join(_path, newDirName))
                log = f'from {oldDirName} to {newDirName} in path: {_path}\n'
                _file.write(log)

    except IOError:
        print('Do not open file: %s\n' % logFileName)
    except:
        print('Upss, something is wrong!')

    finally:
        if _file:
            _file.close()

else:
    print(f"Stara wersja: {oldDirName} i nowa wersja: {newDirName} sa takie same!\n")

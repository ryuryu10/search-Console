#Segmentation fault: 11 > 권한 오류

from pick import pick
from function import setting
from function import scanner
setting.path('database/config.json')

title = 'HOME > \n원하시는 작업을 선택하세요 :'
options = ['시작하기', '환경설정']
option, index = pick(options, title)
if index == 0:
    if scanner.Connection(setting.view()['url']) == 200:
        print('사이트에 접속할 수 있음')
    else:
        print('사이트를 접속할 수 없음.')
elif index == 1:
    title = 'HOME > Setting\n원하시는 작업을 선택하세요 : '
    options = ['설정값 수정','설정값 보기','뒤로가기']
    option, index = pick(options, title)
    if index == 1:
        print(setting.view())
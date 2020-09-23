#엘베 하나로 돌림
import requests
url = 'http://localhost:8000'
tops = [5, 25, 25]
class Command:
    def __init__(self, i):
        self.command = {}
        self.command['elevator_id'] = i  # 엘베 번호
        self.command['command'] = ''     # 명령
        self.command['call_ids'] = []    # 나가거나 들어갈 번호
    def receive(self):
        if self.command['command'] == 'EXIT' or self.command['command']=='ENTER':
            return self.command
        del(self.command['call_ids'])
        return self.command

def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()

def commandQuery(node, cmd):
    node.command['command'] = cmd
    return node.receive()

def p0_simulator():
    user = 'tester'
    problem = 2               #문제 번호
    count = 1                 #사용할 엘베 수
    top = tops[problem]       #꼭대기층(1층 ~ 꼭대기층)
    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))
    dir = [1, 1, 1, 1]     #1위로, 0아래로
    while 1:
        #우선 엘베 한 대로 simulation
        temp = oncalls(token)
        if temp['is_end']: break
        commandList = [[]for _ in range(count)]
        for i, elevator in enumerate(temp['elevators']):
            flag=False                      #이 층에서 탈 수 있거나 내릴 수 있는거 확인
            c = Command(i)
            d = dir[i]                      #방향 저장해놓은거 가져옴
            calls = temp['calls']
            floor = elevator['floor']
            # 이 층에서 탈 사람이나(call[3]같고 call[4] 방향에 맞으면), 내릴 사람 있으면(passneger[3]이 층과 같으면))
            for passsenger in elevator['passengers']:  # 내릴사람~~?
                if passsenger['end'] == floor:
                    c.command['command']='EXIT'
                    c.command['call_ids'].append(passsenger['id'])
                    flag=True
            if flag:
                commandList[i] = c.receive()
                c = Command(i)
            if not flag:
                entered = 0
                for call in calls:  # 타실??
                    if len(elevator['passengers']) + entered + 1 > 8: break
                    if call['start'] == floor:
                        if d == 1:  # 올라가면a
                            if call['end'] > floor:
                                c.command['command'] = 'ENTER'
                                c.command['call_ids'].append(call['id'])
                                entered += 1
                        else:  # 내려가면
                            if call['end'] < floor:
                                c.command['command'] = 'ENTER'
                                c.command['call_ids'].append(call['id'])
                                entered += 1
            if entered >= 1:
                commandList[i] = c.receive()
                c = Command(i)
                flag=True
            #여기서부터 상태 처리
            if floor == 1 and d == -1: d = 1
            if floor == top and d == 1: d = -1
            status = elevator['status']
            if status == 'STOPPED':
                #멈춰있는데 내리거나 탈 사람이 있다~ 열어주세요~~
                if flag: commandList[i] = (commandQuery(c, 'OPEN'))
                # 그러지 못했음 이동
                else:
                    if d==1: commandList[i]=(commandQuery(c, 'UP'))
                    else: commandList[i] = (commandQuery(c, 'DOWN'))
            elif status == 'UPWARD' or status == 'DOWNWARD':    #가던 중에 멈춰야하면
                if flag or floor==top or floor==1: commandList[i] = (commandQuery(c, 'STOP'))
                else:
                    if d==1: commandList[i] = (commandQuery(c, 'UP'))
                    else: commandList[i] = (commandQuery(c, 'DOWN'))
            elif status == 'OPENED':    #열려있음!
                if flag: continue
                else: commandList[i] = (commandQuery(c, 'CLOSE'))
            dir[i] = d
        # print(status, floor, commandList)
        action(token, commandList)

if __name__ == '__main__':
    p0_simulator()


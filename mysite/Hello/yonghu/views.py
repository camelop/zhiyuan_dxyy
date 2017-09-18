from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Problem
import json
import time

def login(request):
    error_message = ""
    if 'username' in request.session.keys():
        return HttpResponseRedirect('/problems')
    if request.method == 'POST':
        if len(request.POST['username']) == 0:
            error_message = "Empty username."
        elif len(request.POST['password']) == 0:
            error_message = "Empty password."
        else:
            s = User.objects.filter(username=request.POST['username'])
            if len(s) == 0 or request.POST['password'] != s[0].password:
                error_message = "Incorrect username or password."
            else:
                request.session['username'] = request.POST['username']
                return HttpResponseRedirect('/problems')
    if 'username' in request.session.keys():
        context = {'error_message': error_message,'logined': 1, 'name': request.session['username']}
    else:
        context = {'error_message': error_message,'logined': 0, 'name': ''}
    return render(request, 'login.html', context)

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/login')

def problems(request):
    if 'username' not in request.session.keys():
    	return HttpResponseRedirect('/login')
    user = User.objects.filter(username=request.session['username'])[0]
    obj = json.loads(user.stat)
    mark = [x[0] for x in obj]
    H1 = [x[1] for x in obj]
    H2 = [x[2] for x in obj]
    open = json.loads(user.open)
    context = {'name': request.session['username'], 'user': user, 'H1_state': H1, 'H2_state': H2, 'mark_state': mark, 'open': open}
    return render(request, 'problems.html', context)

contentname=['','aadsfg','safda','24wrgfdgh','eragdfh','ratgdzfh','8iruytfhsdgf','uydthfgx','resgdfz','rthsdgzfbx','kiujhfgdf']
hint1name=['','8iyujghn','q2wr3st4dfg','vfgsty6','2eqrwfegr','4tegr6','qjttig','5ifnsk','4etgv7','dfgyhd','57utjyfhngj']
hint2name=['','9thfjco','hebev9j','jhnri9c','vy82btp','gsy6fu3','0rgbdlc','fwuhvb','sefhdjb','sfdhkjfah','y4bgl']

def problem(request, problem_id):
    if 'username' not in request.session.keys():
        return HttpResponseRedirect('/login')
    user = User.objects.filter(username=request.session['username'])[0]
    obj = json.loads(user.stat)
    H1 = [x[1] for x in obj]
    H2 = [x[2] for x in obj]
    obj2 = json.loads(user.open)
    if obj2[int(problem_id)-1] == 0:
        return HttpResponseRedirect('/problems')
    problem = Problem.objects.get(pk=problem_id)
    context = {'user': user, 'problem': problem, 'name': request.session['username'], 'content':contentname[int(problem_id)], 'hint1':hint1name[int(problem_id)], 'hint2':hint2name[int(problem_id)], 'H1': H1, 'H2': H2}
    return render(request, 'problem.html', context)

def unlock(request):
    if 'username' not in request.session.keys():
        return HttpResponseRedirect('/login')
    error_message = ""
    user = User.objects.filter(username=request.session['username'])[0]
    obj = json.loads(user.open)
    if obj[int(request.GET['problem_id'])-1] == 0:
        if user.point <= 0:
            return HttpResponseRedirect('/problems')
        user.point -= 1
        obj[int(request.GET['problem_id'])-1] = 1
        user.open = json.dumps(obj)
        user.save()
    return HttpResponseRedirect('/problems')

def submit(request):
    if 'username' not in request.session.keys():
        return HttpResponseRedirect('/login')
    user_list = User.objects.all()
    error_message = ''
    if request.method == 'POST':
        if len(request.POST['site']) == 0:
            error_message = "请输入地点编号。"
        elif len(request.POST['group']) == 0:
            error_message = "请输入小组编号。"
        elif len(request.POST['score']) == 0:
            error_message = "请输入任务分数。"
        else:
            user = User.objects.filter(username="group"+request.POST['group'])[0]
            problem_id = int(request.POST['site'])
            score = int(request.POST['score'])
            obj = json.loads(user.stat)
            if obj[problem_id - 1][0] == 0 and score != 0:
                user.point += 1
            user.mark += score - obj[problem_id - 1][0]
            obj[problem_id - 1][0] = score
            user.stat = json.dumps(obj)
            user.save()
            log = "第"+request.POST['group']+"组第"+request.POST['site']+"题的得分为"+request.POST['score']+", 备注信息："+request.POST['remark']+", 时间："+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()+3600*8)) + "\n"
            file = open('adminlog.txt','a')
            file.write(log)
            file.close()
            error_message = "提交成功！"
    if 'username' in request.session.keys():
        context = {'user_list':user_list, 'error_message': error_message,'logined': 1, 'name': request.session['username']}
    else:
        context = {'user_list':user_list, 'error_message': error_message,'logined': 0, 'name': ''}
    return render(request, 'submit.html', context)


def addpoint(request):
    if 'username' not in request.session.keys():
        return HttpResponseRedirect('/login')
    user_list = User.objects.all()
    error_message = ""
    if request.method == 'POST':
        if request.GET['action'] == 'add':
            for user in user_list:
                user.point += 3
                user.save()
                error_message = "增加点数成功！"
        if request.GET['action'] == 'clear':
            for user in user_list:
                user.point = 0
                user.mark = 0
                user.save()
                error_message = "点数清零成功！"
        if request.GET['action'] == 'refresh':
            return HttpResponseRedirect('/uhsnaidaij')
    if 'username' in request.session.keys():
        context = {'user_list':user_list, 'error_message': error_message,'logined': 1, 'name': request.session['username']}
    else:
        context = {'user_list':user_list, 'error_message': error_message,'logined': 0, 'name': ''}
    return render(request, 'addpoint.html', context)

def usehint(request):
    if 'username' not in request.session.keys():
        return HttpResponseRedirect('/login')
    user = User.objects.filter(username=request.session["username"])[0]
    if request.method == 'POST':
        problem_id = int(request.GET['problem'])
        hint_num = int(request.GET['hint_num'])
        obj = json.loads(user.stat)
        if obj[problem_id - 1][hint_num] == 0:
            obj[problem_id - 1][hint_num] = 1
            if hint_num == 1:
                if obj[problem_id - 1][0] == 0:
                    user.mark -= 20
            elif hint_num == 2:
                if obj[problem_id - 1][1] == 1:
                    if obj[problem_id - 1][0] == 0:
                            user.mark -= 30
                else:
                    if obj[problem_id - 1][0] == 0:
                        user.mark -= 50
                obj[problem_id - 1][1] = 1
            user.stat = json.dumps(obj)
            user.save()
    return HttpResponseRedirect('/problem/'+request.GET['problem'])
        

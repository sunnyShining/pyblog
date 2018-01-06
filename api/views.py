from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'api/index.html')

def upload(request):
    if request.method == 'POST':
        myfile = request.FILES.get('file')
        if not myfile:
            return JsonResponse({
                'code': '900001',
                'data': {},
                'msg': '未选择文件',
            })
        filename = myfile.name
        file = myfile.read()
        filesize = myfile.size
        if filesize == 0:
            return JsonResponse({
                'code': '900001',
                'data': {},
                'msg': '不能上传空文件',
            })
        with open('upload/%s' %filename, 'wb') as fn:
            fn.write(file)
            return JsonResponse({
                'code': '000000',
                'data': {
                    'path': 'upload/%s' % filename
                },
                'msg': '上传成功',
            })
    else:
        return JsonResponse({
            'code': '900001',
            'data': {},
            'msg': '上传失败',
        })
def download(request, filename):
    file = open('upload/%s' %filename).read()
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s' %filename
    return response
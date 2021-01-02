from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from urllib import parse
import boto3
from .models import Post
from boto3.dynamodb.conditions import Key, Attr
import operator
import pandas
# from .awsconfig import *
AWS_ACCESS_KEY_ID = "생략"
AWS_SECRET_ACCESS_KEY = "생략"
AWS_DEFAULT_REGION = ""

s3_bucket_name = 'fire-video-s3'
s3 = boto3.client('s3',
    region_name=AWS_DEFAULT_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# AWS S3 end
#######dynamodb/센서데이터###########
# 인증
dynamodb = boto3.resource('dynamodb',
    region_name=AWS_DEFAULT_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,)

# 사용할 테이블 지정
table = dynamodb.Table('sensor-data')

response = table.scan(

    FilterExpression=Attr('id').begins_with('2')
)
a = response['Items']
t_list = []
dic = {}

# 불러온 데이터 정렬
for i in range(len(a)):
   temp = sorted(a[i].items())
   dic[temp[1][0]+str(i)] = temp[1][1]
sdict= sorted(dic.items(), key=operator.itemgetter(1),reverse=True)

# 정렬한 데이터 중 가장 최근 데이터 11개로 df 만듦
fin = []
for j in range(0,11):
   response = table.query(KeyConditionExpression=Key('id').eq(sdict[j][1]))
   items=response['Items']
   # print(items[0]['id'])
   fin.append(items[0])

df = pandas.DataFrame(fin)

df['gas'] = df['gas'].astype(float)
time = pandas.to_datetime(df['id'], format='%y-%m-%d %H:%M:%S').apply(lambda x:x.strftime('%Y-%m-%d %H:%M:%S'))

#######dynamodb/센서데이터 끝###########

#######dynamodb/센서데이터 끝###########
def index(request):
    # posts = Post.objects.all()
    # context = {"posts":posts}
    video_list = Post.objects.all()
    context = {'posts' : video_list}
    return render(request, 'mainapp/index.html', context)
# 화재감지영상보기

def video(request):
    filed = get_filenames(s3) # file 이름들을 받아옴
    # print(filed)
    if request.method == "POST":
        idd = request.POST.get("select1", None)
        AWS_STORAGE_BUCKET_NAME = 'fire-video-s3'
        AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
        DATE = parse.quote(str(idd[:8])) # url 형식으로 바꾸어 주기
        TIME = parse.quote(str(idd[9:]))
        print(idd[:9], idd[10:])
        FILENAME = 'video.mp4'
        VIDEO_URL = 'https://%s/%s+%s/%s' % (AWS_S3_CUSTOM_DOMAIN, DATE, TIME, FILENAME)
        content = {'static_url': VIDEO_URL,
        'datetimelist':filed , 'datetime':idd, 'DATE':DATE, 'TIME':str(idd[9:])}
        return render(request, 'mainapp/video-view.html', content)
    return render(request, 'mainapp/video-view.html', {'datetimelist':filed, 'static_url':1})


# 지도시각화
def mapview(request): # 빅데이터 지도시각화
    return render(request, 'mainapp/mapview.html', None)
def maptest(request):
    return render(request, 'mainapp/map_object.html', None)

# 실시간 그래프
def realtime(request):
    return render(request, 'mainapp/realtime.html')

# video : 영상 날짜/시간 가져오기
def get_filenames(s3):
    filedic = [] # 날짜 : [시간] 을 저장
    result = s3.list_objects_v2(Bucket=s3_bucket_name, Prefix='')
    for item in result['Contents']:
        files = item['Key']
        filedic.append(files[:-10])
        # if len(files) > 9:
        #     key = files[:10]
        #     val = files[11:19]
        #     if key in filedic.keys():
        #         filedic[key].append(val)
        #     else:
        #         filedic[key] = [val]
    return filedic

def sensor(request):
    data = []
    type = request.GET.get('type')
    if type == 'initial': # type=initial 일때, 기존 DB에 있는 가장 최근 값 10개
        for i in range(10, 0, -1):
            data.append({"x": time[i], "y": df['gas'].iloc[i]})
    else:
        data.append({"x": time[0],"y": df['gas'].iloc[0]}) # type=initial 아닐 때, 가장 최근 찍힌 센서값
    return JsonResponse(data, safe=False)

def sensor_data(request) :
    return render(request, 'realtime.html', None)
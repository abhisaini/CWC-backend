from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post, Applicant
import json
@csrf_exempt
def createUser(request, method = ['POST']):
    req_data = json.loads(request.body.decode('utf-8'))
    user = User(id = req_data["id"], password = req_data["pass"])
    user.save()
    return HttpResponse(user.id)
@csrf_exempt
def getUsers(request,method = ['GET']):
    users = User.objects.all()
    user_json = [{
        "id" : str(x.id)
    } for x in users]
    return HttpResponse(json.dumps(user_json), content_type="application/json")


@csrf_exempt
def login(request,method = ['POST', 'GET']):
    if request.method == 'GET' :
        req_data = {
            "id" : request.GET["id"],
            "pass" : request.GET["pass"]
        }
    else :
        print(request.body, " : BODY")
        req_data = json.loads(request.body.decode('utf-8'))
    print(req_data)
    if(User.objects.filter(id = req_data['id'])):
        user = User.objects.get(id = req_data['id'])
        if user.password == req_data['pass']:
            request.session['user'] = req_data['id']
            print(request.session['user'])
    return HttpResponse(request.session.get("user"))
# Create your views here.

@csrf_exempt
def createPost(request,method = ['POST']):
    if request.method == 'POST' :
        if not request.session.get('user', None):
            msg = {"err" : "not logged in"}
            return HttpResponse(json.dumps(msg), content_type="application/json")
        req_data = json.loads(request.body.decode('utf-8'))
        user = request.session["user"]
        club = req_data["club"]
        title = req_data["title"]
        content = req_data["content"]
        post = Post(
            club= club,
            title = title,
            content = content,
            owner = user
        )
        post.save()
        msg = {"msg" : "success"}
        return HttpResponse(json.dumps(msg), content_type="application/json")
@csrf_exempt
def getPosts(request,method = ['GET']):
    posts = Post.objects.all()
    post_json = [{
        "title" : x.title,
        "content" : x.content,
        "owner" : x.owner,
        "club" : x.club,
        "id" : str(x.id),
        "created_at" : str(x.created_at),
        "updated_at" : str(x.updated_at)
    } for x in posts]
    return HttpResponse(json.dumps(post_json), content_type="application/json")

@csrf_exempt
def deletePost(request):
    postId = request.GET["id"]
    if not request.session.get('user', None):
        msg = {"err" : "user not logged in"}
        return HttpResponse(json.dumps(msg), content_type="application/json")
    if not Post.objects.filter(id = postId):
        msg = {"err" : "no such item exist"}
        return HttpResponse(json.dumps(msg), content_type="application/json")
    post = Post.objects.get(id=postId) 
    if request.session["user"] != post.owner:
        msg = {"err" : "user dont have permissions to delete the item"}
        return HttpResponse(json.dumps(msg), content_type="application/json")
    post.delete()
    msg = {"msg" : "deleted"}
    return HttpResponse(json.dumps(msg), content_type="application/json")


@csrf_exempt
def checksession(request,method = ['POST', 'GET']):
    print(request.session['user'])
    return HttpResponse(request.session.get("user"))

@csrf_exempt
def applyVolunteer(request, method = ['POST']):
    if request.method == 'POST' :
        req_data = json.loads(request.body.decode('utf-8'))
        name = req_data["name"]
        mobile = req_data["mobile"]
        address = req_data["address"]
        applicant = Applicant(
            name = name,
            mobile = mobile,
            address = address
        )
        applicant.save()
        msg = {"msg" : "success"}
        return HttpResponse(json.dumps(msg), content_type="application/json")
 
def getApplicant(request, method = ['GET']):
    applicants = Applicant.objects.all()
    applicant_json = [{
        "name" : x.name,
        "mobile" : x.mobile,
        "address" : x.address,
        "timestamp" : str(x.timestamp),
        "id" : str(x.id),
    } for x in applicants]
    return HttpResponse(json.dumps(applicant_json), content_type="application/json")
    
#

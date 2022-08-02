def visited(request,ref_visitor,instance):
    if ref_visitor !=0:
        instance.num_of_visitors+=1
        instance.save()
        request.session["ref_visitor"]=0
    else:
        print(ref_visitor)

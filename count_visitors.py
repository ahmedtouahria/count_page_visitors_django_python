def visited(request,ref_visitor,instance):
    if ref_visitor !=instance.id:
        instance.num_of_visitors+=1
        instance.save()
        request.session["ref_visitor"]=instance.id
    else:
        print(ref_visitor)

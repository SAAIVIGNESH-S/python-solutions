def fun(s):
    try:
        username, url = s.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False
    
    if not(username.replace('-','').replace('_','').isalnum()):
        return False
    
    elif not(website.isalnum()):
        return False
    
    elif len(extension) > 3:
        return False
    
    else :
        return True

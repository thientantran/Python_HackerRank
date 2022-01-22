def fun(s):
    import re
    # return True if s is a valid email, else return False
    t=re.search(r'^[\w\d-]+\@[a-zA-Z0-9]+\.\w?\w?\w?$',s)
    if t:
        return True
    else:
        return False
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
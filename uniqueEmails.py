def uniqueEmail(emails):
  #emails = set(emails)
  emailSet = []
  for email in emails:
    email, domain = email.split("@")[0], email.split("@")[1]
    email = email.replace('.','') 
    email = list(email)
    if '+' in email: email = email[0:email.index('+')]
    email = ''.join(email)
    email += "@" + domain
    emailSet.append(email)
  print(emailSet)
  emailSet = set(emailSet)
  return len(emailSet)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(uniqueEmail(emails))

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(uniqueEmail(emails))

emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(uniqueEmail(emails))
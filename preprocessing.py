import re

def cleanAmp(post):
  return re.sub(r"&amp;", "&", post)

def cleanGt(post):
  return re.sub(r"&gt;", ">", post)

def cleanLt(post):
  return re.sub(r"&lt;", "<", post)

def cleanNumbers(post):
  return re.sub(r"[0-9+", "", post)

def cleanURL(post):
  return re.sub(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", "", post)

def cleanLbTag(post):
  return re.sub(r"<lb>", " ", post)

def cleanTabTag(post):
  return re.sub(r"<tab>", " ", post)

def toLowerCase(post):
  return post.lower()

def cleanBrackets(post):
  return re.sub(r"[\(\[\{\}\]\)]", " ", post)

def cleanSymbols(post):
  return re.sub(r"[\+\-\*#\"\?!@\.,;:_\$\€><~\/\^•\|]", " ", post)

def cleanNumbers(post):
  return re.sub(r"[0-9]", "", post)

def cleanApexes(post):
  return re.sub(r"\W\'([a-zA-Z0-9_ ]*)\'", r"\1", post)

def cleanEmoji(post):
  emoji = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
  return emoji.sub(r'', post)

def normalizeUser(post):
  return re.sub(r"\/?u\/\w*", "user", post)

def normalizeSub(post):
  return re.sub(r"\/?r\/\w*", "subreddit", post)

def normalizeWords(post):
  words = {"y'all": "you all", "af": "as fuck", "bf": "boyfriend", "gf": "girlfriend", "bff": "bestfriend", 
           "bif": "before i forget", "bol": "best of luck", "bot": "back on topic", "btw": "by the way", "bcos": "because", 
           "cmon": "come on", "cos": "because", "cuz": "because", "da": "the", "dl": "download", "dm": "direct message", 
           "em": "them", "imho": "in my honest opinion", "imo": "in my opinion", "omg": "oh my god", "tbh": "to be honest",
           "u": "you"}
  for w, w2 in words.items():
    if(w in post):
      post.replace(w, w2)
  return post

def clean(post):
  post = cleanAmp(post)
  post = cleanGt(post)
  post = cleanLt(post)
  post = cleanURL(post)
  post = cleanLbTag(post)
  post = cleanTabTag(post)
  post = toLowerCase(post)
  post = cleanBrackets(post)
  post = normalizeUser(post)
  post = normalizeSub(post)
  post = normalizeWords(post)
  post = cleanSymbols(post)
  post = cleanNumbers(post)
  post = cleanApexes(post)
  post = cleanEmoji(post)
  return post
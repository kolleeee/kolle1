import mechanize
#requests 模拟提交表单登陆DZ BBS  发帖  回帖 QQ29295842
br = mechanize.Browser()
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open(r'http://bbs.sandaha.com/forum.php')

formcount=0
for frm in br.forms():  
  if str(frm.attrs["id"])=="lsform":
    break
  formcount=formcount+1
br.select_form(nr=formcount)
control=br.form.find_control('username')
control.value='2602159946'

control=br.form.find_control('password')
control.value='2602159946'
response = br.submit()

open('b2.html','w').write(response.read())
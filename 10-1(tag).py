txt = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system
and test content databases. The content for each topic is
created by experts and is all carefully designed with a
comprehensive knowledge to greatly benefit all candidates
who participate."""

txtLower = txt.lower()

for ch in txtLower:
    if ch in ".,?":
        txtLower = txtLower.replace(ch,'')
        
txtLst = txtLower.split()       
setX = set(txtLst)              
lst = list(setX)                
print("最後串列 = ", sorted(lst))

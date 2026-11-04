# Turns the canvas files in project/ into plain HTML pages in assets/ (fonts, logo and QR codes sit there too).
# Then print each page from Chrome at 100% scale, no margins, to get the print PDF.
# PDF page order: Counter-front, Counter-back, Postcard-front, Postcard-back, Pocket-cards (cardstock), Board-poster (plain paper).
import re, sys, os
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(HERE,'project')
blobs={'c16d331316db5d74af8231d1430645f3':'staffkin-logo.svg','61e7acffaa86676d9034e8dc166fceb4':'qr-counter.svg',
'5347a7794130c861059da524b6c03e6d':'qr-refs.png','c6003d8666ebe245fa0f8a44b007fdb3':'qr-poster.svg','209a091d3d2763fbcd6b25731827beee':'qr-pocket.svg'}
for f,n in [('Counter-front.dc.html',4),('Counter-back.dc.html',4),('Postcard-front.dc.html',4),('Postcard-back.dc.html',4),('Board-poster.dc.html',1),('Pocket-cards.dc.html',10)]:
    s=open(os.path.join(SRC,f)).read()
    for k,v in blobs.items(): s=s.replace('/_blob/'+k,v)
    s=re.sub(r'<script src="./support.js"></script>','',s)
    s=re.sub(r'<script type="text/x-dc".*?</script>','',s,flags=re.S)
    s=re.sub(r'<sc-for[^>]*>(.*?)</sc-for>',lambda m:m.group(1)*n,s,flags=re.S)
    s=s.replace('<x-dc>','').replace('</x-dc>','').replace('<helmet>','').replace('</helmet>','')
    ff=''.join(f"@font-face{{font-family:Outfit;font-weight:{w};src:url(outfit-latin-{w}-normal.woff2)}}" for w in (400,500,600))
    s=re.sub(r'<link[^>]*fonts.g[^>]*>','',s)
    s=s.replace('<style>','<style>'+ff+'@page{size:8.5in 11in;margin:0}html,body{margin:0}')
    open(os.path.join(HERE,'assets',f.replace('.dc.html','.html')),'w').write(s)
print('ok')

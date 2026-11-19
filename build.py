# Rebuild index.html from template.html + img/ (embeds images as base64)
import base64, glob, os, re
t = open('template.html').read()
for p in glob.glob('img/*'):
    k = os.path.splitext(os.path.basename(p))[0]
    mime = 'image/png' if p.endswith('.png') else 'image/jpeg'
    t = t.replace('{{' + k + '}}', 'data:%s;base64,%s' % (mime, base64.b64encode(open(p, 'rb').read()).decode()))
left = re.findall(r'\{\{\w+\}\}', t)
assert not left, left
open('index.html', 'w').write(t)
print('index.html', os.path.getsize('index.html'), 'bytes')
